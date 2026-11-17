def main():
    import sys
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    # 第一行讀取 N 與 M
    n_m = input_data[0].strip().split()
    N = int(n_m[0])
    M = int(n_m[1])
    
    # 讀取 A 社團名單（若 N=0 則為空白行或不存在）
    a_list = []
    if N > 0 and len(input_data) > 1 and input_data[1].strip() != "":
        a_list = input_data[1].strip().split()
        
    # 讀取 B 社團名單
    b_line_idx = 2 if N > 0 else 1
    b_list = []
    if M > 0 and b_line_idx < len(input_data) and input_data[b_line_idx].strip() != "":
        b_list = input_data[b_line_idx].strip().split()
        
    # 解題限制：必須將兩份名單轉成 set
    set_a = set(a_list)
    set_b = set(b_list)
    
    # 使用集合運算：交集、聯集、差集
    intersection_set = set_a & set_b  # 交集：共同成員[cite: 15]
    union_set = set_a | set_b         # 聯集：至少參加一個社團[cite: 15]
    diff_a_b = set_a - set_b          # A 減 B：只參加 A 社團[cite: 15]
    diff_b_a = set_b - set_a          # B 減 A：只參加 B 社團[cite: 15]
    
    # 輸出處理輔助函式
    def format_output(s):
        if not s:
            return "NONE"
        # 輸出前使用 sorted() 排序並以空白分隔[cite: 15]
        return " ".join(sorted(s))
        
    # 依序輸出四行：交集、聯集、A 減 B、B 減 A[cite: 15]
    print(format_output(intersection_set))
    print(format_output(union_set))
    print(format_output(diff_a_b))
    print(format_output(diff_b_a))

if __name__ == '__main__':
    main()
cite: 15