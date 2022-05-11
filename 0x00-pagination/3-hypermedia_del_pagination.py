#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """The goal here is that if between two queries, certain rows are
        removed from the dataset, the user does not miss items from dataset
        when changing page."""
        assert isinstance(index, int)
        assert 0 < index < len(self.dataset())
        data = self.indexed_dataset()
        data_dict = {}

        i = index
        while (len(data_dict) < page_size and i < len(self.dataset())):
            if i in data:
                data_dict[i] = data[i]
            i += 1

        info_end = list(data_dict.values())
        indexes = data_dict.keys()

        return {
            'index': index,
            'data': info_end,
            'page_size': len(info_end),
            'next_index': max(indexes) + 1
        }
