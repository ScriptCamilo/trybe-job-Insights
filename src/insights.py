from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    jobs_types = []
    for job in jobs_list:
        if job["job_type"] != "" and job["job_type"] not in jobs_types:
            jobs_types.append(job["job_type"])
    return jobs_types


def filter_by_job_type(jobs, job_type):
    filtered_list = [
        job for job in jobs if job["job_type"] == job_type
    ]
    return filtered_list


def get_unique_industries(path):
    jobs_list = read(path)
    jobs_industry = []
    for job in jobs_list:
        if job["industry"] != "" and job["industry"] not in jobs_industry:
            jobs_industry.append(job["industry"])
    return jobs_industry


def filter_by_industry(jobs, industry):
    filtered_list = [
        job for job in jobs if job["industry"] == industry
    ]
    return filtered_list


def get_max_salary(path):
    jobs_list = read(path)
    max_salary = 0
    for job in jobs_list:
        is_salary_not_invalid = job["max_salary"] != "invalid"
        is_salary_not_empty = job["max_salary"] != ""

        if is_salary_not_invalid and is_salary_not_empty:
            is_salary_greater = float(job["max_salary"]) > max_salary

            if is_salary_greater:
                max_salary = int(job["max_salary"])
    return max_salary


def get_min_salary(path):
    jobs_list = read(path)
    min_salary = None
    for job in jobs_list:
        is_salary_not_invalid = job["min_salary"] != "invalid"
        is_salary_not_empty = job["min_salary"] != ""

        if is_salary_not_invalid and is_salary_not_empty:
            if min_salary is None:
                min_salary = float(job["min_salary"])
                continue

            is_salary_smaller = float(job["min_salary"]) < min_salary
            if is_salary_smaller:
                min_salary = int(job["min_salary"])
    return min_salary


def is_integers_valid(values):
    for num in values:
        if not isinstance(num, int):
            raise(ValueError)


def is_keys_valid(expected_keys, keys):
    for key in expected_keys:
        if key not in keys:
            raise(ValueError)


def matches_salary_range(job, salary):
    expected_keys = ["min_salary", "max_salary"]
    is_keys_valid(expected_keys, keys=job.keys())

    min_salary = job["min_salary"]
    max_salary = job["max_salary"]

    is_integers_valid([min_salary, max_salary, salary])

    if min_salary > max_salary:
        raise(ValueError)

    if min_salary <= salary <= max_salary:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
