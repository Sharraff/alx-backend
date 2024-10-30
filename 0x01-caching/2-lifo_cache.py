#!/usr/bin/python3
"""
A minimal LIFO Cache implementation
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    A LIFO cache class
    """

    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        adds new item to cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.stack.remove(key)

        elif len(self.cache_data) >= self.MAX_ITEMS:
            key_to_discard = self.stack.pop()
            print(f'DISCARD: {key_to_discard}')
            self.cache_data.pop(key_to_discard)
        self.stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        retrieves item from cache
        """
        return self.cache_data.get(key)
