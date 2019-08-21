import boto3
import gzip
from io import BytesIO
from config import bucket, key

s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket)
s3_key = key
client = boto3.client('s3')

def list_files_within_the_last_hour():
    s3_list = []
    FilesNotFound = True
    for obj in bucket.objects.filter(Prefix=s3_key):
        n = obj.get()['Body'].read()
        gzipfile = BytesIO(n)
        gzipfile = gzip.GzipFile(fileobj=gzipfile)
        content = gzipfile.read()
        print(content)
        file = ('{0}'.format(obj.key))
        s3_list.append(file)
        FilesNotFound = False
    if FilesNotFound:
        print("No Files Found!", "No file in {0}/{1}".format(bucket, s3_key))
    print(s3_list)
    return (s3_list, content)