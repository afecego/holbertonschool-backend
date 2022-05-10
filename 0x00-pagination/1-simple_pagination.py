#!/usr/bin/env python3
"""Implement a method named get_page that takes two integer arguments page with
default value 1 and page_size with default value 10"""
import csv
from typing import List


def index_range(page, page_size):
    """return in a list for those particular pagination parameters
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """If the input arguments are out of range for the dataset, an empty
        list should be returned"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        [first, last] = index_range(page, page_size)
        return self.dataset()[first:last]
