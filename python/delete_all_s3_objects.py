import boto3
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prefix", "-p", default="", type=str)
    return parser.parse_args()

def delete_all_objects(bucket_name):
    s3 = boto3.client('s3')

    # Get the list of objects in the bucket
    paginator = s3.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket_name, Prefix=prefix)
    total_deleted = 0
    for page in pages:
        keys_to_delete = [{'Key': obj['Key']} for obj in page['Contents']]
        s3.delete_objects(Bucket=bucket_name, Delete={'Objects': keys_to_delete})
        print(f'Deleted {page["KeyCount"]} objects')
        total_deleted = total_deleted + page["KeyCount"]
        print(f'Total objects deleted: {total_deleted}')


if __name__ == '__main__':
    args = parse_args()
    prefix = args.prefix
    bucket_name = 'forecast-prod-us-east-1-benchmarklabs-partitioned'  # Replace with your S3 bucket name
    delete_all_objects(bucket_name)
