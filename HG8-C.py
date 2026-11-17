def main():
    import sys
    input_data = sys.stdin.read().splitlines()
    if len(input_data) < 3:
        return

    # 第一行是 N M，雖然我們可以用 set 自動去重，但讀取時要從第二行和第三行抓名單
    # 第二行是 A 社團的成員姓名
    set_a = set(input_data[1].strip().split())
    # 第三行是 B 社團的成員姓名
    set_b = set(input_data[2].strip().split())

    # 集合運算
    intersection_set = set_a & set_b  # 共同社團（交集）
    union_set = set_a | set_b        # 至少參加一個社團（聯集）
    diff_a_b = set_a - set_b         # 只參加 A 社團 (A 減 B)
    diff_b_a = set_b - set_a         # 只參加 B 社團 (B 減 A)

    # 輸出處理輔助函式
    def format_output(s):
        if not s:
            return "NONE"
        # 依字母順序排序並以空白分隔
        return " ".join(sorted(s))

    # 依照題目規定的順序輸出四行：交集、聯集、A 減 B、B 減 B(應為 B 減 A)
    print(format_output(intersection_set))
    print(format_output(union_set))
    print(format_output(diff_a_b))
    print(format_output(diff_b_a))

if __name__ == '__main__':
    main()