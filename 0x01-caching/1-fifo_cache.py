#!/usr/bin/python3
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """create a class FIFOCache inherits BaseCaching"""
    def __init__(self):
        """overload def __init__(self): but don’t forget to call the parent
        init: super().__init__()"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data the item value for
        the key key"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                fifo = self.keys[0]
                self.keys.pop(0)
                del self.cache_data[fifo]
                print('DISCARD: {}'.format(fifo))

    def get(self, key):
        """Must return the value in self.cache_data linked to key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
