# 讀取輸入的三位正整數 N
N = int(input())

# 取出百位、十位與個位數
a = N // 100
b = (N // 10) % 10
c = N % 10

# 計算各行輸出內容
line1 = f"{a} {b} {c}"
line2 = a + b + c
line3 = a * b * c
line4 = c * 100 + b * 10 + a

# 依序輸出 4 行結果
print(line1)
print(line2)
print(line3)
print(line4)