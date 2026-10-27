import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  # 依照範例 1 輸入：1000 3 10 100 分別代表 B, N, R, C
  # 根據範例 1 的輸入對應：1000 (B), 3 (N), 10 (C), 100 (R)
  # 讀取順序：B, N, C, R
  B = int(input_data[0])
  N = int(input_data[1])
  C = int(input_data[2])
  R = int(input_data[3])

  # 計算服務費（整數運算，不足 1 元捨去）
  service_fee = (B * C) // 100

  # 計算應付總額 T
  T = B + service_fee - R
  if T < 0:
    T = 0

  # 計算每人基礎金額 q 與餘數 b
  q = T // N
  b = T % N
  a = N - b

  # 輸出結果
  print(T)
  print(f"{q} {a}")
  print(f"{q + 1} {b}")


if __name__ == "__main__":
  solve()