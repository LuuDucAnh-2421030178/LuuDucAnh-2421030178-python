#vd
n = int(input("nhap n:"))
tong = 0
i = 1
while i <= n:
    i = i + 1
    print("tong la",tong)
#lenh (break)
var = 10
while var > 0
print('gia tri bien hien tai la:',var)
var = var - 1
if var ==5:
    break
#lenh continve
var = 5
while var > 0:
    var = var - 1
    if var == 3:
        continue
    print('gia tri bien hien tai la:',var)
#lenh (pass)
i = 1
while i <= 10:
    if(i % 2 == 0):
        pass
    else:
        print(i)
        i = i + 1
#nhap vao 3 diem toan ly hoa
x = float(input('Nhap diem toan:'))
y = float(input('Nhap diem ly:'))
z = float(input('Nhap diem hoa:'))
tong = (x + y + z) / 3
if tong < 5:
    print("yeu")
    if (tong > 5) and (tong < 9):
        print("tb")
    else if (tong > 7) and (tong < 9):
print('kha')
else:
print('gioi')
#vd nhap vao 1 day so tinh tong cac so chan co mat trong day so
day_so = list(map list,input("Nhap day so:"))
input_string = input("Nhap day so (canh nhau boi dau cach):")
numbers = [int (x) forx in input_string.split()]
tong_chan = 0
i = 0
while i < len(numbers):
    if nimbers [i] %2 == 0:
        tong_chan += numbers[i]
        i += 1
        print[(f"tong cac so chan la:{tong_chan}")]
