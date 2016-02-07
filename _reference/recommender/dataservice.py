from pymongo import MongoClient
import random


class DataService(object):

    @classmethod
    def init(cls, client):
        cls.client = client
        cls.db = client.appstore
        cls.user_download_history = cls.db.user_download_history
        cls.app_info = cls.db.app_info

    @classmethod
    def clean_up(cls):
        # drop the 2 collections
        cls.user_download_history.drop()
        cls.app_info.drop()

    @classmethod
    def read_then_persist(cls, filename):
        try:
            user_id = 1
            file = open(filename, 'r')
            for line in file:
                # process each line of the file
                if line.startswith('-'):
                    continue
                apps = line.split('\t')[3]
                apps = apps.rstrip(',').split(',')
                apps = apps[:10]
                if len(apps) < 6:
                    continue
                apps = cls.__pick_random_6_to_10(apps)
                download_history = []
                for app in apps:
                    info = app.split(':')
                    app_id = info[0]
                    title = info[1]
                    # store in collection app_info
                    document = {'app_id': app_id, 'title': title}
                    cls.persist_app_info(document)
                    download_history.append(app_id)
                # store in collection user_download_history
                cls.persist_user_download_history(user_id, download_history)
                user_id += 1
        except Exception as e:
            print e
        finally:
            file.close()

    @classmethod
    def __pick_random_6_to_10(cls, apps):
        if len(apps) < 10:
            return apps
        return random.sample(apps, random.randint(6, 10))

    @classmethod
    def persist_user_download_history(cls, user_id, download_history):
        new_doc = {'user_id': user_id, 'download_history': download_history}
        return cls.user_download_history.insert_one(new_doc)

    @classmethod
    def persist_app_info(cls, document):
        filter_dict = {'app_id': document['app_id']}
        return cls.app_info.replace_one(filter_dict, document, True)

    @classmethod
    def retrieve_user_download_history(cls, filter_dict={}):
        # return a dict {user_id: download_history} containing user download history data
        # return all data in the collection if no filter is specified
        result = {}
        cursor = cls.get_cursor_user_download_history(filter_dict)
        for user_download_history in cursor:
            result[user_download_history['user_id']] = user_download_history['download_history']
        return result

    @classmethod
    def retrieve_app_info(cls, filter_dict={}):
        # return a dict {app_id: {title}} containing user download history data
        # return all data in the collection if no filter is specified
        result = {}
        cursor = cls.get_cursor_app_info(filter_dict)
        for app_info in cursor:
            app_id = app_info['app_id']
            title = app_info['title']
            result[app_id] = {'title': title}
            try:
                top_5_app = app_info['top_5_app']
                result[app_id]['top_5_app'] = top_5_app
            except KeyError:
                pass
        return result

    @classmethod
    def update_app_info(cls, filter_dict, update):
        cls.app_info.update_one(filter_dict, update, True)

    @classmethod
    def get_cursor_user_download_history(cls, filter_dict={}):
        return cls.user_download_history.find(filter_dict)

    @classmethod
    def get_cursor_app_info(cls, filter_dict={}):
        return cls.app_info.find(filter_dict)
