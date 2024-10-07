import json

# Đây là một chuỗi JSON
json_data = '''
{
    "ho_va_ten": "Nguyễn Văn A",
    "nam_sinh": 2004,
    "gioi_tinh": "Nam",
    "sdt": "0123456789",
    "email": "nguyenvana@uneti.edu.vn"
}
'''

# Chuyển đổi chuỗi JSON thành đối tượng Python
doi_tuong_python = json.loads(json_data)

# Hiển thị đối tượng Python
print(doi_tuong_python)

# Kiểm tra kiểu dữ liệu
print(type(doi_tuong_python))

