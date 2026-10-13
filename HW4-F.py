# 讀取一行包含三個以空白分隔的正整數，並轉換為串列後排序
sides = sorted(list(map(int, input().split())))
a, b, c = sides[0], sides[1], sides[2]

# 判斷是否能組成三角形 (任意兩邊長之和嚴格大於第三邊，因為已排序所以檢查 a + b > c 即可)
if a + b <= c:
    print("Invalid")
elif a == b and b == c:
    print("Equilateral")
elif a == b or b == c:
    print("Isosceles")
else:
    print("Scalene")