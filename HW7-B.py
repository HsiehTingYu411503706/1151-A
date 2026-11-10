def is_prime(n):
    """判斷 n 是否為質數的函數"""
    # 0 與 1 不是質數
    if n <= 1:
        return False
    
    # 檢查從 2 開始，到平方不大於 n 的範圍 (i * i <= n)
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
        
    return True

def main():
    # 讀取輸入的一行：L 與 R
    L, R = map(int, input().split())
    
    primes = []
    
    # 在主程式中對區間內每個整數呼叫 is_prime(n)
    for num in range(L, R + 1):
        if is_prime(num):
            primes.append(num)
            
    # 輸出結果
    if len(primes) == 0:
        print("NONE")
        print("0 0")
    else:
        # 第一行：輸出所有質數，以空白分隔
        print(*(primes))
        # 第二行：輸出質數個數與總和，以空白分隔
        print(f"{len(primes)} {sum(primes)}")

if __name__ == '__main__':
    main()