def main():
    import sys
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    # 讀取跑者數 N
    N = int(input_data[0].strip())
    
    runners = []
    # 讀取 N 行跑者資料
    for i in range(1, N + 1):
        if i >= len(input_data):
            break
        parts = input_data[i].strip().split()
        if len(parts) >= 3:
            name = parts[0]
            time_val = int(parts[1])
            penalty_val = int(parts[2])
            
            # 限制要求：原始資料必須存為 tuple (name, time, penalty)，並用 list 收集
            runner_tuple = (name, time_val, penalty_val)
            runners.append(runner_tuple)

    # 排序 key：
    # 1. 總秒數 (time + penalty)
    # 2. 原始完賽秒數 (time)
    # 3. 姓名字母順序 (name)
    # 透過索引讀取 tuple，符合限制規定
    sorted_runners = sorted(
        runners, 
        key=lambda r: (r[1] + r[2], r[1], r[0])
    )

    # 輸出結果：每行輸出跑者姓名與總秒數，以一個空白分隔
    for r in sorted_runners:
        total_seconds = r[1] + r[2]
        print(f"{r[0]} {total_seconds}")

if __name__ == '__main__':
    main()
cite: 3