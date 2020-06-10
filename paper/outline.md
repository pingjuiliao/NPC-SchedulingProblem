## Abstract

## Introduction
### Question
* Optimize job scheduling(JS) => NP-Hard
* (Yes/No) Can jobs be scheduled within *k* units of time budget? => NP-Complete

### Complexity class of the problem & Background
* Show NP-complete: show JS is in NP and 3SAT <= JS
    * Establish a polynomial time algorithm that translates 3SAT into JS
    * If JS can be solved in P, 3SAT should be solved in P. This is contradiction.
    * 3SAT <= SUBSET-SUM <= JS [link](https://web.stanford.edu/class/archive/cs/cs103/cs103.1132/lectures/27/Small27.pdf)
    * 3SAT <= JS [link](https://cs.stackexchange.com/questions/91599/3-sat-reduction-to-jobs-scheduling-problem-np-completeness)
* Similar problems

### An Instance
#### Job
* Load (Processing Time required to finish a job)
* Time of start
* Time of end
* Waiting time
* A CPU can process one job at a time of unit period.

#### Criteria
* Average waiting time
* Time to finish all jobs
* Average (end - start)

#### Extras
* Dependency between jobs?
* Whether a job can be stopped/resumed
* Priority?
* Each job has 1 time unit of load
* Multicore

## Implementation & Solving
* We have SAT solvers.
* Translate an arbitrary JS to SAT, then solve SAT by SAT solver.
* Explain our reduction and algorithm
* Sample generation

## Evaluation - Test and Analysis
* Correctness (Yes to yes instances, No to no instances)
* Running Time with respect to input size
    * Graph representation would be good

## Discussion
