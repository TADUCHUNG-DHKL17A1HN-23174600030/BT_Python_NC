import requests

# URL API để lấy danh sách các bài post
url = "https://jsonplaceholder.typicode.com/posts"

# Gửi yêu cầu GET tới API
response = requests.get(url)

# Kiểm tra xem yêu cầu có thành công không
if response.status_code == 200:
    # Lấy dữ liệu JSON từ phản hồi
    posts = response.json()
    
    # Hiển thị tổng số bài post
    print(f"Tổng số bài post: {len(posts)}\n")
    
    # Hiển thị danh sách các bài post
    for post in posts:
        print(f"User ID: {post['userId']}")
        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("-" * 40)
else:
    print("Không thể lấy dữ liệu từ API. Mã lỗi:", response.status_code)