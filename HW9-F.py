a, b = map(int, input().split())
start = min(a, b)
end = max(a, b)

primes = []
for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for d in range(2, int(num ** 0.5) + 1):
            if num % d == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))

print(" ".join(primes))