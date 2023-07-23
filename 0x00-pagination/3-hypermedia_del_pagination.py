#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


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
                i: dataset[i - 1] for i in range(1, len(dataset) + 1)
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get a dictionary containing hypermedia pagination information for the dataset based on the given index.

        Args:
            index (int, optional): The start index of the page (1-indexed). Defaults to None.
            page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
            Dict: A dictionary containing hypermedia pagination information.
        """ 
        dataset = self.indexed_dataset()
        total_items = len(dataset)

        if index is None:
            index = 1
        assert 1 <= index <= total_items, "Invalid index range."

        end_index = min(index + page_size, total_items)

        # Check if the requested index is within the available range after deletion
        if index not in dataset:
            index = min(dataset.keys(), key=lambda x: abs(x - index))

        # Check if the requested end_index is within the available range after deletion
        if end_index not in dataset:
            end_index = min(dataset.keys(), key=lambda x: abs(x - end_index))

        data = [dataset[i] for i in range(index, min(end_index + 1, total_items + 1))]

        next_index = end_index + 1 if end_index < total_items else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
