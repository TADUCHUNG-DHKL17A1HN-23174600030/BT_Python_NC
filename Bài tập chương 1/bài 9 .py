class DaGiac:
    def __init__(self, canh):
        self.canh = canh  # Danh sách độ dài các cạnh

    def chu_vi(self):
        return sum(self.canh)

    def display(self):
        print(f"Đa giác có {len(self.canh)} cạnh: {self.canh}")
        print(f"Chu vi: {self.chu_vi()}")

class HinhBinhHanh(DaGiac):
    def __init__(self, canh_dai, canh_ngan):
        super().__init__([canh_dai, canh_ngan, canh_dai, canh_ngan])
        self.canh_dai = canh_dai
        self.canh_ngan = canh_ngan
        self.chieu_cao = float(input("Nhập chiều cao của hình bình hành: "))

    def dien_tich(self):
        return self.canh_dai * self.chieu_cao

    def display(self):
        super().display()
        print(f"Cạnh dài: {self.canh_dai}, Cạnh ngắn: {self.canh_ngan}, Chiều cao: {self.chieu_cao}, Diện tích: {self.dien_tich()}")

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong)
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def display(self):
        super().display()
        print(f"Chiều dài: {self.chieu_dai}, Chiều rộng: {self.chieu_rong}, Diện tích: {self.dien_tich()}")

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)
        self.canh = canh

    def display(self):
        super().display()
        print(f"Cạnh: {self.canh}, Diện tích: {self.dien_tich()}")

# Tạo các đối tượng và hiển thị thông tin
print("Nhập thông tin cho hình bình hành:")
hinh_binh_hanh = HinhBinhHanh(5, 3)
hinh_binh_hanh.display()

print("\nNhập thông tin cho hình chữ nhật:")
hinh_chu_nhat = HinhChuNhat(4, 6)
hinh_chu_nhat.display()

print("\nNhập thông tin cho hình vuông:")
hinh_vuong = HinhVuong(5)
hinh_vuong.display()
