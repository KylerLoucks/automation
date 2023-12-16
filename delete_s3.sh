#!/bin/bash

set -eux

S3_BUCKET_NAME="forecast-prod-us-east-1-benchmarklabs-partitioned"

# --force removes non versioned objects before removing the bucket.
# https://docs.aws.amazon.com/cli/latest/reference/s3/rb.html
echo "deleting s3://${S3_BUCKET_NAME}"
aws s3 rb s3://${S3_BUCKET_NAME} --force > /dev/null
