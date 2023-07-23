#!/usr/bin/env python3
"""
This function takes two interger arguments and returns a tuple
"""


def index_range(page, page_size):
    """
    Function returns a tuple with a starting index and end index

    Args:
        page (int): The page number (1-indexed)
        page_size: The number of items per page

    Returns:
        tuple: A tuple with a start and end index (both inclusive)
    """
    if page <= 0 or page_size <= 0:
        raise ValueError()
    begin_index = (page - 1) * page_size
    stop_index = begin_index + page_size
    range = (begin_index, stop_index)

    return range


if __name__ == "__main__":
    index_range(page, page_size)
