## NP-complete scheduler
This is a job scheduler that answers whether given a set of jobs can be finished in time.
### Final Paper
  - [Google Doc](https://docs.google.com/document/d/1h5Jn-hfyWUJGp7O47tWCFypgyM2amLW8-H0ZhYZesl0/edit?usp=sharing)
  - [Overleaf](https://www.overleaf.com/4414353837nknwqqzgsnyk)

### Parameters
Jobs        : any given jobs can have priority relationship
Processors  : number of processors for handling this problem
Time        : time limit for finishing all the jobs

### Usage 
```
./schedule.py -j [Information of jobs] -p [number of processor] -t [deadline of time]
```

for example
```
./schedule.py -j jobs/kitchen.json -p 1 -t 15
```

