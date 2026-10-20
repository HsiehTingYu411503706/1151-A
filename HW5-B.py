# 讀取輸入的起點 a、終點 b、正整數 k
a, b, k = map(int, input().split())

# 初始化個數與總和變數
count = 0
total = 0

# 使用 for 迴圈走訪從 a 到 b 的所有整數
for i in range(a, b + 1):
    # 判斷是否為 k 的倍數 (即除以 k 的餘數為 0)
    if i % k == 0:
        count += 1
        total += i

# 輸出個數與總和，以空白分隔
print(count, total)