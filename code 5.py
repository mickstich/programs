string = input("Enter a string ")
list = []
for i in string:
    if i not in list:
        list.append(i)
for j in list:
    print(j,string.count(j))


