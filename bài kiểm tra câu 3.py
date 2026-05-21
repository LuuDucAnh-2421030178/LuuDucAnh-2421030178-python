n = int(input("Nhập số nguyên dương n: "))

tich_chu_so = 1
for c in str(n):
    tich_chu_so *= int(c)

if tich_chu_so % 2 == 0 and tich_chu_so > 20:
    print(f"Tích các chữ số ({tich_chu_so}) là số chẵn và lớn hơn 20.")
else:
    print(f"Tích các chữ số ({tich_chu_so}) KHÔNG thỏa mãn điều kiện.")