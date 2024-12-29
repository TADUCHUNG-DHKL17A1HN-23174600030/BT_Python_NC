import sqlite3

# Kết nối hoặc tạo cơ sở dữ liệu
conn = sqlite3.connect('17A1KHDL\LAB4\DATA\product.db')
cursor = conn.cursor()

# Tạo bảng product nếu chưa tồn tại
cursor.execute('''
CREATE TABLE IF NOT EXISTS product (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    Amount INTEGER NOT NULL
)
''')

conn.commit()
conn.close()


import sqlite3

# Hàm kết nối cơ sở dữ liệu
def ket_noi_csdl():
    return sqlite3.connect('17A1KHDL\LAB4\DATA\product.db')
    

# 1. Hiển thị danh sách sản phẩm
def hien_thi_san_pham():
    conn = ket_noi_csdl()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM product')
    rows = cursor.fetchall()
    if rows:
        print(f"{'ID':<5}{'Tên sản phẩm':<20}{'Giá':<10}{'Số lượng':<10}")
        print("-" * 50)
        for row in rows:
            print(f"{row[0]:<5}{row[1]:<20}{row[2]:<10}{row[3]:<10}")
    else:
        print("Không có sản phẩm nào trong cơ sở dữ liệu.")
    conn.close()

# 2. Thêm sản phẩm mới
def them_san_pham():
    ten = input("Nhập tên sản phẩm: ")
    gia = float(input("Nhập giá sản phẩm: "))
    so_luong = int(input("Nhập số lượng sản phẩm: "))

    conn = ket_noi_csdl()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)', (ten, gia, so_luong))
    conn.commit()
    conn.close()
    print("Sản phẩm đã được thêm thành công.")

# 3. Tìm kiếm sản phẩm theo tên
def tim_kiem_san_pham():
    ten = input("Nhập tên sản phẩm cần tìm: ")
    conn = ket_noi_csdl()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM product WHERE Name LIKE ?', ('%' + ten + '%',))
    rows = cursor.fetchall()
    if rows:
        print(f"{'ID':<5}{'Tên sản phẩm':<20}{'Giá':<10}{'Số lượng':<10}")
        print("-" * 50)
        for row in rows:
            print(f"{row[0]:<5}{row[1]:<20}{row[2]:<10}{row[3]:<10}")
    else:
        print("Không tìm thấy sản phẩm phù hợp.")
    conn.close()

# 4. Cập nhật thông tin sản phẩm
def cap_nhat_san_pham():
    ma_san_pham = int(input("Nhập ID sản phẩm cần cập nhật: "))
    gia_moi = float(input("Nhập giá mới: "))
    so_luong_moi = int(input("Nhập số lượng mới: "))

    conn = ket_noi_csdl()
    cursor = conn.cursor()
    cursor.execute('UPDATE product SET Price = ?, Amount = ? WHERE Id = ?', (gia_moi, so_luong_moi, ma_san_pham))
    if cursor.rowcount > 0:
        print("Cập nhật sản phẩm thành công.")
    else:
        print("Không tìm thấy sản phẩm với ID đã nhập.")
    conn.commit()
    conn.close()

# 5. Xóa sản phẩm
def xoa_san_pham():
    ma_san_pham = int(input("Nhập ID sản phẩm cần xóa: "))
    conn = ket_noi_csdl()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM product WHERE Id = ?', (ma_san_pham,))
    if cursor.rowcount > 0:
        print("Sản phẩm đã được xóa thành công.")
    else:
        print("Không tìm thấy sản phẩm với ID đã nhập.")
    conn.commit()
    conn.close()

# Menu chính
def menu_chinh():
    while True:
        print("\n=== Quản Lý Sản Phẩm ===")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Tìm kiếm sản phẩm theo tên")
        print("4. Cập nhật thông tin sản phẩm")
        print("5. Xóa sản phẩm")
        print("6. Thoát")
        lua_chon = input("Chọn chức năng (1-6): ")

        if lua_chon == '1':
            hien_thi_san_pham()
        elif lua_chon == '2':
            them_san_pham()
        elif lua_chon == '3':
            tim_kiem_san_pham()
        elif lua_chon == '4':
            cap_nhat_san_pham()
        elif lua_chon == '5':
            xoa_san_pham()
        elif lua_chon == '6':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


menu_chinh()