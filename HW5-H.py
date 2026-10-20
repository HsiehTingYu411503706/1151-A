# 讀取輸入的非負整數 n
n = int(input())

# 初始化各位數總和變數
total_sum = 0

# 當 n 大於 0 時持續迴圈 (若 n 為 0 則不進入迴圈，總和保持 0)
while n > 0:
    # 取得目前個位數並累加到總和
    total_sum += n % 10
    # 去掉個位數
    n //= 10

# 輸出各位數總和
print(total_sum)