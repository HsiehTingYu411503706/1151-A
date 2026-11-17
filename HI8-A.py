def main():
    import sys
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    idx = 0
    # 1. 讀取初始歌曲數量 N
    N = int(input_data[idx].strip())
    idx += 1

    # 2. 讀取初始播放清單
    playlist = []
    if N > 0 and idx < len(input_data) and input_data[idx].strip() != "":
        playlist = input_data[idx].strip().split()
    idx += 1

    # 3. 讀取指令數量 Q
    if idx < len(input_data):
        Q = int(input_data[idx].strip())
        idx += 1
    else:
        Q = 0

    # 4. 依序執行 Q 個指令
    for _ in range(Q):
        if idx >= len(input_data):
            break
        line = input_data[idx].strip()
        idx += 1
        if not line:
            continue

        parts = line.split()
        cmd = parts[0]

        if cmd == "ADD":
            song = parts[1]
            playlist.append(song)
        elif cmd == "REMOVE":
            song = parts[1]
            if song in playlist:
                playlist.remove(song)  # 題目指定：刪除從前後算第一個同名歌曲
        elif cmd == "REVERSE":
            playlist.reverse()

    # 5. 輸出結果
    print(len(playlist))
    if not playlist:
        print("EMPTY")
    else:
        print(" ".join(playlist))

if __name__ == '__main__':
    main()