usage = int(input())

if usage <= 120:
    cost = usage * 2.10
elif usage <= 500:
    cost = 120 * 2.10 + (usage - 120) * 3.02
else:
    cost = 120 * 2.10 + (500 - 120) * 3.02 + (usage - 500) * 4.39

print(f"NT${cost:.1f}")