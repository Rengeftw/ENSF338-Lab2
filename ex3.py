import timeit
import cProfile, pstats, io
from pstats import SortKey

def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
    
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    # third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

#test_function()
#third_function()

# formated into reports via the pstats module

# 1. A profiler is a module that generates a statistics of a program in the form of a report to describe how often each part fun or how long it takes to execute them.

# 2. Profiling is providing a summary of a program execution, where as benchmarking is comparing two or more program to measure different aspects of their execution. Profiling for python is different than benchmarking because profilers add overheads to to the profiled program, which makes it diffult to compare programs fairly.

pr = cProfile.Profile()
pr.enable()

test_function()
third_function()

pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())

# 3. 
# 68 function calls (23 primitive calls) in 16.266 seconds

#    Ordered by: cumulative time

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1   16.266   16.266   16.266   16.266 c:\Users\mikam\Desktop\School\Winter2025\ENSF338\ENSF338-Lab2\ex3.py:18(third_function)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 c:\Users\mikam\Desktop\School\Winter2025\ENSF338\ENSF338-Lab2\ex3.py:12(test_function)
#     55/10    0.000    0.000    0.000    0.000 c:\Users\mikam\Desktop\School\Winter2025\ENSF338\ENSF338-Lab2\ex3.py:5(sub_function)
#        10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# 4. Most of the execution time goes to the funciton
# third_function(), because more operations are performed
# in third_fuction() compared to test_function().