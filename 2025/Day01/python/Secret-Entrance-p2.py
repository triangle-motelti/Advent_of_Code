#!/usr/bin/env python3
import sys

def counts(n):
    base = n // 5
    rem = n % 5
    cnt = [base] * 5

    for r in range(1, 5):
        if rem >= r:
            cnt[r] += 1
    return cnt

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n, m = map(int, data[:2])
    a = counts(n)
    b = counts(m)
    ans = sum(a[r] * b[(5 - r) % 5] for r in range(5))
    print(ans)

if __name__ == "__main__":
    main()
