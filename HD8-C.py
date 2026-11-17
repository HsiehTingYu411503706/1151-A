def main():
    import sys
    input_data = sys.stdin.read().splitlines()
    if len(input_data) < 2:
        return

    # 讀取 A 社團與 B 社團的成員名單
    set_a = set(input_data[0].strip().split())
    set_b = set(input_data[1].strip().split())

    # 計算集合運算
    intersection_set = set_a & set_b  # 交集：皆參加兩個社團
    union_set = set_a | set_b        # 聯集：至少參加一個社團
    diff_a_b = set_a - set_b         # A 減 B：只參加 A 社團
    diff_b_a = set_b - set_a         # B 減 A：只參加 B 社團

    # 輸出處理輔助函式
    def format_output(s):
        if not s:
            return "NONE"
        # 依名稱排序並以空白分隔
        return " ".join(sorted(s))

    # 依序輸出四行：交集、聯集、A 減 B、B 減 A
    print(format_output(intersection_set))
    print(format_output(union_set))
    print(format_output(diff_a_b))
    print(format_output(diff_b_a))

if __name__ == '__main__':
    main()