import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  idx = 0
  # 1. 讀取菜單
  M = int(input_data[idx])
  idx += 1

  drink_names = []
  drink_prices = []
  drink_counts = []

  for _ in range(M):
    drink_names.append(input_data[idx])
    drink_prices.append(int(input_data[idx + 1]))
    drink_counts.append(0)
    idx += 2

  # 2. 讀取訂單
  N = int(input_data[idx])
  idx += 1

  student_names = []
  student_bills = []  # 儲存每位學生各筆訂單的金額，或者直接對應商品累計

  # 為了記錄每個學生的訂單明細，我們可以用二維或平行串列記錄
  # 記錄每位學生購買各飲料的數量：student_quantities[student_idx][drink_idx]
  student_quantities = []

  for _ in range(N):
    s_name = input_data[idx]
    d_name = input_data[idx + 1]
    qty = int(input_data[idx + 2])
    idx += 3

    # 尋找或新增學生
    if s_name not in student_names:
      student_names.append(s_name)
      # 初始化該學生對所有飲料的購買量為 0
      student_quantities.append([0] * M)

    s_idx = student_names.index(s_name)
    d_idx = drink_names.index(d_name)

    # 累計該飲料總杯數
    drink_counts[d_idx] += qty
    # 累計該學生該飲料的購買量
    student_quantities[s_idx][d_idx] += qty

  # 3. 計算每種飲料優惠後的單價
  actual_prices = []
  for i in range(M):
    if drink_counts[i] >= 10:
      actual_prices.append(drink_prices[i] - 5)
    else:
      actual_prices.append(drink_prices[i])

  # 4. 輸出 DRINK 統計
  for i in range(M):
    print(f"DRINK {drink_names[i]} {drink_counts[i]}")

  # 5. 計算每位同學應付金額並輸出
  total_class_amount = 0
  for s_idx in range(N):  # 這裡用安全範圍或 len(student_names)
    pass  # 下方改用 len(student_names)

  for s_idx in range(len(student_names)):
    s_amount = 0
    for d_idx in range(M):
      s_amount += student_quantities[s_idx][d_idx] * actual_prices[d_idx]

    total_class_amount += s_amount
    print(f"STUDENT {student_names[s_idx]} {s_amount}")

  # 6. 輸出全班總額
  print(f"TOTAL {total_class_amount}")


if __name__ == "__main__":
  solve()