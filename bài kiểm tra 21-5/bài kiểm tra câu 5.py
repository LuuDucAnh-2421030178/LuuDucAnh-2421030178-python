m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))

tong_chu_so_n = sum(int(c) for c in str(n))

if tong_chu_so_n == 0:
    print("Tổng chữ số của n bằng 0, không thể chia.")
elif m % tong_chu_so_n == 0:
    print(f"m = {m} chia hết cho tổng chữ số của n ({tong_chu_so_n}).")
else:
    print(f"m = {m} không chia hết cho tổng chữ số của n ({tong_chu_so_n}).")
