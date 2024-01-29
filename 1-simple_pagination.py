#!/usr/bin/env python3


"""
Define a function that returns a tuple
based on the given pagination parameters
"""


import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of start index and end index
    for the given pagination parameters.

    Returns:
        tuple: Start index and end index for the specified page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a specific page of the dataset based on pagination parameters.

        Returns:
            List[List]: Page of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        # Return an empty list if the indexes are out of range
        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
