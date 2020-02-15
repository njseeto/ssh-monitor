# ssh-monitor

A small project to download and unzip ssh log files from S3 buckets, reads them and identifies the number of times a specific ip address is attempting to maliciously log into a server.

Decided to write this small application as we had no observability regarding the SSH'ing into instances. This program accesses a S3 bucket unzips the file and looks for a specific phrase, in this case 'possible break in attempt' or 'Invalid user', it then takes out the IP address associated with these phrases and counts them. The output will look something this:

```
{'101.230.236.177': 1, '103.81.51.4': 1}
```

Where the key is the ip address and the value is the number of times the address was associated with the offending phrases.

I set this program to check the logs of the previous hour, as per the `config.py` file. But change it however as per your requirements.

What you need to run this:
- AWS credentials configured on your machine. [This](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html) might be useful.
- Python 3
- Boto 3 
    -   `sudo pip install boto3`

You will need to configure the `config.py` file to suit your needs. Notably the S3 key and buckets, and the allowed ip ranges (add more as required).

To run tests:
- `python3 test_monitor.py`
- Be sure to have `config.py` file configured

To run the program via the command line:
- You will need to change the `monitor.py` file.
- In the following, change both `return` to `print`

```
    for obj in appended_list:
        ip = find_ip(obj)
        if ip is not None:
            ip_list.append(ip)
        results = {value: len(list(frequency)) for value, frequency in groupby(sorted(ip_list))}
        return results
    else:
        return None
```
- run `python3 monitor.py`
- You should see something similar to the below in your terminal:

```
{'101.230.236.177': 1, '103.81.51.4': 1}
```

Next Steps:
- Place this program on AWS Lambda to have it trigger automatically.
- Add a threshold/criteria for mnumber of attempts from a specific IP address. Eg: More than 10 attempts from one IP address.
- Add Slack integration, ie: send a Slack notification when there is a malicious ip address that hits the set threshold.
- Look at ways to block and unblock potentially malicious IP addresses.