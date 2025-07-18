# Use `date.weekday()` to get day of week (0=Monday, 6=Sunday)
# Access date components with `.year`, `.month`, `.day` attributes
# Date objects support arithmetic (e.g., `end - start` gives timedelta)
# Sort dates naturally with `sorted()` for chronological order
# Negative indices access list from the end (`-1` is last item)
# We can represent the date as a string in different formats using strftime(%m, %B, %d, %j, %y, %Y) (%B for month name, %j for day of the year, %y last 2 digits of year) and isoformat()

from datetime import date

hurricane_andrew = date(1992, 8, 22)
print(hurricane_andrew.weekday())

######

florida_hurricane_dates = [date(1950, 8, 31), date(1950, 9, 5), date(1950, 10, 18), date(1950, 10, 21), date(1951, 5, 18), date(1951, 10, 2), date(1952, 2, 3), date(1952, 8, 30), date(1953, 6, 6), date(1953, 8, 29), date(1953, 9, 20), date(1953, 9, 26), date(1953, 10, 9), date(1955, 8, 21), date(1956, 7, 6), date(1956, 9, 24), date(1956, 10, 15), date(1957, 6, 8), date(1957, 9, 8), date(1958, 9, 4), date(1959, 6, 18), date(1959, 10, 8), date(1959, 10, 18), date(1960, 7, 29), date(1960, 9, 10), date(1960, 9, 15), date(1960, 9, 23), date(1961, 9, 11), date(1961, 10, 29), date(1962, 8, 26), date(1963, 10, 21), date(1964, 6, 6), date(1964, 8, 27), date(1964, 9, 10), date(1964, 9, 20), date(1964, 10, 5), date(1964, 10, 14), date(1965, 6, 15), date(1965, 9, 8), date(1965, 9, 30), date(1966, 6, 9), date(1966, 6, 30), date(1966, 7, 24), date(1966, 10, 4), date(1968, 6, 4), date(1968, 6, 18), date(1968, 7, 5), date(1968, 8, 10), date(1968, 8, 28), date(1968, 9, 26), date(1968, 10, 19), date(1969, 6, 9), date(1969, 8, 18), date(1969, 8, 29), date(1969, 9, 7), date(1969, 9, 21), date(1969, 10, 1), date(1969, 10, 2), date(1969, 10, 21), date(1970, 5, 25), date(1970, 7, 22), date(1970, 8, 6), date(1970, 9, 13), date(1970, 9, 27), date(1971, 8, 10), date(1971, 8, 13), date(1971, 8, 29), date(1971, 9, 1), date(1971, 9, 16), date(1971, 10, 13), date(1972, 5, 28), date(1972, 6, 19), date(1972, 9, 5), date(1973, 6, 7), date(1973, 6, 23), date(1973, 9, 3), date(1973, 9, 25), date(1974, 6, 25), date(1974, 9, 8), date(1974, 9, 27), date(1974, 10, 7), date(1975, 6, 27), date(1975, 7, 29), date(1975, 9, 23), date(1975, 10, 1), date(1975, 10, 16), date(1976, 5, 23), date(1976, 6, 11), date(1976, 8, 19), date(1976, 9, 13), date(1977, 8, 27), date(1977, 9, 5), date(1978, 6, 22), date(1979, 7, 11), date(1979, 9, 3), date(1979, 9, 12), date(1979, 9, 24), date(1980, 8, 7), date(1980, 11, 18), date(1981, 8, 17), date(1982, 6, 18), date(1982, 9, 11), date(1983, 8, 28), date(1984, 9, 9), date(1984, 9, 27), date(1984, 10, 26), date(1985, 7, 23), date(1985, 8, 15), date(1985, 10, 10), date(1985, 11, 21), date(1986, 6, 26), date(1986, 8, 13), date(1987, 8, 14), date(1987, 9, 7), date(1987, 10, 12), date(1987, 11, 4), date(1988, 5, 30), date(1988, 8, 4), date(1988, 8, 13), date(1988, 8, 23), date(1988, 9, 4), date(1988, 9, 10), date(1988, 9, 13), date(1988, 11, 23), date(1989, 9, 22), date(1990, 5, 25), date(1990, 10, 9), date(1990, 10, 12), date(1991, 6, 30), date(1991, 10, 16), date(1992, 6, 25), date(1992, 8, 24), date(1992, 9, 29), date(1993, 6, 1), date(1994, 7, 3), date(1994, 8, 15), date(1994, 10, 2), date(1994, 11, 16), date(1995, 6, 5), date(1995, 7, 27), date(1995, 8, 2), date(1995, 8, 23), date(1995, 10, 4), date(1996, 7, 11), date(1996, 9, 2), date(1996, 10, 8), date(1996, 10, 18), date(1997, 7, 19), date(1998, 9, 3), date(1998, 9, 20), date(1998, 9, 25), date(1998, 11, 5), date(1999, 8, 29), date(1999, 9, 15), date(1999, 9, 21), date(1999, 10, 15), date(2000, 8, 23), date(2000, 9, 9), date(2000, 9, 18), date(2000, 9, 22), date(2000, 10, 3), date(2001, 6, 12), date(2001, 8, 6), date(2001, 9, 14), date(2001, 11, 5), date(2002, 7, 13), date(2002, 8, 4), date(2002, 9, 4), date(2002, 9, 14), date(2002, 9, 26), date(2002, 10, 3), date(2002, 10, 11), date(2003, 4, 20), date(2003, 6, 30), date(2003, 7, 25), date(2003, 8, 14), date(2003, 8, 30), date(2003, 9, 6), date(2003, 9, 13), date(2004, 8, 12), date(2004, 8, 13), date(2004, 9, 5), date(2004, 9, 13), date(2004, 9, 16), date(2004, 10, 10), date(2005, 6, 11), date(2005, 7, 6), date(2005, 7, 10), date(2005, 8, 25), date(2005, 9, 12), date(2005, 9, 20), date(2005, 10, 5), date(2005, 10, 24), date(2006, 6, 13), date(2006, 8, 30), date(2007, 5, 9), date(2007, 6, 2), date(2007, 8, 23), date(2007, 9, 8), date(2007, 9, 13), date(2007, 9, 22), date(2007, 10, 31), date(2007, 12, 13), date(2008, 7, 16), date(2008, 7, 22), date(2008, 8, 18), date(2008, 8, 31), date(2008, 9, 2), date(2009, 8, 16), date(2009, 8, 21), date(2009, 11, 9), date(2010, 6, 30), date(2010, 7, 23), date(2010, 8, 10), date(2010, 8, 31), date(2010, 9, 29), date(2011, 7, 18), date(2011, 8, 25), date(2011, 9, 3), date(2011, 10, 28), date(2011, 11, 9), date(2012, 5, 28), date(2012, 6, 23), date(2012, 8, 25), date(2012, 10, 25), date(2015, 8, 30), date(2015, 10, 1), date(2016, 6, 6), date(2016, 9, 1), date(2016, 9, 14), date(2016, 10, 7), date(2017, 6, 21), date(2017, 7, 31), date(2017, 9, 10), date(2017, 10, 29)]

