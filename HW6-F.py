import sys


def solve():
  # 讀取所有輸入，保留第二行的空白與換行格式
  lines = sys.stdin.readlines()
  if not lines:
    return

  # 第一行為 K
  K = int(lines[0].strip())

  # 第二行為原始訊息 S（可能包含結尾的換行符號，需透過切片或 rstrip 保留原貌）
  # 題目說明第二行長度不計換行，但 sys.stdin.readlines 會讀入換行符號
  S = lines[1]
  if S.endswith("\n"):
    S = S[:-1]
  if S.endswith("\r"):
    S = S[:-1]

  encrypted_chars = []

  for char in S:
    code = ord(char)
    # 檢查是否為大寫字母 (A-Z: 65 ~ 90)
    if 65 <= code <= 90:
      new_code = 65 + (code - 65 + K) % 26
      encrypted_chars.append(chr(new_code))
    # 檢查是否為小寫字母 (a-z: 97 ~ 122)
    elif 97 <= code <= 122:
      new_code = 97 + (code - 97 + K) % 26
      encrypted_chars.append(chr(new_code))
    else:
      # 非英文字母保持原樣
      encrypted_chars.append(char)

  # 組合並輸出結果，最後加上換行
  print("".join(encrypted_chars))


if __name__ == "__main__":
  solve()