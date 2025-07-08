# pandas can read CSV and parse date columns into datetime objects: parse_dates=['column_name']
# dt accessor provides datetime properties/methods

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