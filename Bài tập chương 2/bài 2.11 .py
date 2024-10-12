import json
from datetime import datetime

# hàm lấy thời gian theo định dạng ban đầu 
def lay_thoi_gian():
    return datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

# Hàm ghi dữ liệu vào json
def luu_du_lieu(du_lieu):
    tap_tin=f"{lay_thoi_gian().json}"
    with open("ten_tap_tin",'w') as file:
        json.dump(du_lieu,file,ensure_ascii=False,indent=4)
    print(f"giao dịch đã được lưu vào tập tin {tap_tin} ")

# Chương trinh quản lý
def quan_ly_giao_dich():
    danh_sach_giao_dich=[]
    while True:
        # Nhập thông tin vào tệp 
        so_tien=input("Số Tiền :")
        if so_tien.lower()=="Ext":
            break
    so_luong_vang=input("Số lượng vàng ")

    # Lưu giao dịch vào danh sách 
    giao_dich={
        "Số tiền":so_tien,
        "Số lượng vàng ":so_luong_vang,
    }    
    danh_sach_giao_dich.append(giao_dich)

    # Hiển thi danh sách giao dịch đã gặp
    print("\nDanh sách giao dichh")
    for i , gd in enumerate(danh_sach_giao_dich):
        print(f"Giao dịch {i} : {gd}")

    lua_chon = input("\nBạn có muốn lưu giao dịch vào tệp JSON? (1: Có, 0: Không): ")
    
    if lua_chon == '1':
        luu_du_lieu(danh_sach_giao_dich)
    else:
        print("Giao dịch không được lưu.")

quan_ly_giao_dich()

