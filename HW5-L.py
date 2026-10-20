# 讀取輸入的非負整數金額 m
m = int(input())

# 初始化硬幣總數變數
coin_count = 0

# 當金額大於 0 時持續迴圈
while m > 0:
    # 根據題目規則依序判斷並扣除硬幣面額
    if m >= 50:
        m -= 50
    elif m >= 10:
        m -= 10
    elif m >= 5:
        m -= 5
    else:
        m -= 1
    # 每扣除一枚硬幣，硬幣總數加 1
    coin_count += 1

# 輸出最少硬幣數 (若 m 為 0 則不進入迴圈，輸出 0)
print(coin_count)