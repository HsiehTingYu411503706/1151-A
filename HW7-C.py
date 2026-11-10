def normalize(text):
    """將原始字串進行清理：只保留英文字母與數字，並將英文轉為小寫"""
    result = []
    for ch in text:
        # 檢查是否為英文大小寫或數字
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9'):
            result.append(ch.lower())
    return "".join(result)

def is_palindrome(text, left, right):
    """使用遞迴檢查字串在 left 到 right 範圍內是否為回文"""
    # 基礎情況：當左右指標相遇或交錯時，代表已比對完畢，是回文
    if left >= right:
        return True
    
    # 比較兩端的字元是否相同
    if text[left] != text[right]:
        return False
    
    # 遞迴縮小範圍，比較內側的字元
    return is_palindrome(text, left + 1, right - 1)

def main():
    import sys
    # 讀取整行（包含可能含有空格的輸入）
    line = sys.stdin.readline()
    if not line:
        return
    # 去除結尾的換行字元
    raw_text = line.rstrip('\r\n')
    
    # 1. 整理字串
    cleaned_text = normalize(raw_text)
    
    # 2. 判斷回文
    length = len(cleaned_text)
    if length <= 1:
        is_pali = True
    else:
        is_pali = is_palindrome(cleaned_text, 0, length - 1)
        
    # 3. 輸出結果
    if is_pali:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()