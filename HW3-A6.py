# 讀取矩陣 A
a, b = map(int, input().split())
c, d = map(int, input().split())

# 讀取矩陣 B
e, f = map(int, input().split())
g, h = map(int, input().split())

# 計算矩陣 C = A * B
c11 = a * e + b * g
c12 = a * f + b * h
c21 = c * e + d * g
c22 = c * f + d * h

# 輸出結果
print(f"{c11} {c12}")
print(f"{c21} {c22}")