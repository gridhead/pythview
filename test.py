#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Test for interview

def remove_duplicates(input: list) -> list:
    """
    This function removes any duplicates from list.

    Test 1) Fix this function and remove any error you find.

    Params:
        input: List to remove duplicates from

    Returns:
        List without duplicates.
    """
    no_dup_list = []
    for indx in input:
        if indx not in no_dup_list:
            no_dup_list.append(indx)
    return no_dup_list


def sort_list(input: list) -> list:
    """
    This function sorts the input list.

    Test 2) Write this function to work as expected.

    Params:
        input: List to sort

    Returns:
        Sorted list.
    """
    input.sort()
    return input


if __name__ == "__main__":
    # Main of the python test
    unsorted_list = [1, 2, 2, 5, 1, 3, 20, 15]

    # Test 1: Remove duplicates
    no_dup_list = remove_duplicates(unsorted_list)

    # Assert that output is correct
    assert no_dup_list == [1, 2, 5, 3, 20, 15]

    # Test 2: Sort list
    sorted_list = sort_list(no_dup_list)

    # Assert that output is sorted
    assert sorted_list == [1, 2, 3, 5, 15, 20]
