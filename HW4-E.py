# 讀取一行包含三個以空白分隔的整數 a、b、c
a, b, c = map(int, input().split())

# 計算判別式 D = b^2 - 4 * a * c
D = b * b - 4 * a * c

# 根據 D 的值判斷並輸出相異實根個數
if D > 0:
    print(2)
elif D == 0:
    print(1)
else:
    print(0)