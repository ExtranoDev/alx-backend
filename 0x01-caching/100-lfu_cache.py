#!/usr/bin/env python3
"""LFU caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LRUCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """initialization"""
        super().__init__()
        self.lru = {}

    def put(self, key, item):
        """Handles LRUCache Item management"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                to_remove = min(self.lru, key=self.lru.get)
                del self.lru[to_remove]
                del self.cache_data[to_remove]
                print("DISCARD: {}".format(to_remove))
            if key in self.lru:
                self.lru[key] += 1
            else:
                self.lru[key] = 0

    def get(self, key):
        """return a value linked to the key and updated access time"""
        if key in self.lru:
            self.lru[key] += 1
        return self.cache_data.get(key)
