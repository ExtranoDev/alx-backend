#!/usr/bin/env python3
"""LIFO caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """initialization"""
        super().__init__()

    def put(self, key, item):
        """assign to cache"""
        if key is not None and item is not None:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                temp_key = list(self.cache_data.items())[-1][0]
                del self.cache_data[temp_key]
                print("DISCARD: {}".format(temp_key))
            self.cache_data[key] = item

    def get(self, key):
        """return a value linked to the key"""
        data = self.cache_data.get(key)
        return data if data is not None else None
