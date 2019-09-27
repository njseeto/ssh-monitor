import boto3
import gzip
from io import BytesIO
from config import bucket, key
import re

s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket)
s3_key = key
client = boto3.client('s3')

def find_ip(element):
    element_lowercase = element.lower()
    if "possible break-in attempt" in element_lowercase or "invalid user" in element_lowercase:
        return re.search("\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}", element).group(0)

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
        print(len(appended_list))

        FilesNotFound = False
    if FilesNotFound:
        print("No Files Found!", "No file in {0}/{1}".format(bucket, s3_key))

def read_one_file():
    try:
        s3 = boto3.resource('s3')
        obj = s3.Object(bucket, s3_key) # need to add the specific file
        n = obj.get()['Body'].read()
        gzipfile = BytesIO(n)
        gzipfile = gzip.GzipFile(fileobj=gzipfile)
        content = gzipfile.read()
        print(content)
    except Exception as e:
        print(e)
        raise e