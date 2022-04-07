string = input("Enter the String to input\n")
dis_string = dict()
dis_string_rev = dict()
i = j = 0
count = 0
temp = ""
length = len(string)
while i < length:
    temp = ""
    j = i
    while j < length:
        temp = string[i:j+1]
        if temp not in dis_string.values() and len(temp) > 1:
            dis_string[count] = temp
            count += 1
        j += 1
    i += 1
list1 = list()
count = 0
for t in dis_string.values():
    temp1 = t[::-1]
    if t == temp1:
        dis_string_rev[count] = temp1
        list1.insert(count, len(t))
        count += 1
#  print(len(dis_string_rev))
if len(dis_string_rev) == 0:
    print("Empty Dictionary")
    exit()
else:
    index = 0
    print(list1)
    for k in range(1, count):
        if list1[k] > list1[index]:
            index = k
    print(dis_string_rev)
    print(dis_string_rev[index])
