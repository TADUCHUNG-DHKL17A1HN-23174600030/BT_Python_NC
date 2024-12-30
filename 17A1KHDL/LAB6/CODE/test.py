import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Khởi tạo cơ sở dữ liệu SQLite
def khoi_tao_co_so_du_lieu():
    ket_noi = sqlite3.connect("sanpham.db")
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS sanpham (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten TEXT NOT NULL,
            gia REAL NOT NULL,
            soluong INTEGER NOT NULL
        )
    """)
    ket_noi.commit()
    ket_noi.close()

# Hàm thêm sản phẩm
def them_san_pham():
    ten = o_nhap_ten.get()
    gia = o_nhap_gia.get()
    soluong = o_nhap_soluong.get()
    if not ten or not gia or not soluong:
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")
        return
    try:
        ket_noi = sqlite3.connect("sanpham.db")
        con_tro = ket_noi.cursor()
        con_tro.execute("INSERT INTO sanpham (ten, gia, soluong) VALUES (?, ?, ?)", (ten, float(gia), int(soluong)))
        ket_noi.commit()
        ket_noi.close()
        messagebox.showinfo("Thành công", "Đã thêm sản phẩm")
        tai_danh_sach_san_pham()
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# Hàm tải danh sách sản phẩm
def tai_danh_sach_san_pham():
    for item in bang_sanpham.get_children():
        bang_sanpham.delete(item)
    ket_noi = sqlite3.connect("sanpham.db")
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT * FROM sanpham")
    for hang in con_tro.fetchall():
        bang_sanpham.insert("", "end", values=hang)
    ket_noi.close()

# Hàm xóa sản phẩm
def xoa_san_pham():
    muc_duoc_chon = bang_sanpham.selection()
    if not muc_duoc_chon:
        messagebox.showerror("Lỗi", "Vui lòng chọn sản phẩm để xóa")
        return
    ma_san_pham = bang_sanpham.item(muc_duoc_chon)["values"][0]
    ket_noi = sqlite3.connect("sanpham.db")
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM sanpham WHERE id = ?", (ma_san_pham,))
    ket_noi.commit()
    ket_noi.close()
    messagebox.showinfo("Thành công", "Đã xóa sản phẩm")
    tai_danh_sach_san_pham()

# Tạo giao diện chính
ung_dung = tk.Tk()
ung_dung.title("Quản lý sản phẩm")

# Khung nhập liệu
khung_nhap_lieu = tk.Frame(ung_dung)
khung_nhap_lieu.pack(pady=10)

tk.Label(khung_nhap_lieu, text="Tên sản phẩm:").grid(row=0, column=0, padx=5, pady=5)
o_nhap_ten = tk.Entry(khung_nhap_lieu)
o_nhap_ten.grid(row=0, column=1, padx=5, pady=5)

tk.Label(khung_nhap_lieu, text="Giá:").grid(row=1, column=0, padx=5, pady=5)
o_nhap_gia = tk.Entry(khung_nhap_lieu)
o_nhap_gia.grid(row=1, column=1, padx=5, pady=5)

tk.Label(khung_nhap_lieu, text="Số lượng:").grid(row=2, column=0, padx=5, pady=5)
o_nhap_soluong = tk.Entry(khung_nhap_lieu)
o_nhap_soluong.grid(row=2, column=1, padx=5, pady=5)

# Khung nút chức năng
khung_nut = tk.Frame(ung_dung)
khung_nut.pack(pady=10)

nut_them = tk.Button(khung_nut, text="Thêm sản phẩm", command=them_san_pham)
nut_them.grid(row=0, column=0, padx=10)

nut_xoa = tk.Button(khung_nut, text="Xóa sản phẩm", command=xoa_san_pham)
nut_xoa.grid(row=0, column=1, padx=10)

# Bảng danh sách sản phẩm
bang_sanpham = ttk.Treeview(ung_dung, columns=("ID", "Tên sản phẩm", "Giá", "Số lượng"), show="headings")
bang_sanpham.heading("ID", text="ID")
bang_sanpham.heading("Tên sản phẩm", text="Tên sản phẩm")
bang_sanpham.heading("Giá", text="Giá")
bang_sanpham.heading("Số lượng", text="Số lượng")
bang_sanpham.pack(pady=10)

# Khởi tạo cơ sở dữ liệu và tải danh sách sản phẩm
khoi_tao_co_so_du_lieu()
tai_danh_sach_san_pham()

# Khởi chạy ứng dụng
ung_dung.mainloop()

