n=int(input("enter the no'"))
k=[]
while (n>0):
    a=int(float(n%2))
    k.append(a)
    n=(n-a)/2
string=""
for j in k[::-1]:
    string=string+str(j)
print("The binary no is %s" %(string))
