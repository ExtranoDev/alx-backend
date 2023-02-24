#!/usr/bin/env python3
"""Simple Pagination"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int):
    """Funtion returns a tuple of size two
       containing a start index and an end index
       Returns: start_idx and end_idx
       args:
            page(int): page index
            page_size(int): page size
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return start_idx, end_idx


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
        """Returns page of pagination data passed"""
        assert type(page) == int and type(page_size) == int
        assert page > 0
        assert page_size > 0
        pages = index_range(page, page_size)
        dataset = self.dataset()
        try:
            return [self.__dataset[i] for i in range(pages[0], pages[1])]
        except Exception:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Implement a get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary
        args:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """
        pages = self.get_page(page, page_size)
        total_page = math.floor(len(self.__dataset) / page_size)
        return {
                "page_size": len(pages),
                "page": page,
                "data": pages[:],
                "next_page": None if page + 1 > total_page else page + 1,
                "prev_page": None if page - 1 == 0 else page - 1,
                "total_pages": total_page
               }
