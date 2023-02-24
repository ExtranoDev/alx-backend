#!/usr/bin/env python3
"""FIFO caching"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """initialization"""
        super().__init__()

    def put(self, key, item):
        """assign to cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key_temp = list(self.cache_data.items())[0][0]
            del self.cache_data[key_temp]
            print("DISCARD: {}".format(key_temp))

    def get(self, key):
        """return a value linked to the key"""
        data = self.cache_data.get(key)
        return data if data is not None else None
