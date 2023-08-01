#!/bin/bash

set -eux

stack_name="cloudformation_stack_name"

# Delete Cloudformation stack example:
aws cloudformation delete-stack --stack-name "${stack_name}" > /dev/null