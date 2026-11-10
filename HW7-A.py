def parking_fee(minutes):
    """計算單筆停車費用的函數"""
    if minutes == 0:
        return 0
    
    # 計算 30 分鐘區間數（不足 30 分鐘進位，可用數學技巧：(minutes + 29) // 30）
    intervals = (minutes + 29) // 30
    fee = intervals * 30
    
    # 費率上限為 200 元
    if fee > 200:
        fee = 200
        
    return fee

def main():
    # 讀取紀錄數 N
    N = int(input())
    # 讀取 N 個停車分鐘數
    minutes_list = list(map(int, input().split()))
    
    # 計算每輛車的費用
    fees = [parking_fee(m) for m in minutes_list]
    
    # 計算總和
    total_revenue = sum(fees)
    
    # 輸出第一行：各車費用（以空白分隔）
    print(*(fees))
    # 輸出第二行：費用總和
    print(total_revenue)

if __name__ == '__main__':
    main()