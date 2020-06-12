## NP-complete scheduler
This is a job scheduler that answers whether given a set of jobs can be finished in time.

### Parameters
- Jobs        : A job has a time load. Any given jobs can have dependency relationship
- Processors  : Number of processors for handling this problem
- Time        : Time budget for finishing all the jobs

### Usage 
```
./schedule.py -j [path/to/json file] -p [number of processor] -t [time budget]
```

for example
```
./schedule.py -j jobs/kitchen.json -p 1 -t 15
```

#### Instance generator
Empty dependency
```
./jobs/inst_gen_no_order.py
```
Custom dependency
```
./jobs/inst_get_order.py
```
