# Question
    - Optimize job scheduling(JS)
    - (Yes/No) Can jobs be scheduled less than *k* units of time?

## Complexity class of the problem
    - Show NP-complete: show JS is in NP and 3SAT <= JS
        - Establish a polynomial time algorithm that translates 3SAT into JS
        - If JS can be solved in P, 3SAT should be solved in P. This is contradiction.

# Instance
## Job
    - Duration(Processing Time)
    - Time of start
    - Time of end
    - Waiting time

## CPU
    - A CPU can process one job at a time of unit period.

## Criteria
    - Average waiting time
    - Time to finish all jobs

# Solving
    - We have SAT solvers.
    - Translate an arbitrary JS to SAT, then solve SAT by SAT solver.

# Test and Analysis
    - Correctness (Yes to yes instances, No to no instances)
    - Running Time with respect to input size
    -
