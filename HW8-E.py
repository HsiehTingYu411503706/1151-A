def main():
    import sys
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    # 讀取紀錄數 N
    N = int(input_data[0].strip())
    
    # 1. 必須用 set 保存已出現的記錄並去重
    unique_records_set = set()
    
    line_idx = 1
    for _ in range(N):
        if line_idx >= len(input_data):
            break
        parts = input_data[line_idx].strip().split()
        if len(parts) >= 2:
            student = parts[0]
            booth = parts[1]
            
            # 2. 必須將每筆紀錄存成 tuple (student, booth)
            record_tuple = (student, booth)
            unique_records_set.add(record_tuple)
        line_idx += 1
        
    # 第一行輸出有效集章總數（即不重複的 (學生, 攤位) 組合數量）
    total_valid_stamps = len(unique_records_set)
    print(total_valid_stamps)
    
    # 3. 再以 dict 統計每人章數
    student_counts_dict = {}
    for record in unique_records_set:
        # 透過解包讀取 tuple
        student, booth = record
        if student in student_counts_dict:
            student_counts_dict[student] += 1
        else:
            student_counts_dict[student] = 1
            
    # 4. 最後以 list 儲存並透過排序建立排行榜
    # 排序規則：章數多者在前（降冪 -count），章數相同時姓名字母字典序較小者在前（升冪 name）
    ranking_list = []
    for student, count in student_counts_dict.items():
        ranking_list.append((student, count))
        
    # 使用 sorted 進行排序
    sorted_ranking = sorted(
        ranking_list, 
        key=lambda x: (-x[1], x[0])
    )
    
    # 輸出每位學生的姓名與章數
    for student, count in sorted_ranking:
        print(f"{student} {count}")

if __name__ == '__main__':
    main()
cite: 9