import boto3
import json
from inspect import getmembers
from optparse import OptionParser
from bson import json_util
import datetime

client = boto3.client('macie2',region_name='us-east-1')
my_list=list()
paginator = client.get_paginator('list_findings')
index=1
for finding in paginator.paginate(maxResults=50):
    for findingid in finding['findingIds']:
        a=my_list.append(findingid)
        a=findingid
#print(my_list)
#print(type(my_list))
for i in my_list:
    response = client.get_findings(findingIds=[i])
    print(response)
    def datetime_handler(x):
        if isinstance(x, datetime.datetime):
            return x.isoformat()
        raise TypeError("Unknown type")
    json.dumps(response, default=datetime_handler)
    with open("sample.json", "a") as json_file:
        print(response)
        json.dump(response,json_file,indent=4,default=datetime_handler)
    
