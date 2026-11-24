keys = list(map(int, input().split()))
cipher = input()
l = len(keys)

result = []
idx = 0  # 只計算英文字母的位置

for ch in cipher:
    shift = -keys[idx % l]
    if 'A' <= ch <= 'Z':
        base = ord('A')
        new_ch = chr((ord(ch) - base + shift) % 26 + base)
        result.append(new_ch)
        idx += 1
    elif 'a' <= ch <= 'z':
        base = ord('a')
        new_ch = chr((ord(ch) - base + shift) % 26 + base)
        result.append(new_ch)
        idx += 1
    else:
        result.append(ch)

print("".join(result))