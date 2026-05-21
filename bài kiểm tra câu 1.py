n = int(input("Nhập n: "))

x = []
for i in range(n):
    x.append(float(input(f"Nhập x[{i+1}]: ")))

duong_hop_le = [xi for xi in x if 0 < x < 1000]

if duong_hop_le:
    trung_binh = sum(duong_hop_le) / len(duong_hop_le)
    print(f"Trung bình cộng: {trung_binh:.2f}")
else:
    print("Không có phần tử nào thỏa mãn điều kiện.")
