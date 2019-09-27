from datetime import datetime, timedelta

# Use these variables if required in key
now = datetime.utcnow()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
get_last_hour = datetime.now() - timedelta(hours = 1)
last_hour = (get_last_hour.strftime('%H'))

# Add your bucket and key here
bucket = ''
key = f'/secure/{year}/{month}/{day}/{last_hour}'