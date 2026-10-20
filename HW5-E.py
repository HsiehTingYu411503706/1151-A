# 讀取輸入的非負整數 n
n = int(input())

# 處理 n 等於 0 或 1 的特殊情況
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    # 初始化前兩項的值
    a = 0  # F(0)
    b = 1  # F(1)
    
    # 使用 for 迴圈從第 2 項計算到第 n 項
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
        
    # 輸出第 n 項的值
    print(b)