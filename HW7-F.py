def best_total(prices, index, remaining):
    """使用純遞迴探索 0/1 背包問題的選擇"""
    # 基礎情況：如果已經考慮完所有商品，或是預算剛好歸零，則無法再花費更多
    if index == len(prices) or remaining == 0:
        return 0
    
    # 分支 1：不選目前商品（直接跳到下一個商品）
    skip = best_total(prices, index + 1, remaining)
    
    # 分支 2：若買得起則選目前商品
    take = 0
    if prices[index] <= remaining:
        take = prices[index] + best_total(prices, index + 1, remaining - prices[index])
        
    # 回傳兩者中的最大值
    if skip > take:
        return skip
    else:
        return take

def main():
    import sys
    # 讀取所有標準輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    B = int(input_data[1])
    
    # 依商品順序讀取價格串列（不可排序、不可去重）
    prices = []
    for i in range(2, 2 + N):
        prices.append(int(input_data[i]))
        
    # 呼叫題目規定的遞迴函數
    ans = best_total(prices, 0, B)
    
    # 輸出結果
    print(ans)

if __name__ == '__main__':
    main()