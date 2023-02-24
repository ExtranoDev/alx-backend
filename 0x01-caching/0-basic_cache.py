#!/usr/bin/env python3
"""Basic Dictionary"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache that inherits from BaseCaching and
        is a caching system"""
    def __init__(self):
        """initialization"""
        super().__init__()

    def put(self, key, item):
        """assign to dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return a value linked to the key"""
        data = self.cache_data.get(key)
        return data if data is not None else None
