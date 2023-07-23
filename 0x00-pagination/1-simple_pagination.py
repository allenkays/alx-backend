#!/usr/bin/env python3
"""
This module deals with RESTFUL API pagination
"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Function returns a tuple with a starting index and end index

    Args:
        page (int): The page number (1-indexed)
        page_size: The number of items per page

    Returns:
        tuple: A tuple with a start and end index (both inclusive)
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positve intergers.")
    begin_index = (page - 1) * page_size
    stop_index = begin_index + page_size
    range = (begin_index, stop_index)

    return range


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a specific page of the dataset based on the given
        pagination parameters.

        Args:
            page (int, optional): The page number (1-indexed).
            Defaults to 1.
            page_size (int, optional): The number of items per page.
            Defaults to 10.

        Returns:
            List[List]: A list of the rows (data) for the requested page.
        """
        assert isinstance(page, int) and page > 0, (
                "Page must be a positive interger."
                )
        assert isinstance(page_size, int) and page_size > 0, (
                "Page_size must be a positive interger"
                )
        dataset = self.dataset()
        start_idx, end_idx = index_range(page, page_size)

        # Return an empty list if the requested page is out of range
        if start_idx >= len(dataset):
            return []

        return dataset[start_idx:end_idx + 1]
