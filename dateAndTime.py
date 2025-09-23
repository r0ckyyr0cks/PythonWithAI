import datetime
import pytz


def get_current_datetime():
    """Returns the current date and time as a formatted string."""
    now = datetime.datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")


print(f"Local Timezone - {get_current_datetime()}")

tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.datetime.now(tz_NY)
print(f"New York Timezone - {datetime_NY.strftime('%d-%m-%Y %H:%M:%S')}")

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.datetime.now(tz_London)
print(f"London Timezone - {datetime_London.strftime('%d-%m-%Y %H:%M:%S')}")


print("^ " * 20)


def get_datetime_in_timezone(timezone_str):
    """Returns the current date and time in the specified timezone."""
    tz = pytz.timezone(timezone_str)
    datetime_tz = datetime.datetime.now(tz)
    return datetime_tz.strftime("%d-%m-%Y %H:%M:%S")


print(f"Tokyo Timezone - {get_datetime_in_timezone('Asia/Tokyo')}")
print(f"Texas Timezone - {get_datetime_in_timezone('America/Chicago')}")

