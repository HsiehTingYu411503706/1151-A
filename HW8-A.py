def main():
    import sys
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    # 讀取初始音樂數量 N
    N = int(input_data[0].strip())
    
    # 讀取初始播放清單（若 N=0 則清單為空）
    if N > 0 and len(input_data) > 1 and input_data[1].strip() != "":
        playlist = input_data[1].strip().split()
    else:
        playlist = []
        
    # 讀取指令數 Q
    # 尋找 Q 的位置（通常在第 3 行，若 N=0 則可能在不同行，故用尋找的方式較保險）
    # 根據題目格式：第一行 N，第二行 N個名稱，第三行 Q，接下來 Q 行指令
    line_idx = 2 if N > 0 else 1
    if line_idx < len(input_data):
        Q = int(input_data[line_idx].strip())
        line_idx += 1
    else:
        Q = 0

    # 依序執行 Q 個指令
    for _ in range(Q):
        if line_idx >= len(input_data):
            break
        cmd_line = input_data[line_idx].strip()
        line_idx += 1
        
        if not cmd_line:
            continue
            
        parts = cmd_line.split(maxsplit=1)
        op = parts[0]
        
        if op == "ADD":
            song = parts[1]
            playlist.append(song)
        elif op == "REMOVE":
            song = parts[1]
            if song in playlist:
                playlist.remove(song)
        elif op == "REVERSE":
            playlist.reverse()

    # 輸出結果
    final_count = len(playlist)
    print(final_count)
    if final_count > 0:
        print(" ".join(playlist))
    else:
        print("EMPTY")

if __name__ == '__main__':
    main()