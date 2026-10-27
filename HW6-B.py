import sys


def solve():
  # 讀取一整行（包含可能的空白與結尾換行）
  line = sys.stdin.readline()
  if not line:
    return
  # 移除結尾的換行符號（保留原始字串的頭尾空白供後續處理）
  s = line.rstrip("\r\n")

  # 1. 移除頭尾的半形空白
  s = s.strip(" ")

  # 2. 把英文字母轉成小寫
  s = s.lower()

  # 3. 將中間每一段連續半形空白改成一個底線
  # 使用 split() 會自動以任意連續空白分割字串，並過濾掉空字串
  parts = s.split(" ")
  # 過濾掉因為多個空白產生的空字串（若有需要），再用 "_" 連接
  filtered_parts = [p for p in parts if p != ""]
  formatted_s = "_".join(filtered_parts)

  # 4. 檢查是否合法
  is_valid = True
  length = len(formatted_s)

  # 檢查長度是否在 6 至 16 之間
  if length < 6 or length > 16:
    is_valid = False
  else:
    # 檢查每個字元是否只能是 a-z、0-9 或底線 '_'
    for char in formatted_s:
      if not (
          ("a" <= char <= "z") or ("0" <= char <= "9") or (char == "_")
      ):
        is_valid = False
        break

  # 輸出結果
  print(formatted_s)
  if is_valid:
    print("VALID")
  else:
    print("INVALID")


if __name__ == "__main__":
  solve()