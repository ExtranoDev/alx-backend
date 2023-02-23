#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page, page_size):
    """Funtion returns a tuple of size two
       containing a start index and an end index
       Returns: start_idx and end_idx
       args:
            page(int): page index
            page_size(int): page size
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx * page_size
    return start_idx, end_idx
