# 讀取輸入的非負整數 n
n = int(input())

# 初始化階乘結果變數為 1 (符合 0! = 1 的定義)
factorial = 1

# 使用 for 迴圈從 1 累乘到 n
for i in range(1, n + 1):
    factorial *= i

# 輸出階乘結果
print(factorial)