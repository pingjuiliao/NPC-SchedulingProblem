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

# Set maximum order
print("Enter maximum dependency: ", end="")
m_order = int(six.moves.input())

# Total load
tot_load = 0;

for i in range(1, n_job+1):
    this_load = random.randint(1, l_load+1)
    tot_load += this_load
    this_order = random.randint(0, m_order)
    if this_order > (i-1):
        this_order = i-1

    order_list = random.sample(range(1, this_order+1), this_order)
    dependency = []
    for e in order_list:
        dependency.append("job"+str(e))

    data['jobs']['job'+str(i)] = [this_load, dependency]

json_obj = json.dumps(data, indent = 3)
print("Total load %d" %(tot_load))
print(data)

with open('case_order.json', 'w') as outfile:
    outfile.write(json_obj)
