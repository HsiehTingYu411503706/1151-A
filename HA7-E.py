import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    N = int(next(iterator))
    K = int(next(iterator))

    blocked = [False] * (N + 1)
    for _ in range(K):
        bad_step = int(next(iterator))
        blocked[bad_step] = True

    memo = [-1] * (N + 1)
    ans = count_ways(0, N, blocked, memo)
    print(ans)