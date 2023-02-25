#!/usr/bin/env python3
"""LRU caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """initialization"""
        super().__init__()
        self.lru = []

    def put(self, key, item):
        """Handles LRUCache Item management"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.lru:
                self.lru.remove(key)
            self.lru.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                to_remove = self.lru[0]
                del self.cache_data[to_remove]
                self.lru.pop(0)
                print("DISCARD: {}".format(to_remove))

    def get(self, key):
        """return a value linked to the key and updated access time"""
        data = self.cache_data.get(key)
        if data:
            if key in self.lru:
                self.lru.remove(key)
            self.lru.append(key)
            return data
        return None
