#!/usr/bin/python3
"""
A basic LRU Cache implementation
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRU Cache Base class
    """

    def __init__(self):
        super().__init__()
        self.LRU_tracker = OrderedDict()

    def put(self, key, item):
        """
        adds a new item to LRU Cache
        """
        if key is None and item is None:
            return
        if key in self.cache_data:
            self.LRU_tracker.move_to_end(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            leased_used_key, _ = self.LRU_tracker.popitem(last=False)
            print(f'DISCARD: {leased_used_key}')
            self.cache_data.pop(leased_used_key)
        self.cache_data[key] = item
        self.LRU_tracker[key] = 0

    def get(self, key):
        """
        retrieves item from the cache
        """
        if key in self.cache_data:
            self.LRU_tracker.move_to_end(key)
        return self.cache_data.get(key)
