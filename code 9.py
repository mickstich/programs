a = ["malasia","malayalam","malai"]
item1= a[0]
for i in range(1,len(a)):
    b = ""
    for j in range(len(a[i])):
       if j<len(item1) and item1[j] == a[i][j]:
         b+=item1[j]
       else:
        break
    item1 = b
print(item1)




