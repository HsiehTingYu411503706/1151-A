import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  N = int(input_data[0])

  names = []
  subtotals = []

  idx = 1
  for _ in range(N):
    name = input_data[idx]
    price = int(input_data[idx + 1])
    quantity = int(input_data[idx + 2])
    idx += 3

    # 計算買 3 送 1 優惠後的付費件數
    # 每 3 件中有 2 件需要付費，未滿 3 件的部分正常計費
    paid_quantity = (quantity // 3) * 2 + (quantity % 3)
    subtotal = paid_quantity * price

    names.append(name)
    subtotals.append(subtotal)

  # 計算加總小計
  total_sum = sum(subtotals)

  # 合計滿 1000 元折 100 元（限折一次）
  if total_sum >= 1000:
    final_amount = total_sum - 100
  else:
    final_amount = total_sum

  # 找出小計最高的商品（若相同則取輸入較早者，即索引最小者）
  max_subtotal = -1
  top_name = ""
  for i in range(N):
    if subtotals[i] > max_subtotal:
      max_subtotal = subtotals[i]
      top_name = names[i]

  # 輸出前 N 行：商品名稱與優惠後小計
  for i in range(N):
    print(f"{names[i]} {subtotals[i]}")

  # 輸出總金額與最高花費商品
  print(f"TOTAL {final_amount}")
  print(f"TOP {top_name}")


if __name__ == "__main__":
  solve()