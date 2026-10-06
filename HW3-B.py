# 讀取輸入的總秒數 S
S = int(input())

# 計算小時、分鐘與秒數
hours = S // 3600
minutes = (S % 3600) // 60
seconds = S % 60

# 輸出結果，以空白分隔
print(f"{hours} {minutes} {seconds}")