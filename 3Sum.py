list1 = list()
n = int(input("Enter the number of element to be placed in list:\n"))
for k in range(0, n):
    x = int(input())
    list1.append(x)
print(list1)
length = len(list1)
list2 = list(list())
if length == 0:
    print(list2)
    exit()
list1.sort()
print(list1)
list2 = list(list())
length = len(list1)
max1 = list1[length-1]
min1 = list1[0]
count = 0
for i in range(0, length):
    for j in range(i+1, length):
        add = list1[i] + list1[j]
        add = add * -1
        if min1 <= add <= max1:
            lb = 0
            ub = length-1
            index = -1
            while lb < ub:
                mid = (lb+ub)//2
                if list1[mid] == add:
                    index = mid
                    break
                elif list1[mid] > add:
                    ub = mid-1
                elif list1[mid] < add:
                    lb = mid+1
            if index >= 0:
                first = list1[i]
                second = list1[j]
                third = list1[index]
                list3 = list()
                list3.append(first)
                list3.append(second)
                list3.append(third)
                list3.sort()
                if list3 not in list2:
                    list2.append(list3)
print(list2)
