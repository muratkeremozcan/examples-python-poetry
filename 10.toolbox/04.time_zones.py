# 1. Create timezone-aware datetimes using timezone(timedelta(hours=X))
# 2. Convert between timezones with astimezone() (preferred)
# 3. Use replace(tzinfo=) carefully - doesn't convert time
# 4. Use dateutil to get timezone objects (preferred)

from datetime import datetime, timedelta, timezone

# US central time zone
CT = timezone(timedelta(hours=-6))
dt = datetime(2022, 1, 1, 15, 23, 25, tzinfo=CT)
print('timezone-aware datetime CT:', dt, dt.isoformat())

# Turkish time zone
TR = timezone(timedelta(hours=2))
dt_tr = datetime(2022, 1, 1, 15, 23, 25, tzinfo=TR)
print('timezone-aware datetime TR:', dt_tr, dt_tr.isoformat())


# Adjusting timezone vs changing tzinfo
print('adjust timezone TR to UTC:',dt_tr.astimezone(timezone.utc))
# change tzinfo
print('change tzinfo TR to UTC:',dt_tr.replace(tzinfo=timezone.utc))



######
onebike_datetimes = [{'start': datetime(2017, 10, 1, 15, 23, 25), 'end': datetime(2017, 10, 1, 15, 26, 26)}, {'start': datetime(2017, 10, 1, 15, 42, 57), 'end': datetime(2017, 10, 1, 17, 49, 59)}, {'start': datetime(2017, 10, 2, 6, 37, 10), 'end': datetime(2017, 10, 2, 6, 42, 53)}, {'start': datetime(2017, 10, 2, 8, 56, 45), 'end': datetime(2017, 10, 2, 9, 18, 3)}, {'start': datetime(2017, 10, 2, 18, 23, 48), 'end': datetime(2017, 10, 2, 18, 45, 5)}, {'start': datetime(2017, 10, 2, 18, 48, 8), 'end': datetime(2017, 10, 2, 19, 10, 54)}, {'start': datetime(2017, 10, 2, 19, 18, 10), 'end': datetime(2017, 10, 2, 19, 31, 45)}, {'start': datetime(2017, 10, 2, 19, 37, 32), 'end': datetime(2017, 10, 2, 19, 46, 37)}]

# convert to datetimes to another timezone
edt = timezone(timedelta(hours=-4))

for trip in onebike_datetimes[:3]:
	trip['start'] = trip['start'].replace(tzinfo=edt)
	trip['end'] = trip['end'].replace(tzinfo=edt)

print(onebike_datetimes[:3])


for trip in onebike_datetimes[:3]:
	dt = trip['start']
	# move dt to be in UTC
	dt = dt.astimezone(timezone.utc)
	
# Print the start time in UTC
print('Original:', trip['start'], '| UTC:', dt.isoformat())
print('\n')

######

from dateutil import tz

et = tz.gettz('US/Eastern')
ct = tz.gettz('US/Central')
tr = tz.gettz('Turkey')

# The actual timezone data is used when you apply these timezone objects to datetime objects using methods like astimezone() or replace(tzinfo=...)
# print(et)
# print(ct)
# print(tr)

for trip in onebike_datetimes[:3]:
	trip['start'] = trip['start'].replace(tzinfo=et)
	trip['end'] = trip['end'].replace(tzinfo=et)

print(onebike_datetimes[:3])

#######
uk = tz.gettz('Europe/London')

local = onebike_datetimes[0]['start']
notlocal = local.astimezone(uk)

print(local.isoformat())
print(notlocal.isoformat())