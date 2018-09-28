def calc(n, k):
    if k > n:
        return 0
    elif k == 0:
        return 1
    else:
        return calc(n-1, k) + calc(n-1, k-1)
# C(n, k) = C(n - 1, k) + C(n - 1, k - 1)


print(calc(*map(int, input().split())))
