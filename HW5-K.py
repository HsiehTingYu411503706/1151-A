# 讀取輸入的正整數 a 與 b
a, b = map(int, input().split())

# 使用 while 迴圈進行輾轉相除法
while b != 0:
    r = a % b
    a = b
    b = r

# 當 b 為 0 時，a 即為最大公因數
print(a)