m=int(input("nhap m="))
n=int(input("nhap n="))
a=[]
for i in range(0,m):
    a.append([])
    for j in range(0,n):
        x=float(input("nhap phan tu thu a [%d][%d]"%(i+1,j+1)))
        a[i].append(x)
        print("mang ma nhap b:")
        for i in range (0,m):
            for j in range (0,n):
                print("%8.2f"%a[i][j],end='')
                print()