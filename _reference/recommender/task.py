import operator
import thread
import time

from dataservice import DataService


class RecommenderTask(object):

    def __init__(self, dict_user_download_history, dict_app_info):
        self.dict_user_download_history = dict_user_download_history
        self.dict_app_info = dict_app_info

    def calculate_and_persist_top_5_app_single_thread(self):
        # find the 5 top recommended app for each app and persist them in app_info
        print "calculate_and_persist_top_5_app_single_thread()"
        start = time.clock() # start time of processor time

        download_history = self.dict_user_download_history.values()
        for app in self.dict_app_info.keys():
            self.run(app, download_history)

        end = time.clock() # end time of processor time
        print "time elapsed = " + str(end - start)

    def calculate_and_persist_top_5_app_multi_thread(self):
        # find the 5 top recommended app for each app and persist them in app_info
        print "calculate_and_persist_top_5_app_multi_thread()"
        start = time.clock() # start time of processor time
        
        download_history = self.dict_user_download_history.values()
        for app in self.dict_app_info.keys():
            task = self.create_task(app, download_history)
            thread.start_new_thread(task.run, ())

        end = time.clock() # end time of processor time
        print "time elapsed = " + str(end - start)

    def run(self, app, download_history):
        # This need serious optimization where we calculate similarity as A->B B->A is always dup
        # Ideally loop through all download history

        # create a dict to store each other app and its similarity to this app
        app_similarity = {} # {app_id: similarity}

        for apps in download_history:
            if app not in apps:
                continue
            #calculate the similarity
            similarity = Helper.cosine_similarity_app_applist(app, apps)
            for other_app in apps:
                if other_app == app:
                    continue
                if app_similarity.has_key(other_app):
                    app_similarity[other_app] = app_similarity[other_app] + similarity
                else:
                    app_similarity[other_app] = similarity

        # ignore apps not in any download history
        if len(app_similarity) == 0:
            return

        # sort app_similarity dict by value and get the top 5 as recommendation
        sorted_tups = self.__sort_dict_by_value(app_similarity)
        #print sorted_tups
        top_5_app = [sorted_tups[0][0], sorted_tups[1][0], sorted_tups[2][0], sorted_tups[3][0], sorted_tups[4][0]]
        #print "top_5_app for " + str(self.app) + ":\t" + str(top_5_app)

        # store the top 5
        DataService.update_app_info({'app_id': app}, {'$set': {'top_5_app': top_5_app}})

    def __sort_dict_by_value(self, dictionary):
        return sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)

class Helper(object):

    @classmethod
    def cosine_similarity_app_applist(cls, app, app_list):
        return cls.__cosine(1, 1, len(app_list))

    @classmethod
    def cosine_similarity_applist_applist(cls, app_list1, app_list2):
        match_count = cls.__count_match(app_list1, app_list2)
        return cls.__cosine(match_count, len(app_list1), len(app_list2))

    @classmethod
    def __count_match(cls, list1, list2):
        count = 0
        for element in list1:
            if element in list2:
                count += 1
        return count

    @classmethod
    def __cosine(cls, match, len1, len2):
        return float(match) / (len1 * len2)