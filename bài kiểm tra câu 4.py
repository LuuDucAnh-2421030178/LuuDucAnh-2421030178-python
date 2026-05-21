a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

tong = a + b
chu_so_lon_nhat = max(int(c) for c in str(tong))

print(f"Tổng a + b = {tong}")
print(f"Chữ số lớn nhất trong tổng: {chu_so_lon_nhat}")