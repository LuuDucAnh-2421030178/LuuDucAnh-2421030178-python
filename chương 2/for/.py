a = []
s = 0
n = int(input("nhập số ptử của dãy số: "))

for i in range(1, n + 1):
    k = int(input("nhập phần tử thứ " + str(i) + ": "))
    a.append(k)

for i in a:
    s = s + i

print("Tổng của dãy số là: " + str(s))
