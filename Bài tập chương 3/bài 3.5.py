import codecs

height = []
weight = []

file_path_h = 'Bài tập chương 3/heights_1.txt'
file_path_w = 'D:/Python_Nângcao/TA_DUC_HUNG_DHKL17A1HN_23174600030/Bài tập chương 3/weights_1.txt'


with codecs.open(file_path_h, 'r', encoding='utf-8-sig') as file:
    for line in file:
        height.append(line.strip())

with codecs.open(file_path_w, 'r', encoding='utf-8-sig') as file:
    for line in file:
        weight.append(line.strip())

height_str = ','.join(height)
weight_str = ','.join(weight)

height = [int(x) for x in height_str.split(',')]
weight = [int(x) for x in weight_str.split(',')]

print(height)
print(weight)