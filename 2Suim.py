"""
 Complexity : O(n^2)
target = int(input("Enter the target value:\n"))
x = int(input("Enter the number of element to be inserted in list:\n"))
list1 = list()
list2 = list(list())
for i in range(0, x):
    t = int(input())
    list1.append(t)

length = len(list1)-1
for a in range(0, length, 1):
    p = list1[a]
    for b in range(length, a, -1):
        q = list1[b]
        if p + q == target:
            list4 = list()
            list4.append(a)
            list4.append(b)
            if list4 not in list2:
                list2.append(list4)
print(list2)
"""

target = int(input("Enter the target value:\n"))
x = int(input("Enter the number of element to be inserted in list:\n"))
list1 = list()
left = dict()
list2 = list()
for i in range(0, x):
    t = int(input())
    rem = target - t
    left[i] = t
    list1.append(rem)
for x, y in left.items():
    if y in list1:
        m = list1.index(y)
        n = x
        break
list2.append(n)
list2.append(m)
print(list2)

