#!/usr/bin/env python3
"""Write a function named index_range that takes two integer arguments page
and page_size"""
import csv


def index_range(page, page_size):
    """return in a list for those particular pagination parameters"""
    return ((page - 1) * page_size, page * page_size)
