# 讀取輸入的目前存款 s、每天新增金額 d、目標金額 t
s, d, t = map(int, input().split())

# 初始化天數變數
days = 0

# 當存款小於目標金額時，持續增加天數與存款
while s < t:
    s += d
    days += 1

# 輸出最少天數
print(days)