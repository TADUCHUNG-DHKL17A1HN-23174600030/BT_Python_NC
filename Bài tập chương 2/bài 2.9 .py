import json

# Đây là một đối tượng Python (dictionary)
doi_tuong_python = {
    "ho_va_ten": "Nguyễn Văn A",
    "nam_sinh": 2004,
    "gioi_tinh": "Nam",
    "sdt": "0123456789",
    "email": "nguyenvana@uneti.edu.vn"
}

# Chuyển đổi đối tượng Python thành chuỗi JSON, sắp xếp theo từ khóa
json_data = json.dumps(doi_tuong_python, ensure_ascii=False, indent=4, sort_keys=True)

# Hiển thị chuỗi JSON với mức thụt lề 4
print(json_data)
