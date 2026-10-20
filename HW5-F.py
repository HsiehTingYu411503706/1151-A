# 讀取輸入的正整數 n
n = int(input())

# 使用外層 for 迴圈控制列數 i (從 1 到 n)
for i in range(1, n + 1):
    # 使用內層 for 迴圈控制欄數 j (從 1 到 n)
    for j in range(1, n + 1):
        # 計算乘積並以欄寬 4 靠右對齊輸出 (end="" 避免自動換行)
        print(f"{i * j:4d}", end="")
    # 每一列結束後輸出換行
    print()