import boto3
import json
from datetime import datetime

client = boto3.client('macie2', region_name='us-east-1')
finding_ids = list()  # Use a more descriptive name

paginator = client.get_paginator('list_findings')
for finding in paginator.paginate(maxResults=50):
  finding_ids.extend(finding['findingIds'])  # Use extend for adding multiple elements

def datetime_handler(x):
  if isinstance(x, datetime):
    return x.isoformat()
  raise TypeError("Unknown type")

with open("sample.json", "a") as json_file:
  for finding_id in finding_ids:
    response = client.get_findings(findingIds=[finding_id])
    print(response)
    json.dump(response, json_file, indent=4, default=datetime_handler)
