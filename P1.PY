cities = ["Taipei", "Taichung","Tainan"]

data = []

for i in range(3):
    row = []
    for j in range(5):
        row.append(float(input()))
    data.append(row)

tc_data = data[1]
print(f'{sum(tc_data)/len(tc_data):.3f}')
#星期四溫度最高的城市? 溫度多少?
#(輸出格式:{city}:{溫度} 無空白)

idx = 3
max_row_idx = -1
max_temp = 0
for i in range(len(data)):
    temper = data[i][idx]
    if temper > max_temp:
        max_temp = temper
        max_row_idx = i

#參考寫法#
for i,row in enumerate(data):
    temper = row[idx]
    if temper > max_temp:
        max_temp = temper
        max_row_idx = i 

print(f'{cities[max_row_idx]}:{max_temp:.1f}')
 
#計算三個城市五天的平均溫度，輸出平均溫度最高的城市名
max_row_idx = -1
max_temp = 0
for i, row in enumerate(data):
    temper = sum(row)/len(row)
    if temper > max_temp:
        max_temp = temper
        max_row_idx = i

print(cities[max_row_idx])