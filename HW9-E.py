original_n = input().strip()
current = original_n
step = 0

while True:
    step += 1
    digit_sum = sum(int(ch) for ch in current)
    print(f"Pass {step} : {digit_sum}")
    if digit_sum < 10:
        break
    current = str(digit_sum)

print(f"Digital Root of {original_n} : {digit_sum}")