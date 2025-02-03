1. Interpolation search is better when we have uniform data (equal difference between the values of indexes). For example, considering an array={10,20,30,40,50}, and the difference between the values is the same, i.e., in our case, it is 10 between all the values at the different index. 
In the above case, interpolation search is better for estimation, whereas binary search is better when the data is not uniform and equally spaced.
Interpolation search gives a better estimation of the target position.

2. Interpolation search alogrithum is good for unform distribution data, but if the data is not uniform, the performance will be degraded, since the estimation of the element at the required index is not correct. 

3. pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))
This part of the code will be affected, since this part of code is responsible for getting the position of the element in the array.

4. Linear search is better in case if we don't have to follow the complex alogrithums as above. Working on a small array, we have repeated occurances of the same element, data is unsorted and as stated above it is not required to to use complex alogrithum as compared to linear search.
When we don't have any knowledge of data whether it does follow the above conditions like sorted, uniform it is better to use linear search.

5. Considering a small array like an array with less than 10 elements, using binary search as calculating the midpoints and then finding the element will be more complex, and linear search will be a better option in that case.

6. Using the interpolation and binary search depending upon the requirement untill we reach at a certain point when the array size is shrinked to a certain point we can use linear search to increase the speed of the output.