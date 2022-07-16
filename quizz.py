from math import factorial


def combination(n, k):
    return factorial(n) / (factorial(n - k) * factorial(k))


def combination_rec(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return combination_rec(n - 1, k - 1) + combination_rec(n - 1, k)

# -------------------------------------------------------------------------


comb1 = combination(46, 6)
comb2 = combination(25, 6)

print(comb1 - comb2)


sum = 0
for i in range(25, 46):
    comb = combination(i, 5)
    sum += comb

print(sum)
