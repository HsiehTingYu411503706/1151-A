# 讀取輸入的非負整數 n
n = int(input())

# 初始化反轉結果變數
reversed_num = 0

# 當 n 大於 0 時持續迴圈 (若 n 為 0 則不進入迴圈，結果保持 0)
while n > 0:
    # 取得目前的個位數
    digit = n % 10
    # 將累積的反轉結果乘以 10 並加上新的個位數
    reversed_num = reversed_num * 10 + digit
    # 去掉個位數
    n //= 10

# 輸出反轉後的整數
print(reversed_num)