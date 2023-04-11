#!/usr/bin/env python3
''' Task 11's module.
'''
import pymongo


def schools_by_topic(mongo_collection, topic):
    ''' Returns th list of school having a specific topic.
    '''
    return mongo_collection.find({"topics": topic})
