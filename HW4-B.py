# 讀取西元年份 y
y = int(input())

# 判斷閏年與平年規則
if y % 400 == 0:
    print("Leap")
elif y % 100 == 0:
    print("Common")
elif y % 4 == 0:
    print("Leap")
else:
    print("Common")