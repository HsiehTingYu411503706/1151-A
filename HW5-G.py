# 初始化總和變數
total = 0

# 使用 while 迴圈持續讀取輸入
while True:
    n = int(input())
    # 當讀到 0 時終止迴圈
    if n == 0:
        break
    # 將數值累加到總和
    total += n

# 輸出 0 之前的總和
print(total)