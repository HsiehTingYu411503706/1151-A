# 讀取停車時數 h
h = int(input())

# 計算總停車費
fee = 0
if h <= 2:
    fee = h * 30
elif h <= 5:
    fee = 2 * 30 + (h - 2) * 20
else:
    fee = 2 * 30 + 3 * 20 + (h - 5) * 10

# 輸出總金額
print(fee)