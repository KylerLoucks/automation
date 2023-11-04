import boto3
import logging

class S3Service:

    def __init__(self, region):
        self.s3_client = boto3.client(
            's3',
            region_name=region
        )

    def read_binary(self, bucket, key):
        """
        Return an objects body content.
        """
        logging.debug(f"About to read binary for key: [{key}] in bucket: [{bucket}]")

        response = self.s3_client.get_object(Bucket=bucket, Key=key)
        binary_content = response['Body'].read()
        return binary_content

    def search(self, bucket, prefix):
        """
        Search for and return a list of objects by a prefix
        """
        logging.debug(f"Searching objects in bucket: [{bucket}] with prefix: [{prefix}]")

        keys = []
        paginator = self.s3_client.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
            for content in page.get("Contents", []):
                keys.append(content["Key"])

        return keys

    def write_binary(self, bucket, key, binary, metadata=None):
        logging.debug(f"About to write binary for key: [{key}] in bucket: [{bucket}] with metadata: {metadata}")

        response = self.s3_client.put_object(Bucket=bucket, Key=key, Body=binary, Metadata=metadata if metadata else {})
        return response

    def delete_object(self, bucket, key):
        logging.debug(f"About to delete Object [{bucket}].[{key}]")
        self.s3_client.delete_object(Bucket=bucket, Key=key)

    def delete_objects(self, bucket, prefix):
        logging.debug(f"About to delete objects from [{bucket}] with prefix [{prefix}]")

        # Get all keys with the given prefix
        keys_to_delete = [{'Key': key} for key in self.search(bucket, prefix)]
        if keys_to_delete:
            self.s3_client.delete_objects(Bucket=bucket, Delete={'Objects': keys_to_delete})

    def does_object_exist(self, bucket, key):
        logging.debug(f"About to see if Object [{bucket}].[{key}] exists")
        try:
            self.s3_client.head_object(Bucket=bucket, Key=key)
            return True
        except:
            return False
