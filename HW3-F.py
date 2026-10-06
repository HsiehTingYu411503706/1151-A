# 讀取 2x2 矩陣
A = [list(map(int, input().split())) for _ in range(2)]
a, b = A[0]
c, d = A[1]

det = a * d - b * c

# 計算反矩陣
inv_a = d / det
inv_b = -b / det
inv_c = -c / det
inv_d = a / det

# 輸出四捨五入至 4 位小數
for row in ((inv_a, inv_b), (inv_c, inv_d)):
    print(*[f"{value:.4f}" for value in row])