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
    # third function that calculates the square of the numbers from 0 to 99999999
    return [i**2 for i in range(100000000)]

# 1. A profiler is a module that generates a statistic of a program in the form of a report to describe how often each part run and how long it takes to execute them.

# 2. Profiling summarizes a program’s execution, while benchmarking compares multiple programs. Profiling in Python differs from benchmarking since profilers add overhead, making fair comparisons difficult. This is especially true for Python vs. C, as profilers slow down Python but not C, making C seem faster.

pr = cProfile.Profile()

pr.enable()
test_function()
pr.disable()

s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())

pr.clear()

pr.enable()
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