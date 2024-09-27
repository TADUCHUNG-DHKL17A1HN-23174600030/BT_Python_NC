class TS:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm Toán: "))
        self.diem_ly = float(input("Nhập điểm Lý: "))
        self.diem_hoa = float(input("Nhập điểm Hóa: "))

    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}, Điểm Toán: {self.diem_toan}, Điểm Lý: {self.diem_ly}, Điểm Hóa: {self.diem_hoa}")

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

def sap_xep_tu_cao_xuong(thi_sinh_list):
    for i in range(len(thi_sinh_list)):
        for j in range(len(thi_sinh_list) - 1):
            if thi_sinh_list[j].tinh_tong_diem() < thi_sinh_list[j + 1].tinh_tong_diem():
                thi_sinh_list[j], thi_sinh_list[j + 1] = thi_sinh_list[j + 1], thi_sinh_list[j]

def main():
    danh_sach_thi_sinh = []
    so_luong = int(input("Nhập số lượng thí sinh: "))

    for _ in range(so_luong):
        thí_sinh = TS("", 0, 0, 0)
        thí_sinh.nhap_thong_tin()
        danh_sach_thi_sinh.append(thí_sinh)

    # Điểm chuẩn
    diem_chuan = 20

    # Lọc danh sách thí sinh trúng tuyển
    thí_sinh_trúng_tuyen = [ts for ts in danh_sach_thi_sinh if ts.tinh_tong_diem() >= diem_chuan]

    # Sắp xếp theo điểm từ cao xuống thấp
    sap_xep_tu_cao_xuong(thí_sinh_trúng_tuyen)

    # In danh sách thí sinh trúng tuyển
    print("\nDanh sách thí sinh trúng tuyển:")
    for ts in thí_sinh_trúng_tuyen:
        ts.in_thong_tin()
        print(f"Tổng điểm: {ts.tinh_tong_diem()}")


    main()
