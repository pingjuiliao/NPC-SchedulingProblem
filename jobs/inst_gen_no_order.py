#! /usr/bin/env python

import json
import random
import six

data = {}
data['name'] = "test1"
data['jobs'] = {}

# Number of Jobs
print("Generating a test case")
print("Enter the number of jobs: ", end="")
n_job = int(six.moves.input())

# Load limit
print("Enter the limit of load: ", end="")
l_load = int(six.moves.input())

# Total load
tot_load = 0;

for i in range(1, n_job+1):
    load = random.randint(1, l_load+1)
    tot_load += load
    data['jobs']['job'+str(i)] = [load, []]

json_obj = json.dumps(data, indent = 2)
print("Total load %d" %(tot_load))

with open('case_no_order.json', 'w') as outfile:
    outfile.write(json_obj)
