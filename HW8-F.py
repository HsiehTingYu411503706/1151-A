def main():
    import sys
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    # 讀取記錄數 N
    N = int(input_data[0].strip())
    
    # 1. 必須使用 list 保存輸入紀錄，每筆為 tuple (user, item)
    records_list = []
    
    line_idx = 1
    for _ in range(N):
        if line_idx >= len(input_data):
            break
        parts = input_data[line_idx].strip().split()
        if len(parts) >= 2:
            user = parts[0]
            item = parts[1]
            records_list.append((user, item))
        line_idx += 1
        
    # 最後一行讀取 target K
    target_k = 0
    if line_idx < len(input_data):
        target_parts = input_data[line_idx].strip().split()
        if len(target_parts) >= 2:
            target_user = target_parts[0]
            target_k = int(target_parts[1])
        elif len(target_parts) == 1:
            target_user = target_parts[0]
            
    # 2. 以 dict 將使用者對應到商品 set
    user_items_dict = {}
    for user, item in records_list:
        if user not in user_items_dict:
            user_items_dict[user] = set()
        user_items_dict[user].add(item)
        
    # 如果目標使用者不在記錄中，則沒有推薦商品
    if target_user not in user_items_dict:
        print(0)
        return
        
    target_items_set = user_items_dict[target_user]
    
    # 3. 透過交集判斷相似使用者（至少買過一件與目標相同的商品，且排除自己）
    similar_users = set()
    for other_user, items_set in user_items_dict.items():
        if other_user == target_user:
            continue
        # 交集運算判斷是否有共同購買商品
        intersection = target_items_set & items_set
        if len(intersection) > 0:
            similar_users.add(other_user)
            
    # 4. 以 dict 累計候選商品分數
    # 候選商品：相似使用者買過、但目標尚未買過的商品 (差集)
    recommendation_scores = {}
    for other_user in similar_users:
        other_items = user_items_dict[other_user]
        # 差集運算：other_items - target_items_set
        candidate_items = other_items - target_items_set
        for item in candidate_items:
            if item not in recommendation_scores:
                recommendation_scores[item] = 0
            recommendation_scores[item] += 1
            
    # 5. 以 list 排序結果
    recommendation_list = []
    for item, score in recommendation_scores.items():
        recommendation_list.append((item, score))
        
    # 排序規則：分數由大到小 (-score)，同分依商品名稱字元字典序排序 (item)
    sorted_recommendations = sorted(
        recommendation_list,
        key=lambda x: (-x[1], x[0])
    )
    
    # 計算實際推薦數量 R = min(K, 候選數)
    total_candidates = len(sorted_recommendations)
    R = min(target_k, total_candidates)
    
    # 輸出結果
    print(R)
    for i in range(R):
        item, score = sorted_recommendations[i]
        print(f"{item} {score}")

if __name__ == '__main__':
    main()
cite: 11