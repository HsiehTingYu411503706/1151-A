# 讀取輸入的正整數 n
n = int(input())

# 初始化總和變數
total = 0

# 使用 for 迴圈從 1 累加到 n
for i in range(1, n + 1):
    total += i

# 輸出結果
print(total)