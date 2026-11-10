def count_ways(step, n, blocked, memo):
    """使用記憶化遞迴計算從目前 step 到達 n 的走法數"""
    # 1. 終點判斷：如果剛好走到目標 n，回傳 1（代表找到一種有效走法）
    if step == n:
        return 1
    
    # 2. 超出範圍判斷：如果走超過目標 n，回傳 0
    if step > n:
        return 0
    
    # 3. 損壞階梯判斷：如果踩到損壞的階梯，回傳 0
    if blocked[step]:
        return 0
    
    # 4. 記憶化檢查：如果已經計算過該位置的走法數，直接回傳
    if memo[step] != -1:
        return memo[step]
    
    # 5. 遞迴呼叫自身：分別處理再走 1 階與再走 2 階的情況
    ways_1 = count_ways(step + 1, n, blocked, memo)
    ways_2 = count_ways(step + 2, n, blocked, memo)
    
    # 6. 將結果儲存至 memo 中並回傳
    memo[step] = ways_1 + ways_2
    return memo[step]

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    
    # 建立 blocked 布林串列，長度為 N + 1，初值為 False
    blocked = [False] * (N + 1)
    
    # 如果有損壞階梯，將其標記為 True
    if K > 0:
        for i in range(2, 2 + K):
            bad_step = int(input_data[i])
            blocked[bad_step] = True
            
    # 建立 memo 記憶化串列，長度為 N + 1，初值皆為 -1
    memo = [-1] * (N + 1)
    
    # 呼叫題目規定的遞迴函數
    ans = count_ways(0, N, blocked, memo)
    
    # 輸出結果
    print(ans)

if __name__ == '__main__':
    main()