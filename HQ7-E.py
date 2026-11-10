def count_ways(step, n, blocked, memo):
    # 若超過目標階梯，則此路不通
    if step > n:
        return 0
    # 若剛好到達目標階梯，回傳 1 種走法
    if step == n:
        return 1
    # 若目前踩在損壞的階梯上，則此路不通
    if blocked[step]:
        return 0
    # 若該狀態已經計算過，直接回傳記憶結果
    if memo[step] != -1:
        return memo[step]
    
    # 遞迴計算走 1 步與走 2 步的走法總和
    ways = count_ways(step + 1, n, blocked, memo) + count_ways(step + 2, n, blocked, memo)
    memo[step] = ways
    return ways

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    # 建立長度為 n+1 的布林陣列紀錄損壞階梯（地面 0 不會損壞）
    blocked = [False] * (n + 1)
    if k > 0:
        for i in range(2, 2 + k):
            b_idx = int(input_data[i])
            blocked[b_idx] = True
            
    # 建立長度為 n+1 的記憶陣列，初值皆為 -1
    memo = [-1] * (n + 1)
    
    # 若終點本身損壞，直接輸出 0
    if blocked[n]:
        print(0)
    else:
        result = count_ways(0, n, blocked, memo)
        print(result)

if __name__ == '__main__':
    main()