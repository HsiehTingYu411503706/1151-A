# 讀取第一行 x1, y1
x1, y1 = map(int, input().split())

# 讀取第二行 x2, y2
x2, y2 = map(int, input().split())

# 計算座標差
dx = x2 - x1
dy = y2 - y1

# 計算距離平方並輸出
distance_squared = dx * dx + dy * dy
print(distance_squared)