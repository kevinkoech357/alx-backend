#!/usr/bin/env python3

"""
Create a class BasicCache that inherits from
BaseCaching and is a caching system.
"""


from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    Define put and get methods.
    """

    def __init__(self):
        """
        Initialize a BasicCache object.
        """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """
        Add an item to Cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the most recently used item (LRU)
                discarded_key, _ = self.order.popitem(last=True)
                print(f"DISCARD: {discarded_key}")
                if discarded_key in self.cache_data:
                    del self.cache_data[discarded_key]
            self.cache_data[key] = item
            self.order[key] = None

    def get(self, key):
        """
        Retrieve an item from cache based on key.
        """
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
