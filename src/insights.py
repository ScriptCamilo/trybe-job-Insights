from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    jobs_types = []
    for job in jobs_list:
        if job["job_type"] != "" and job["job_type"] not in jobs_types:
            jobs_types.append(job["job_type"])
    return jobs_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


def get_unique_industries(path):
    jobs_list = read(path)
    jobs_industry = []
    for job in jobs_list:
        if job["industry"] != "" and job["industry"] not in jobs_industry:
            jobs_industry.append(job["industry"])
    return jobs_industry


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


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


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


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
