import json

# Đây là một đối tượng Python (dictionary)
doi_tuong_python = {
    "ho_va_ten": "Nguyễn Văn A",
    "nam_sinh": 2004,
    "gioi_tinh": "Nam",
    "sdt": "0123456789",
    "email": "nguyenvana@uneti.edu.vn"
}

# Chuyển đổi đối tượng Python thành chuỗi JSON
json_data = json.dumps(doi_tuong_python, ensure_ascii=False)

# Hiển thị chuỗi JSON
print(json_data)

# Kiểm tra kiểu dữ liệu
print(type(json_data))


