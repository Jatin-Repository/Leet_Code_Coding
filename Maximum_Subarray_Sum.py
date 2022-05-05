
n = int(input("Enter the size of array:\n"))
print("Enter the number to be inserted in array:\n")
arr = []
for i in range(0, n):
    x = int(input())
    arr.append(x)

"""
          Naive Approach O(n^3)
         1) With n element total n(n+1)/2 subarray combination
         2) Iterate over each approx n^2 subarray for n times to find max subarray leads to O(n^3)
"""

"""
          Coding for Naive Approach
maximum_sum = add = pre_max = 0
for i in range(0, n):
    for j in range(0, n):
        pre_max = arr[j]
        add = 0
        for k in range(j+1, n):
            add += arr[k]
            if add > pre_max:
                pre_max = add
            if pre_max > maximum_sum:
                maximum_sum = pre_max
print(maximum_sum)


"""


"""
          Optimized Approach O(n^2)
         1) With n element total n(n+1)/2 subarray combination
         2) Iterate over each approx n^2 subarray for n times to find max subarray leads to O(n^3)
"""
"""

maximum_sum = add = pre_max = 0
for i in range(0, n):
    pre_max = arr[i]
    add = 0
    for j in range(i+1, n):
        add += arr[j]
        if add > pre_max:
            pre_max = add
        if pre_max > maximum_sum:
            maximum_sum = pre_max
print(maximum_sum)

"""

"""
 Kadane's Algorithm
   1) Solve with similar approach but update if it pre_sum is >0.
   2) Update the max value to pre_sum
"""

cur_sum = 0
maximum_sum = arr[0]
for i in range(0, n):
    cur_sum += arr[i]
    if cur_sum > maximum_sum:
        maximum_sum = cur_sum
    if cur_sum <= 0:
        cur_sum = 0
print(maximum_sum)

