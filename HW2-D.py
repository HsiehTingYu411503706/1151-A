# 一次讀取輸入的兩個整數 w 與 h
w, h = map(int, input().split())

# 計算面積與周長
area = w * h
perimeter = 2 * (w + h)

# 印出結果，中間用空格隔開
print(area, perimeter)