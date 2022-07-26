from src import jobs


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    list_jobs = jobs.read(path)
    set_job_types = set()
    for item in list_jobs:
        if item["job_type"]:
            set_job_types.add(item["job_type"])

    return set_job_types


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

    list_jobs_by_job_types = []
    for item in jobs:
        if item["job_type"] == job_type:
            list_jobs_by_job_types.append(item)

    return list_jobs_by_job_types


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """

    list_jobs = jobs.read(path)
    # list comprehension
    list_industries = [
        item["industry"] for item in list_jobs if item["industry"]]
    set_industries = set(list_industries)

    return set_industries


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

    list_jobs_by_industries = []
    for item in jobs:
        if item["industry"] == industry:
            list_jobs_by_industries.append(item)

    return list_jobs_by_industries


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    list_jobs = jobs.read(path)
    list_max_salary = []
    for item in list_jobs:
        if item["max_salary"] and item["max_salary"] != "invalid":
            list_max_salary.append(int(item["max_salary"]))
    # https://docs.python.org/pt-br/3/library/functions.html#max
    return max(list_max_salary)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    list_jobs = jobs.read(path)
    list_min_salary = []
    for item in list_jobs:
        if item["min_salary"] and item["min_salary"] != "invalid":
            list_min_salary.append(int(item["min_salary"]))

    return min(list_min_salary)


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
    # https://www.delftstack.com/pt/howto/python/python-check-if-character-is-number/#:~:text=Produ%C3%A7%C3%A3o%3A%20Copy%20True-,Use%20a%20fun%C3%A7%C3%A3o%20isnumeric()%20para%20verificar%20se%20um%20determinado,uma%20determinada%20string%20forem%20n%C3%BAmeros.

    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError(" 'min_salary' or 'max_salary' doesn't exists")

    if (
            not str(job["max_salary"]).isnumeric()
            or not str(job["min_salary"]).isnumeric()):
        raise ValueError(" 'min_salary' or 'max_salary' aren't valid integers")

    if job["min_salary"] > job["max_salary"]:
        raise ValueError(" 'min_salary' is greather than 'max_salary' ")

    if type(salary) != int:
        raise ValueError(" 'salary' isn't a valid integer ")

    # https://pt.stackoverflow.com/questions/161505/em-python-existe-opera%C3%A7%C3%A3o-tern%C3%A1ria
    return (True if
            salary >= job["min_salary"] and salary <= job["max_salary"]
            else False)


def validation_salary_range(job, salary):

    if "max_salary" not in job or "min_salary" not in job:
        return False

    if (
            not str(job["max_salary"]).isnumeric()
            or not str(job["min_salary"]).isnumeric()):
        return False

    if job["min_salary"] > job["max_salary"]:
        return False

    if type(salary) != int:
        return False

    return (True if
            salary >= job["min_salary"] and salary <= job["max_salary"]
            else False)


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
    list_jobs = []
    for item in jobs:
        range = {
                    "min_salary": item["min_salary"],
                    "max_salary": item["max_salary"]
                }
        result = validation_salary_range(range, salary)
        if result:
            list_jobs.append(item)

    return list_jobs
