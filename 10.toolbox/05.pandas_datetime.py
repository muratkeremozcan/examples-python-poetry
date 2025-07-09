# Key Pandas Datetime and Time Series Operations
#
# 1. Reading and Parsing Dates:
#    - Read CSV with datetime parsing: pd.read_csv(parse_dates=['column_name'])
#    - Access datetime properties/methods with .dt accessor (ex: ride_durations.dt.total_seconds())
#
# 2. Time Delta Operations:
#    - Calculate time differences between datetime columns
#    - Convert timedelta to seconds: .dt.total_seconds()
#
# 3. Boolean Masking and Filtering:
#    - Create boolean masks for filtering: df['col1'] == df['col2'] (ex: joyrides = rides['Start station'] == rides['End station'])
#    - Filter data using boolean masks: df[mask] (ex: joyrides = rides[joyrides])
#    - Use .sum() on boolean masks to count True values 
#
# 4. Statistical Analysis:
#    - Use median() for duration analysis (less affected by outliers than mean)
#
# 5. Time Series Resampling:
#    - Resample time series data: df.resample('D', on='date_column')
#    - Common frequency strings: 'D' (daily), 'M' (monthly), 'H' (hourly), 'W' (weekly)
#    - Get counts per period: .size()
#    - Plot time series data directly: .plot()
#
# 6. Grouping by Time and Categories:
#    - Group by member type and resample: df.groupby('Member type').resample('M', on='date_column')
#    - Calculate value counts ratios: .value_counts() / .size()
#
# 7. Visualization:
#    - Set y-axis limits: .plot(ylim=[min, max])
#    - Display plots: plt.show()


import pandas as pd
import os

# read file from anywhere
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "capital-onebike.csv")

# Read CSV and parse date columns into datetime objects
rides = pd.read_csv(csv_path, parse_dates=['Start date', 'End date'])
print(rides.iloc[0])

# Calculate time differences between end and start dates
# This creates a timedelta64[ns] Series
ride_durations = rides['End date'] - rides['Start date']

# Convert timedelta to total seconds for easier analysis
# dt accessor provides datetime properties/methods
rides['Duration'] = ride_durations.dt.total_seconds()
print(rides['Duration'].head())


###########
# Boolean mask to identify joyrides (start and end at same station)
# This creates a Series of True/False values where True indicates a joyride
joyrides = rides['Start station'] == rides['End station']
print("{} rides were joyrides".format(joyrides.sum()))

# Median is used instead of mean because it's less affected by outliers
print("Median ride duration: {} seconds".format(rides['Duration'].median()))

# Filter the DataFrame using the boolean mask and calculate median duration
# This is an example of boolean indexing in pandas
print("Median joyride duration: {} seconds".format(
    rides[joyrides]['Duration'].median()
))

import matplotlib.pyplot as plt

# resample('D') is a frequency string that tells pandas to group the data into daily bucket

# Your CSV has timestamps in the 'Start date' column like:
# 2017-10-01 15:23:25
# 2017-10-01 15:42:57 (same day)
# 2017-10-02 06:37:10 (next day)
# When you do resample('D'), pandas:
# Groups all timestamps by their date (ignoring the time part)
# Creates one group for each unique date
# For example, both 2017-10-01 15:23:25 and 2017-10-01 15:42:57 go into the same daily bucket
# The .size() then counts how many rides occurred in each daily bucket.

# Common frequency strings in pandas:
# 'D' = daily
# 'H' = hourly
# 'W' = weekly
# 'M' = monthly
# '15T' = 15 minutes
# '30S' = 30 seconds

rides.resample('D', on = 'Start date')\
  .size()\
  .plot(ylim = [0, 15]) # line plot with y limit

plt.show()


# resample and just select 'Member type' column from the resampled DataFrame
monthly_rides = rides.resample('M', on = 'Start date')['Member type']

# Take the ratio of the .value_counts() over the total number of rides
print(monthly_rides.value_counts() / monthly_rides.size())

# Group rides by member type, and resample to the month
grouped = rides.groupby('Member type')\
  .resample('M', on = 'Start date')

# Print the median duration for each group
print(grouped['Duration'].median())