#!/usr/bin/env python3

"""
Create a class BasicCache that inherits from
BaseCaching and is a caching system.
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Define put and get methods.
    """

    def __init__(self):
        """
        Initialize a BasicCache object.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to Cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from cache based on key.
        """
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
