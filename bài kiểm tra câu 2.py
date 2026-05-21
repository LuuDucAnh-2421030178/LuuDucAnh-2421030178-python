n = int(input("Nhập số nguyên dương n: "))

tong_chu_so = sum(int(c) for c in str(n))

if tong_chu_so % 3 == 0:
    print(f"Tổng các chữ số ({tong_chu_so}) chia hết cho 3.")
else:
    print(f"Tổng các chữ số ({tong_chu_so}) không chia hết cho 3.")