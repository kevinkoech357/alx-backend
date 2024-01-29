#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get hypermedia information for a specific index in the dataset.

        Returns:
            dict: Hypermedia information containing index details.
        """
        dataset = self.dataset()

        # Validate that index is in a valid range
        assert index is None or (isinstance(index, int) and 0 <= index < len(dataset))

        # Set the default index if not provided
        index = 0 if index is None else index

        # Calculate the end index for the current page
        end_index = min(index + page_size, len(dataset))

        # Get the data for the current page
        page_data = dataset[index:end_index]

        # Calculate the next index to query with
        next_index = end_index

        hyper_data = {
            "index": index,
            "next_index": next_index,
            "page_size": len(page_data),
            "data": page_data,
        }

        return hyper_data
