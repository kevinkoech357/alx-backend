#!/usr/bin/env python3


"""
Define a function that returns a tuple
based on the given pagination parameters
"""


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
