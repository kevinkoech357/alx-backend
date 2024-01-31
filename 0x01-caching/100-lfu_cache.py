#!/usr/bin/env python3

"""
Create a class BasicCache that inherits from
BaseCaching and is a caching system.
"""


from base_caching import BaseCaching
from collections import OrderedDict, defaultdict


class LFUCache(BaseCaching):
    """
    Define put and get methods.
    """

    def __init__(self):
        """
        Initialize a BasicCache object.
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.order = OrderedDict()

    def evict_least_frequent(self):
        """
        Evict the least frequently used item (LFU) from the cache.
        """
        min_frequency = min(self.frequency.values())

        # Find all items with the minimum frequency
        items_with_min_frequency = [
            key for key, freq in self.frequency
            .items() if freq == min_frequency
        ]

        # If multiple items have the same frequency,
        # use LRU to choose the least recently used one
        key_to_discard = min(
            items_with_min_frequency, key=lambda key: (self.order[key], key))

        # Print and remove the least frequently used item
        print(f"DISCARD: {key_to_discard}")
        del self.cache_data[key_to_discard]
        del self.frequency[key_to_discard]
        del self.order[key_to_discard]

    def put(self, key, item):
        """
        Add an item to Cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.evict_least_frequent()

            self.cache_data[key] = item
            self.frequency[key] += 1
            # None value to maintain order based on insertion time
            self.order[key] = None

    def get(self, key):
        """
        Retrieve an item from cache based on key.
        """
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
