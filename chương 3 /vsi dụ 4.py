m=int(input("nhap so hang="))
n=int(input("nhap so cot="))
a=[]
for i in range(0,m):
    a.append([])
for j in range(0,n):
    x=float(input("nhap phan tu thu a[%2d][%2d]:"%(i+1,j+1)))
a[i].append(x)
obj=open("e:\\ma tran.txt","w")
obj.write("mang vua nhap la:\n")
for i in range(0,m):
    for j in range(0,n):
        obj.write(str(a[i][j])+" ")
        obj.write("\n")
        obj.close()
