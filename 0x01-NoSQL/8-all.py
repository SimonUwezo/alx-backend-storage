#!/usr/bin/env python3
"""function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """Function that lists all documents in a collection

    Args:
        mongo_collection (pymongo.collection.Collection): collection to analyze

    Returns:
        list:  all documents in a collection or empty list.
    """
    return [doc for doc in mongo_collection.find()]
