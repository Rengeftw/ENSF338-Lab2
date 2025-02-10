import timeit
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#Ex 5 part 1 Implementing linear search and binary search

def linearsearch(arr, target):
    i=0
    for i in range(len(arr)):
        if target == arr[i]:
            return i
    return -1
    
    
def binarysearch(arr, target):
    low= 0; high=size
    
    while (low <= high):
            middle = (low+high)//2
            if (target==arr[middle]):
                return middle
            elif (target < arr[middle]):
                high = middle - 1
                
            else:
                low = middle+1       
    return -1



arr_sizes = [1000,2000,3000,4000,5000,6000,7000]
target_value =  3000
size=len(arr_sizes)


#Ex 5 Part 2
def evaluateSearchTime(searchFunc,arrayLength,iterations=100):
    total_time = timeit.timeit(lambda : searchFunc(list(range(arrayLength)), random.randint(0,arrayLength-1)), number=iterations)
    return total_time/iterations
    

sizes = [1000,2000,4000,8000,16000,32000]

for length in  sizes:
    avg_duration = evaluateSearchTime(linearsearch,length)
    print(f'Average time for simple search on array {length}: ~ {avg_duration} seconds')
    
for length in  sizes:
    avg_duration = evaluateSearchTime(binarysearch,length)
    print(f'Average time for fast search on array {length}: ~ {avg_duration} seconds')

#Ex 5 Part 3
simple_times = [evaluateSearchTime(linearsearch, length) for length in sizes]    
fast_times = [evaluateSearchTime(binarysearch,length) for length in sizes]

def linear_function(x, a, b):
    return a * x + b

def log_function(x, a, b):
    return a * np.log(x) + b

# Curve fitting
params_simple, _ = curve_fit(linear_function, sizes, simple_times)
params_fast, _ = curve_fit(log_function, sizes, fast_times)

# Plotting
plt.figure(figsize=(12, 6))    
# linera Search Plot
plt.subplot(1, 2, 1)
plt.scatter(sizes, simple_times, label='Measured Times')
plt.plot(sizes, linear_function(np.array(sizes), *params_simple), label='Fitted Line', color='red')
plt.title('Simple Search Performance')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.legend()
# Bineary Search Plot
plt.subplot(1, 2, 2)
plt.scatter(sizes, fast_times, label='Measured Times')
plt.plot(sizes, log_function(np.array(sizes), *params_fast), label='Fitted Curve', color='green')
plt.title('Fast Search Performance')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.legend()

plt.tight_layout()
plt.show()


""" 
Exercise 5 part 4:

The interpolating function for linear search is a linear function and the the best-fitting function for a lineare function is a straight-line equation:
f(x) = a * x + b

Parameters: 
a (slope): This tells us how much the time increases as the array gets bigger. A larger "a" means the search takes more time as the list grows.
b (y-intercept): This is the starting time when the array size is zero. It represents the minimum time the algorithm takes, no matter what.


BINARY SEARCH: 
The interpolating function for binary search is a logarithmic function.
A logarithmic function is of the form f(x) = a * log(x) + b


Paremeters:
a (coefficient): This shows how fast the search time increases as the array grows. Since binary search is very efficient, the time grows much slower compared to linear search.
b (constant): This is the starting time when the array size is very small.

Conclusion:
The results match our expectations. Linear search time increases directly with the size of the list, while binary search time grows much more slowly. 
This confirms the theoretical understanding that linear search is slower for large datasets, while binary search is much more efficient.

"""
