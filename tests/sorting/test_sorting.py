import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "min_salary": "1800",
            "max_salary": "3000",
            "date_posted": "1979-10-28",
        },
        {
            "min_salary": "4500",
            "max_salary": "6000",
            "date_posted": "1999-02-06",
        },
        {
            "min_salary": "2000",
            "max_salary": "3500",
            "date_posted": "1975-12-19",
        },
        {
            "min_salary": "2500",
            "max_salary": "4500",
            "date_posted": "1997-03-18",
        },
    ]

    by_min_salary = [jobs[0], jobs[2], jobs[3], jobs[1]]
    by_max_salary = [jobs[1], jobs[3], jobs[2], jobs[0]]
    by_date_posted = [jobs[1], jobs[3], jobs[0], jobs[2]]

    sort_by(jobs, 'min_salary')
    assert jobs == by_min_salary

    sort_by(jobs, 'max_salary')
    assert jobs == by_max_salary

    sort_by(jobs, 'date_posted')
    assert jobs == by_date_posted

    with pytest.raises(ValueError):
        sort_by(jobs, "max")
