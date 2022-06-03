from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
# https://www.programiz.com/python-programming/reading-csv-files

    jobs_list = []
    with open(path, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            jobs_list.append(dict(row))
    return jobs_list
