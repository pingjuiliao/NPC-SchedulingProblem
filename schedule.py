#!/usr/bin/python
import argparse
import json
import sys
import time
from z3 import *

PROBLEM_NAME = "name"
JOBS         = "jobs"


def parseArg() :
    p = argparse.ArgumentParser()
    p.add_argument("-j", dest="input_file", help="JSON file of scheduling problem", required=True)
    p.add_argument("-p", type=int, dest="num_processor", help="Number of processors to solve this problem", required=True)
    p.add_argument("-t", type=int, dest="time_limit", help="time limit for this problem to finish all the jobs", required=True)
    return p.parse_args()

def parseJSON(filename) :
    with open(filename, "rb") as f :
        s = f.read()
        f.close()

    return json.loads(s)

def summary(prob) :
    print("Decoding problem : {}".format(prob[PROBLEM_NAME]))
    for k, v in prob[JOBS].items() :
        jobName  = str(k).rjust(20, "-")
        timeUnit = str(v[0]).rjust(3, " ")
        preReq   = str(v[1]).rjust(30, " ")
        print("{} is a {}-unit job".format(jobName, timeUnit))
        print(" "*24 + "must execute {} first\n".format(preReq))


def get_job_list(prob) :
    j_list   = []
    j_id_map = {}

    ## ID mapping ( map 'name' to 'id' )
    j_id = 0
    for k in prob[JOBS].keys() :
        j_id_map[k] = j_id
        j_id += 1


    for k, v in prob[JOBS].items() :
        j = {}
        j['ID']       = j_id_map[k]
        j['name']     = k
        j['duration'] = v[0]
        j['priori']   = []
        for priori_name in v[1] :
            if priori_name not in j_id_map :
                print("[FATAL] Unrecognized job name '%s' in the prerequisite list" % priori_name)
                sys.exit(-1)
            j['priori'].append(j_id_map[priori_name])
        j_list.append(j)
    return j_list

def solveSchedule(prob, num_processors, time_limit) :

    ## get the transform the list of job
    job_list = get_job_list(prob)
    n = len(job_list)

    ## the starting time for each job
    symbols  = [ Int("J_%03d" % i) for i in range(n) ]

    ## any given jobs must start between time '0' and 'time_limit-1'
    start_bound_c = [ And(0 <= symbols[i], symbols[i] < time_limit) for i in range(n) ]

    ## any given jobs must end before the time limit
    end_bound_c   = [ symbols[i] + job_list[i]['duration'] <= time_limit
                                                        for i in range(n) ]

    ## k processors
    processor_c = []
    for time_slot in range(time_limit) :
        one_processor_one_exec      = [ ( And(symbols[i] <= time_slot, time_slot < symbols[i] + job_list[i]['duration']), 1) for i in range(n) ]
        less_than_k_of_them_is_true = PbLe(one_processor_one_exec, num_processors)
        processor_c.append(less_than_k_of_them_is_true)

    ## any given jobs must start after its priorities
    priori_c = []
    for this_job_id in range(n) :
        for priori_id in job_list[this_job_id]['priori'] :
            priori_c.append( symbols[priori_id] + job_list[priori_id]['duration'] < symbols[this_job_id] )


    ## solve it !!
    print("# Solving.....")
    print("# Using %d processors" % num_processors)
    print("# Must finish all in %d time unit\n" % time_limit)
    print("#" * 50)
    s = Solver()
    s.add( start_bound_c + end_bound_c + processor_c + priori_c )

    sat_tic   = time.time()
    sat_check = s.check()
    sat_toc   = time.time()

    ## Display
    tic = toc = None
    if sat_check == sat :
        m = s.model()
        tic    = time.time()
        result = [ m.evaluate(symbols[i]) for i in range(n) ]
        toc    = time.time()
        sched  = [ (result[i], job_list[i]['name']) for i in range(n) ]
        sched  = sorted(sched, key=lambda x: int(str(x[0])) )
        for i in range(n) :
            print("# %2s : %20s" % (sched[i][0], sched[i][1]))

    else :
        print("UNSAT")

    print("#" * 50 + "\n")
    print(" Solving time    : %.8f " % (sat_toc - sat_tic) )
    if tic is None or toc is None :
        quit()
    print(" Evaluation time : %.8f" % (toc - tic))

def main() :
    args = parseArg()
    print(args.input_file)
    prob = parseJSON(args.input_file)
    summary(prob)
    solveSchedule(prob,
            num_processors=args.num_processor, time_limit=args.time_limit)

if __name__ == "__main__" :
    main()
