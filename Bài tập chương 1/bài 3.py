class PS:
    def __init__(self, tu=0, mau=1):  
        self.tu = tu
        self.mau = mau

    def nhap_ps(self):
        self.tu = float(input("Nhập tử số: "))
        self.mau = float(input("Nhập mẫu số: "))

    def kiemtra(self):
        if self.mau == 0:
            print("Đây không phải là phân số, mời nhập lại.")
        else:
            print("Phân số của bạn là:", self.tu, "/", self.mau)

# Khởi tạo một đối tượng của lớp PS
Ps = PS()
Ps.nhap_ps()
Ps.kiemtra()  # Gọi phương thức kiemtra

