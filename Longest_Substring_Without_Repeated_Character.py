"""

Idea:
    1) Take to Pointing variable i and j with initial value i = j = 0
    2) Take and empty string temp;
        $ while j not equal to string length
            -----> if character exits apply break and come out of the loop
            ----> add character to temp if string[i:j] does not contain character and increment j
    3) Maintain a dictionary for different distinct substring and find length and print the maximum ones.

"""

string = input("Enter the String to input\n")
dis_string = dict()
i = j = 0
count = 0
temp = ""
length = len(string)
ask = True

while i<length:
    temp = ""
    j = i
    while j < length:
        x = string[j]
        if x not in temp:
            temp += x
        else:
            break
        j += 1
    if temp not in dis_string.values():
        dis_string[count] = temp
        count += 1
    i += 1
print(dis_string)
list1 = list()
for t in dis_string.values():
    list1.append(len(t))
length2 = len(list1)
maximum = list1[0]
index = 0
for k in range(1, length2):
    if maximum < list1[k]:
        maximum = list1[k]
    else:
        continue
list2 = list()
for m in range(0, length2):
    if list1[m] == maximum:
        list2.append(dis_string[m])
print(list2)
print(list1)