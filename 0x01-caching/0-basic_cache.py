#!/usr/bin/python3
"""Basic dictionary"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    basic Caching system
    """

    def put(self, key, item):
        """
        adds new item to cashe
        """
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        retrieves item form cache
        """
        return self.cache_data.get(key)
