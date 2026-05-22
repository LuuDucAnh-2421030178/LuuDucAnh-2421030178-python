n = int(input("nhap n="))
dem = 0
i = 2

while n > 1:
    if n % i != 0:
        i = i + 1
    else:
        dem = dem + 1
        while n % i == 0:
            n = n // i

print("so cac so nguyen to la:", dem)