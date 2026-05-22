class bai:
    def __init__(self):
        self.a = int(input("Nhập số nguyên dương a: "))
        self.b = int(input("Nhập số nguyên dương b: "))

    def chu_so_nho_nhat(self):
        min_digit = 9
        while self.b > 0:
            digit = self.b % 10
            if digit < min_digit:
                min_digit = digit
            self.b //= 10
        return min_digit

    def kiem_tra_chia_het(self):
        min_digit = self.chu_so_nho_nhat()
        if min_digit == 0:
            return "Chữ số nhỏ nhất của b là 0, không thể chia cho 0"
        elif self.a % min_digit == 0:
            return "a chia hết cho chữ số nhỏ nhất của b là {}".format(min_digit)
        else:
            return "a không chia hết cho chữ số nhỏ nhất của b là {}".format(min_digit)
c = bai()
print(c.kiem_tra_chia_het())
