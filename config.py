from datetime import datetime, timedelta

# Use these variables if required in key
now = datetime.utcnow()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
get_last_hour = datetime.now() - timedelta(hours = 1)
last_hour = (get_last_hour.strftime('%H'))
allowed_ip_range = ''
allowed_ip_range_2 = ''

# Add your bucket and key here
bucket = ''
key = ''