#!/usr/bin/env python3
"""function that changes all topics of a school document
"""


def update_topics(mongo_collection, name, topics):
    """Function that changes all topics of a school document based on name.

    Args:
        mongo_collection (pymongo.collection.Collection): collection to analyze
        name (str): school name to update.
        topics (list): ist of topics approached in the school.
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
