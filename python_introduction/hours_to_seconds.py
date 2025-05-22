# Define the number of hours to convert
hours = 2

# Calculate the number of seconds
# There are 60 minutes in an hour, and 60 seconds in a minute,
# so 60 * 60 = 3600 seconds in an hour.
seconds = hours * 3600

# Display the result in the requested format
# Note: The "hour(s)" handles singular/plural, but for 2 hours, it will be "hours".
print(f"{hours} hour(s) is {seconds} seconds.")