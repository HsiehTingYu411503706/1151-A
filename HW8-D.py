def main():
    import sys
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    # 讀取初始商品數 N
    N = int(input_data[0].strip())
    
    # 解題限制：必須使用 dict 建立「商品名稱 -> 庫存數量」對應
    inventory = {}
    
    line_idx = 1
    # 讀取初始 N 行商品與庫存
    for _ in range(N):
        if line_idx >= len(input_data):
            break
        parts = input_data[line_idx].strip().split()
        if len(parts) >= 2:
            item = parts[0]
            stock = int(parts[1])
            inventory[item] = stock
        line_idx += 1
        
    # 讀取指令數 Q
    if line_idx < len(input_data):
        Q = int(input_data[line_idx].strip())
        line_idx += 1
    else:
        Q = 0
        
    total_sold_items = 0
    rejected_buy_count = 0
    
    # 依序處理 Q 個指令
    for _ in range(Q):
        if line_idx >= len(input_data):
            break
        cmd_line = input_data[line_idx].strip()
        line_idx += 1
        
        if not cmd_line:
            continue
            
        parts = cmd_line.split()
        op = parts[0]
        item = parts[1]
        qty = int(parts[2])
        
        if op == "ADD":
            # 增加庫存，若尚未登錄則新增
            if item in inventory:
                inventory[item] += qty
            else:
                inventory[item] = qty
        elif op == "BUY":
            # 只有商品存在且庫存足夠時才成交並扣除庫存，否則拒絕整筆
            if item in inventory and inventory[item] >= qty:
                inventory[item] -= qty
                total_sold_items += qty
            else:
                rejected_buy_count += 1

    # 第一行輸出成功售出總件數與被拒絕的購買筆數，以空白分隔
    print(f"{total_sold_items} {rejected_buy_count}")
    
    # 接著依商品名稱字典序，行輸出商品名稱與最後庫存（包含庫存為 0 者）
    for item in sorted(inventory.keys()):
        print(f"{item} {inventory[item]}")

if __name__ == '__main__':
    main()
cite: 7