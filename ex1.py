import timeit
import matplotlib as plt
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
    
    #qs1: This code is finding the fibonacci series and retruns n'th element in the fibonacci series
    
    #qs2:Yes it is as its spliting the problem in to smaller problems and its solving then recursively and once it reaches the end it merges them to find the final solution

    #qs3: time = a * 2^n , a is the time it takes for func(0), so in my case its 1.6999983927235007e-06, so the time complexity expression is O(2^n)

#qs4:

def func_impr(n, store={}):
    if n == 0 or n == 1:
        return n
    if n in store:
        return store[n]

    store[n]= func_impr(n-1, store) + func_impr(n-2, store)
    return store[n]
    
#qs5: 

#qs6:
integer = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]

plt.figure(figsize=(10,5))
plt.dotplt()

#0+1+2+3+4+5+6
#0, 1, 1, 2, 3, 5, 8, 13, 21

if __name__ == "__main__":
    elapsed_time = timeit.timeit(lambda : func(39), number=1)
    elapsed_time2 = timeit.timeit(lambda : func_impr(39), number=1)
    print(func(5)) 
    print(elapsed_time)
    print(func_impr(5))
    print(elapsed_time2)

