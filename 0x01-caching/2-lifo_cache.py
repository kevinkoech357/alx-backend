#!/usr/bin/env python3

"""
Create a class BasicCache that inherits from
BaseCaching and is a caching system.
"""


from base_caching import BaseCaching
from collections import deque


class LIFOCache(BaseCaching):
    """
    Define put and get methods.
    """

    def __init__(self):
        """
        Initialize a BasicCache object.
        """
        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """
        Add an item to Cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the last item (LIFO)
                discarded_key = self.order.pop()
                print(f"DISCARD: {discarded_key}")
                if discarded_key in self.cache_data:
                    del self.cache_data[discarded_key]
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Retrieve an item from cache based on key.
        """
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
