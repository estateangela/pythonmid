c = int(input())
a = list(c) # 將輸入的文字轉換成串列
while c < 0:
    break
b = a[::-1]          # 反轉串列
output = ''.join(b)  # 組合串列內容

print(int(output))

