import time
from datetime import datetime, timedelta

# Get the current time in seconds since the epoch
current_time_seconds = time.time()
print("Current time in seconds since the epoch:", current_time_seconds)

# Convert seconds since the epoch to a structured time tuple
structured_time = time.gmtime(current_time_seconds)
print("Structured time tuple:", structured_time)

# Format the structured time tuple into a string
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", structured_time)
print("Formatted time:", formatted_time)

# Sleep for 5 seconds
print("Sleeping for 3 seconds...")
time.sleep(3)
print("Woke up!")

# Get the current local time
local_time = time.localtime()
print("Current local time:", local_time)

# Working with datetime objects
current_datetime = datetime.now()
print("Current datetime:", current_datetime)

# Adding 3 days to the current datetime
new_datetime = current_datetime + timedelta(days=3)
print("Datetime after adding 3 days:", new_datetime)

# Formatting datetime as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted datetime:", formatted_datetime)

# Parsing a string into a datetime object
parsed_datetime = datetime.strptime("2023-01-15 14:30:00", "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed_datetime)

# Calculating the difference between two datetimes
time_difference = new_datetime - current_datetime
print("Time difference between two datetimes:", time_difference)

# Extracting components from a datetime object
year = current_datetime.year
month = current_datetime.month
day = current_datetime.day
hour = current_datetime.hour
minute = current_datetime.minute
second = current_datetime.second

print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Hour:", hour)
print("Minute:", minute)
print("Second:", second)
