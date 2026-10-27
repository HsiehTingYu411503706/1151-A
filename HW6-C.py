import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  # 讀取每日目標 G 與 7 天步數
  G = int(input_data[0])
  steps = [int(x) for x in input_data[1:8]]

  # 1. 計算總步數
  total_steps = sum(steps)

  # 2. 計算達標天數
  # 3. 找出最高步數出現的所有日期 (1 ~ 7)
  # 4. 計算最長連續達標天數
  target_days_count = 0
  max_val = max(steps)
  max_days = []

  current_streak = 0
  max_streak = 0

  for i in range(7):
    day_num = i + 1
    s = steps[i]

    # 檢查是否達標
    if s >= G:
      target_days_count += 1
      current_streak += 1
    else:
      current_streak = 0

    # 更新最長連續達標
    if current_streak > max_streak:
      max_streak = current_streak

    # 檢查是否為最高步數
    if s == max_val:
      max_days.append(str(day_num))

  # 輸出四行結果
  print(total_steps)
  print(target_days_count)
  print(" ".join(max_days))
  print(max_streak)


if __name__ == "__main__":
  solve()