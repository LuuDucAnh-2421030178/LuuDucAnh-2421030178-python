
def giai_thua(m):
    gt = 1
    for i in range(1, m + 1):
        gt = gt * i
    return gt

n = int(input("nhập n: "))

ket_qua_gt = giai_thua(n)

print("Giai thừa của", n, "là:", ket_qua_gt)
