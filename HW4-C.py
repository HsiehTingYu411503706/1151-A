# 讀取一行包含三個以空白分隔的整數 a、b、c
a, b, c = map(int, input().split())

# 利用條件判斷找出最大值（不使用 max 函數）
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)