import requests

# Địa chỉ API từ đề bài
url = 'https://jsonplaceholder.typicode.com/comments?postId=1'

# Gửi yêu cầu GET tới API
response = requests.get(url)

# Kiểm tra nếu kết nối thành công
if response.status_code == 200:
    # Lấy dữ liệu dưới dạng JSON
    data = response.json()

    # Hiển thị danh sách các bài post nổi bật
    print(f"Danh sách các bài post với postId = 1: \n")
    
    # Hiển thị thông tin của 3 bài post đầu tiên
    for i, post in enumerate(data[:3], 1):  # Chỉ hiển thị 3 bài đầu tiên
        print(f"Bài post {i}:")
        print(f"ID: {post['id']}")
        print(f"Name: {post['name']}")
        print(f"Email: {post['email']}")
        print(f"Body: {post['body']}")
        print("-" * 50)
else:
    print("Không thể kết nối tới API.")