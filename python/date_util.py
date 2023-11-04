from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

def format_as_date_time_hour_truncated(dt: datetime) -> str:
    """
    Takes a datetime object and truncates it to the hour.
    
    Args:
    - dt (datetime): The datetime object to be truncated.

    Returns:
    - str: The ISO-formatted string of the truncated datetime.
    """
    
    # Truncate the datetime to the start of the hour
    dt_truncated = dt.replace(minute=0, second=0, microsecond=0)
    
    # Return the ISO-formatted string
    return dt_truncated.isoformat().replace("+00:00", "Z")


def get_files_date_patterns(dt: datetime, days_before: int) -> list:
    """
    Generate a list of date strings starting from the given date and counting backward for a specified number of days.

    Args:
    - dt (datetime): The starting datetime object.
    - days_before (int): The number of days to count backward from the starting date.

    Returns:
    - list: A list of date strings in "YYYY-MM-DD" format.
    """
    files_date_patterns = []
    
    while days_before >= 0:
        date_only_str = dt.strftime('%Y-%m-%d')
        files_date_patterns.append(date_only_str)
        dt -= timedelta(days=1)
        days_before -= 1
    
    return files_date_patterns




def get_files_date_time_patterns(dt: datetime, days_before: int) -> list:
    """
    Generate a list of date-time strings starting from the given date-time and counting backward for a specified number of days.

    Args:
    - dt (datetime): The starting datetime object.
    - days_before (int): The number of days to count backward from the starting date-time.

    Returns:
    - list: A list of date-time strings in "YYYY-MM-DD_HH00" format.
    """
    files_date_patterns = []
    
    while days_before >= 0:
        datetime_str_for_file = format_as_date_time_for_file(dt)
        files_date_patterns.append(datetime_str_for_file)
        dt -= timedelta(days=1)
        days_before -= 1
    
    return files_date_patterns

def format_as_date_time_for_file(dt: datetime) -> str:
    """
    Format a datetime object to a string in "YYYY-MM-DD_HH00" format.

    Args:
    - dt (datetime): The datetime object to format.

    Returns:
    - str: A string in "YYYY-MM-DD_HH00" format.
    """
    formatted_date = dt.strftime('%Y-%m-%d')
    formatted_hour = dt.strftime('%H')
    return f"{formatted_date}_{formatted_hour}00"

def set_local_datetime(utc_datetime: str, time_zone_str):
    """
    Returns the local time of the UTC time and timezone provided.
    """
    utc_datetime = datetime.fromisoformat(utc_datetime.replace("Z", "+00:00"))
    # Load the time zone
    local_zone = ZoneInfo(time_zone_str)
    
    # Convert the UTC datetime to local datetime
    local_datetime = utc_datetime.astimezone(local_zone)

    local_datetime_str = local_datetime.strftime('%Y-%m-%dT%H:%M')

    return local_datetime_str


def get_utc_datetime_of_instant(instant_datetime_str: str):
    # Parse the UTC datetime string into a datetime object
    return datetime.fromisoformat(instant_datetime_str.replace("Z", "+00:00"))

def get_next_datetime(datetime_obj, aggregation):
    if aggregation == "HOURLY":
        return datetime_obj + timedelta(hours=1)
    elif aggregation == "DAILY":
        return datetime_obj + timedelta(days=1)
    elif aggregation == "WEEKLY":
        return datetime_obj + timedelta(weeks=1)
    elif aggregation == "MONTHLY":
        return datetime_obj + timedelta(days=30)
    elif aggregation == "YEARLY":
        return datetime_obj + timedelta(days=365)
    else:
        raise ValueError(f"{aggregation} is not implemented for get_next_datetime.")

def get_next_instant_datetime(instant_datetime_str, aggregation):
    datetime_obj = get_utc_datetime_of_instant(instant_datetime_str)
    next_datetime_obj = get_next_datetime(datetime_obj, aggregation)
    return next_datetime_obj.isoformat().replace("+00:00", "Z")

def format_as_uid(dt: datetime) -> str:
    truncated_datetime = dt.replace(minute=0, second=0, microsecond=0)
    # Format the datetime as "yyyyMMddHHmmss"
    return truncated_datetime.strftime('%Y%m%d%H%M%S')


def utc_string_to_uid_format(utc_string: str) -> str:
    # Parse the string into a datetime object
    dt = datetime.strptime(utc_string, '%Y-%m-%dT%H:%M:%SZ')
    return format_as_uid(dt)

def local_date_time_of_utc(utc_datetime, timezone_str):
    timezone = ZoneInfo(timezone_str)
    return utc_datetime.astimezone(timezone)

set_local_datetime("2023-11-03T19:00:00Z", "America/Los_Angeles")

job_date_time = datetime.now(timezone.utc)
job0_hour_date_time = format_as_date_time_hour_truncated(job_date_time)