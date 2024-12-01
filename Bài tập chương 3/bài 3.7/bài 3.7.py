import numpy as np

# 1. Đọc dữ liệu từ tập tin baseball_2D.txt
with open('Bài tập chương 3\baseball_2D.txt',encoding='utf-8-sig', mode='r') as file:
    baseball = [list(map(float, line.strip().split())) for line in file]

# Tạo 2D numpy array từ danh sách baseball
np_baseball = np.array(baseball)

# Kiểm tra kiểu dữ liệu và kích thước của np_baseball
print("Kiểu dữ liệu:", np_baseball.dtype)
print("Kích thước:", np_baseball.shape)

# 2. In các giá trị của dòng thứ 50 trong np_baseball
print("\nGiá trị của dòng thứ 50:", np_baseball[49])

# 3. Tạo numpy array np_weight với dữ liệu từ cột thứ hai
np_weight = np_baseball[:, 1]

# 4. Cho biết chiều cao của vận động viên thứ 124
chieu_cao_vdv_124 = np_baseball[123, 0]
print("\nChiều cao của vận động viên thứ 124:", chieu_cao_vdv_124)

# 5. Tính chiều cao trung bình và cân nặng trung bình
chieu_cao_trung_binh = np.mean(np_baseball[:, 0])
can_nang_trung_binh = np.mean(np_weight)

print("\nChiều cao trung bình:", chieu_cao_trung_binh)
print("Cân nặng trung bình:", can_nang_trung_binh)

# 6. Nhận xét về mối tương quan giữa chiều cao và cân nặng
correlation = np.corrcoef(np_baseball[:, 0], np_weight)[0, 1]
if correlation > 0:
    print("\nCó mối tương quan thuận giữa chiều cao và cân nặng.")
elif correlation < 0:
    print("\nCó mối tương quan nghịch giữa chiều cao và cân nặng.")
else:
    print("\nKhông có mối tương quan giữa chiều cao và cân nặng.")
