n=int(input(("enter the number")))
list=[]
for i in range(n):
    temp=[]
    for j in range(i+1):
        if(j==0) or (j==i):
            temp.append(1)
        else:
            temp.append(list[i-1][j-1] +list [i-1][j])
    list.append(temp)
print(list)
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(list[i][j],end=" ")
    print()


