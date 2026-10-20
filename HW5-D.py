# 讀取學生人數 n
n = int(input())

# 讀取第二行的所有成績，並轉換為整數串列
scores = list(map(int, input().split()))

# 初始化總分、及格人數變數
total_score = 0
pass_count = 0

# 使用 for 迴圈逐筆累加總分並計算及格人數
for score in scores:
    total_score += score
    if score >= 60:
        pass_count += 1

# 計算平均分數
average = total_score / n

# 輸出平均分數（保留小數點後 2 位）與及格人數
print(f"{average:.2f}")
print(pass_count)