# 讀取一行包含兩個以空白分隔的整數 a 與 b
a, b = map(int, input().split())

# 根據題目規則進行判斷與輸出
if a > b:
    print("Greater")
elif a < b:
    print("Less")
else:
    print("Equal")