early_hurricanes = 0

for hurricane in florida_hurricane_dates:
	# check if hurricane is before June
	if hurricane.month < 6:
		early_hurricanes += 1

print('Number of hurricanes before June:', early_hurricanes)

######

hurricanes_each_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6:0, 7: 0, 8:0, 9:0, 10:0, 11:0, 12:0}

for hurricane in florida_hurricane_dates:
	month = hurricane.month
	hurricanes_each_month[month] += 1

print(hurricanes_each_month)

######

start = date(2007, 5, 9)

end = date(2007, 12, 13)

print((end - start).days)

######

dates_scrambled = [date(1988, 8, 4), date(1990, 10, 12), date(2003, 4, 20), date(1971, 9, 1), date(1988, 8, 23), date(1994, 8, 15), date(2002, 8, 4), date(1988, 5, 30), date(2003, 9, 13), date(2009, 8, 21), date(1978, 6, 22), date(1969, 6, 9), date(1976, 6, 11), date(1976, 8, 19), date(1966, 6, 9), date(1968, 7, 5), date(1987, 11, 4), date(1988, 8, 13), date(2007, 12, 13), date(1994, 11, 16), date(2003, 9, 6), date(1971, 8, 13), date(1981, 8, 17), date(1998, 9, 25), date(1968, 9, 26), date(1968, 6, 4), date(1998, 11, 5), date(2008, 8, 18), date(1987, 8, 14), date(1988, 11, 23), date(2010, 9, 29), date(1985, 7, 23), date(2017, 7, 31), date(1955, 8, 21), date(1986, 6, 26), date(1963, 10, 21), date(2011, 10, 28), date(2011, 11, 9), date(1997, 7, 19), date(2007, 6, 2), date(2002, 9, 14), date(1992, 9, 29), date(1971, 10, 13), date(1962, 8, 26), date(1964, 8, 27), date(1984, 9, 27), date(1973, 9, 25), date(1969, 10, 21), date(1994, 7, 3), date(1958, 9, 4), date(1985, 11, 21), date(2011, 9, 3), date(1972, 6, 19), date(1991, 6, 30), date(2004, 8, 12), date(2007, 9, 8), date(1952, 2, 3), date(1965, 9, 30), date(2000, 9, 22), date(2002, 9, 26), date(1950, 9, 5), date(1966, 10, 4), date(1970, 5, 25), date(1979, 9, 24), date(1960, 9, 23), date(2007, 8, 23), date(2009, 8, 16), date(1996, 10, 18), date(2012, 10, 25), date(2011, 8, 25), date(1951, 5, 18), date(1980, 8, 7), date(1979, 9, 3), date(1953, 9, 26), date(1968, 10, 19), date(2009, 11, 9), date(1999, 8, 29), date(2015, 10, 1), date(2008, 9, 2), date(2004, 10, 10), date(2004, 9, 16), date(1992, 8, 24), date(2000, 9, 9), date(1971, 9, 16), date(1996, 9, 2), date(1998, 9, 3), date(1951, 10, 2), date(1979, 9, 12), date(2007, 10, 31), date(1953, 10, 9), date(1952, 8, 30), date(1969, 9, 7), date(2015, 8, 30), date(1959, 10, 8), date(2002, 7, 13), date(1961, 10, 29), date(2007, 5, 9), date(2016, 10, 7), date(1964, 9, 20), date(1979, 7, 11), date(1950, 10, 18), date(2008, 8, 31), date(2012, 8, 25), date(1966, 7, 24), date(2010, 8, 10), date(2005, 8, 25), date(2003, 6, 30), date(1956, 7, 6), date(1974, 9, 8), date(1966, 6, 30), date(2016, 9, 14), date(1968, 6, 18), date(1982, 9, 11), date(1976, 9, 13), date(1975, 7, 29), date(2007, 9, 13), date(1970, 9, 27), date(1969, 10, 2), date(2010, 8, 31), date(1995, 10, 4), date(1969, 8, 29), date(1984, 10, 26), date(1973, 9, 3), date(1976, 5, 23), date(2001, 11, 5), date(2010, 6, 30), date(1985, 10, 10), date(1970, 7, 22), date(1972, 5, 28), date(1982, 6, 18), date(2001, 8, 6), date(1953, 8, 29), date(1965, 9, 8), date(1964, 9, 10), date(1959, 10, 18), date(1957, 6, 8), date(1988, 9, 10), date(2005, 6, 11), date(1953, 6, 6), date(2003, 8, 30), date(2002, 10, 3), date(1968, 8, 10), date(1999, 10, 15), date(2002, 9, 4), date(2001, 6, 12), date(2017, 9, 10), date(2005, 10, 5), date(2005, 7, 10), date(1973, 6, 7), date(1999, 9, 15), date(2005, 9, 20), date(1995, 6, 5), date(2003, 7, 25), date(2004, 9, 13), date(1964, 6, 6), date(1973, 6, 23), date(2005, 9, 12), date(2012, 6, 23), date(1961, 9, 11), date(1990, 5, 25), date(2017, 6, 21), date(1975, 6, 27), date(1959, 6, 18), date(2004, 9, 5), date(1987, 10, 12), date(1995, 7, 27), date(1964, 10, 14), date(1970, 8, 6), date(1969, 10, 1), date(1996, 10, 8), date(1968, 8, 28), date(1956, 10, 15), date(1975, 9, 23), date(1970, 9, 13), date(1975, 10, 16), date(1990, 10, 9), date(2005, 10, 24), date(1950, 8, 31), date(2000, 10, 3), date(2002, 10, 11), date(1983, 8, 28), date(1960, 7, 29), date(1950, 10, 21), date(1995, 8, 2), date(1956, 9, 24), date(2016, 9, 1), date(1993, 6, 1), date(1987, 9, 7), date(2012, 5, 28), date(1995, 8, 23), date(1969, 8, 18), date(2001, 9, 14), date(2000, 8, 23), date(1974, 10, 7), date(1986, 8, 13), date(1977, 8, 27), date(2008, 7, 16), date(1996, 7, 11), date(1988, 9, 4), date(1975, 10, 1), date(2003, 8, 14), date(1957, 9, 8), date(2005, 7, 6), date(1960, 9, 15), date(1974, 9, 27), date(1965, 6, 15), date(1999, 9, 21), date(2004, 8, 13), date(1994, 10, 2), date(1971, 8, 10), date(2008, 7, 22), date(2000, 9, 18), date(1960, 9, 10), date(2006, 6, 13), date(2017, 10, 29), date(1972, 9, 5), date(1964, 10, 5), date(1991, 10, 16), date(1969, 9, 21), date(1998, 9, 20), date(1977, 9, 5), date(1988, 9, 13), date(1974, 6, 25), date(2010, 7, 23), date(2007, 9, 22), date(1984, 9, 9), date(1989, 9, 22), date(1992, 6, 25), date(1971, 8, 29), date(1953, 9, 20), date(1985, 8, 15), date(2016, 6, 6), date(2006, 8, 30), date(1980, 11, 18), date(2011, 7, 18)]
# print the first and last dates
print(dates_scrambled[0])
print(dates_scrambled[0 - 1])

dates_ordered = sorted(dates_scrambled)
print(dates_ordered[0])
print(dates_ordered[-1])

###########
# date to string
# Assign the earliest date in florida_hurricane_dates to first_date

first_date = sorted(florida_hurricane_dates)[0]

iso = 'Our earliest hurricane date: ' + first_date.isoformat()
us = 'Our earliest hurricane date: ' + first_date.strftime("%m/%d/%Y")

print(iso)
print(us)

###

andrew = date(1992, 8, 26)
# Print the date in the format 'YYYY-MM'
print(andrew.strftime('%Y-%m'))
# Print the date in the format 'MONTH (YYYY)'
print(andrew.strftime('%m (%Y)'))
print(andrew.strftime('%B (%Y)'))
# Print the date in the format 'YYYY-DDD'
print(andrew.strftime('%y-%j'))
print(andrew.strftime('%Y-%j'))