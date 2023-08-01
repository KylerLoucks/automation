#!/bin/bash

set -eux

S3_BUCKET_NAME="bucket_name"

# Create S3 bucket
aws s3 mb s3://${S3_BUCKET_NAME} > /dev/null

# Sync files to the bucket
aws s3 sync ./folder_to_sync s3://${S3_BUCKET_NAME} > /dev/null