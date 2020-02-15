import boto3
import gzip
from io import BytesIO
from config import bucket, key
import re
from itertools import groupby
from ip_manipulator import get_london_ips

s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket)
s3_key = key
client = boto3.client('s3')

london_ips = get_london_ips()

def find_ip(element):
    element_lowercase = element.lower()
    if "possible break-in attempt" in element_lowercase or "Invalid user" in element:
        malicious_ips = re.search("\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}", element).group(0)
        if malicious_ips not in london_ips:
            return malicious_ips

def list_files_within_the_last_hour():
    appended_list = []
    ip_list = []
    FilesNotFound = True
    for obj in bucket.objects.filter(Prefix=s3_key):
        n = obj.get()['Body'].read()
        gzipfile = BytesIO(n)
        gzipfile = gzip.GzipFile(fileobj=gzipfile)
        content = gzipfile.read().decode("utf-8").splitlines()
        appended_list.extend(content)

    for obj in appended_list:
        ip = find_ip(obj)
        if ip is not None:
            ip_list.append(ip)
        results = {value: len(list(frequency)) for value, frequency in groupby(sorted(ip_list))}
        return results
    else:
        return None

        FilesNotFound = False
    if FilesNotFound:
        print("No Files Found!", "No file in {0}/{1}".format(bucket, s3_key))

list_files_within_the_last_hour()