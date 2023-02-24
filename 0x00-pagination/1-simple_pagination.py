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
