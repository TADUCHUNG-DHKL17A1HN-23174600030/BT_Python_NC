import pandas as pd

# Đọc dữ liệu từ file euro2012.csv
euro12 = pd.read_csv('euro2012.csv')

# In thông tin về DataFrame euro12
print("Loại dữ liệu:", type(euro12))
print("Kích thước:", euro12.shape)
print("Danh sách các cột:", euro12.columns.tolist())

# 1. In giá trị cột Goals
print("\nGiá trị cột Goals:")
print(euro12['Goals'])

# 2. Số đội tham gia Euro 2012
so_doi = euro12['Team'].nunique()
print("\nSố đội tham gia Euro 2012:", so_doi)

# 3. In cột Team
print("\nCột Team:")
print(euro12['Team'])

# 4. Tạo DataFrame mới discipline chỉ chứa 3 cột
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print("\nDataFrame discipline:")
print(discipline)

# 5. Hiển thị các đội có 2 cột 'Red Cards', 'Yellow Cards'
print("\nĐội có số thẻ đỏ và thẻ vàng:")
print(euro12[['Team', 'Red Cards', 'Yellow Cards']])

# 6. a) Tính trung bình Yellow Cards
trung_binh_yellow = euro12['Yellow Cards'].mean()
print("\nTrung bình Yellow Cards:", trung_binh_yellow)

# b) Lọc các đội đã ghi bàn hơn 6 bàn thắng
doi_hon_6_ban = euro12[euro12['Goals'] > 6]
print("\nCác đội ghi bàn hơn 6 bàn thắng:")
print(doi_hon_6_ban[['Team', 'Goals']])

# c) Các đội có tên bắt đầu bằng 'G'
doi_bat_dau_bang_G = euro12[euro12['Team'].str.startswith('G')]
print("\nCác đội có tên bắt đầu bằng 'G':")
print(doi_bat_dau_bang_G['Team'])

# 7. In 7 cột đầu của euro12
print("\n7 cột đầu của euro12:")
print(euro12.iloc[:, :7])

# 8. In tất cả các cột, trừ 3 cột cuối
print("\nTất cả các cột, trừ 3 cột cuối:")
print(euro12.iloc[:, :-3])

# 9. In các cột: Team, Goals, Shooting Accuracy, Yellow Cards, Red Cards
print("\nCác cột: Team, Goals, Shooting Accuracy, Yellow Cards, Red Cards:")
print(euro12[['Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards']])

# 10. In các cột chỉ hiển thị 'Team', 'Shooting Accuracy' từ 'England', 'Italy', 'Russia'
doi_cua_England_Italy_Russia = euro12[euro12['Team'].isin(['England', 'Italy', 'Russia'])]
print("\nCột 'Team', 'Shooting Accuracy' từ 'England', 'Italy', 'Russia':")
print(doi_cua_England_Italy_Russia[['Team', 'Shooting Accuracy']])
