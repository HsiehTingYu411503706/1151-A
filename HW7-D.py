def gcd(a, b):
    """使用遞迴輾轉相除法計算最大公因數"""
    if b == 0:
        return a
    return gcd(b, a % b)

def simplify_recipe(tea, milk, syrup):
    """計算三數的最大公因數，並回傳化簡後的比例值"""
    # 找出三個數中非零的值，先對前兩個數求 gcd，再與第三個數求 gcd
    # 由於題目保證每行至少有一個值大於 0，這樣處理安全且符合限制
    common_divisor = gcd(gcd(tea, milk), syrup)
    
    # 避免防呆（若 common_divisor 為 0 的極端情況，回傳原值，但題目保證至少一數大於 0）
    if common_divisor == 0:
        return tea, milk, syrup
        
    return tea // common_divisor, milk // common_divisor, syrup // common_divisor

def main():
    import sys
    # 讀取全部輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # 第一個數字為 N
    N = int(input_data[0])
    
    index = 1
    for _ in range(N):
        tea = int(input_data[index])
        milk = int(input_data[index + 1])
        syrup = int(input_data[index + 2])
        index += 3
        
        # 呼叫題目要求的 simplify_recipe 函數
        t, m, s = simplify_recipe(tea, milk, syrup)
        
        # 輸出結果
        print(f"{t} {m} {s}")

if __name__ == '__main__':
    main()