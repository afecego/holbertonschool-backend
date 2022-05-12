#!/usr/bin/python3
"""MRUCache caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """create a class MRUCache inherits BaseCaching"""
    def __init__(self):
        """overload def __init__(self): but don’t forget to call the parent
        init: super().__init__()"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data the item value for
        the key key and discard the least recently used item (LRU algorithm)"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.pop(self.keys.index(key))
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                lifo = self.keys[0]
                self.keys.pop(0)
                del self.cache_data[lifo]
                print('DISCARD: {}'.format(lifo))

    def get(self, key):
        """Must return the value in self.cache_data linked to key"""
        if key is not None and key in self.cache_data:
            self.keys.pop(self.keys.index(key))
            self.keys.append(key)
            return self.cache_data[key]
        return None
