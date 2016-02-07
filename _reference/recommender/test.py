import sys
from pymongo import MongoClient

from dataservice import DataService
from task import RecommenderTask

def persist_download_history_and_app_info():
    # persist data into 2 tables
    # user_download_history - (user_id, download_history)
    # app_info              - (app_id, app_name)

    # clean up to remove all old data
    DataService.clean_up()

    # persist work done here
    DataService.read_then_persist('data/sample.data')

    # print for testing, comment out anything below within try block if you want

    # print db and collections, they will show only if any data was persisted
    print "dbs: " + str(DataService.client.database_names())
    db = DataService.db
    print "collections: " + str(db.collection_names()) + "\n"

    # print user_download_history
    user_download_history_cursor = DataService.get_cursor_user_download_history()
    print "user_download_history: count=" + str(user_download_history_cursor.count())
    for user_download_history in user_download_history_cursor:
        print "  " + str(user_download_history)
    print ""

    # print app_info
    app_info_cursor = DataService.get_cursor_app_info()
    print "app_info: count=" + str(app_info_cursor.count())
    for app_info in app_info_cursor:
        print "  " + str(app_info)
    print ""

def load_user_download_history():
    # retrieval work done here
    result = DataService.retrieve_user_download_history()

    # print user download history
    #print "user_download_history: \n  " + str(result) + "\n"

    return result

def load_app_info():
    # retrieval work done here
    result = DataService.retrieve_app_info()

    # print app info
    #print "app_info: \n  " + str(result) + "\n"

    return result

def persist_top_5_apps_for_app(user_download_history, app_info):
    # calculate recommended 5 apps and persist the as a new attribute in app_info collection
    task = RecommenderTask(user_download_history, app_info)
    task.calculate_and_persist_top_5_app_single_thread()

    # print app info
    #print ""
    #print "app_info: \n  " + str(DataService.retrieve_app_info()) + "\n"

def load_top_5_apps(app_id):
    return DataService.retrieve_app_info({'app_id': app_id})

def main():
    try:
        # print to a file
        # f = file('log.txt', 'w')
        # sys.stdout = f

        # get MongoDB client and set it in DataService
        client = MongoClient('localhost', 27017) # or client = MongoClient('mongodb://localhost:27017/')
        DataService.init(client)

        # persist_download_history_and_app_info()
        user_download_history = load_user_download_history()
        app_info = load_app_info()
        persist_top_5_apps_for_app(user_download_history, app_info)

        # print for testing
        #print "app_info: \n  " + str(load_top_5_apps('C10107104'))

    except Exception as e:
        print "Exception! Go fix it!"
        print e

    finally:
        # clean up work
        if 'client' in locals():
            client.close()
        # sys.stdout = sys.__stdout__
        # if 'f' in locals():
        #     f.close()


if __name__ == "__main__":
    main()
