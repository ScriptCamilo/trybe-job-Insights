from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs_array = []

    with open(path) as file:
        jobs_list = csv.DictReader(file)
        for job in jobs_list:
            jobs_array.append(job)

    return jobs_array
