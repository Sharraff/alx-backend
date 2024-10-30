#!/usr/bin/env python3
""" caching system
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Caching system:

    Args:
        LFUCache ([class]): [basic caching]
    """

    def __init__(self):
        """
        initialization of base class
        """
        super().__init__()
        self.temp_list = {}

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None and item is None:
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                pop_item = min(self.temp_list, key=self.temp_list.get)
                self.temp_list.pop(pop_item)
                self.cache_data.pop(pop_item)
                print(f'DISCARD: {pop_item}')
            if not (key in self.temp_list):
                self.temp_list[key] = 0
            else:
                self.temp_list[key] += 1

    def get(self, key):
        """
        Get an item in cache by key
        """
        if (key is None) or not (key in self.cache_data):
            return None
        self.temp_list[key] += 1
        return self.cache_data.get(key)
