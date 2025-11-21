def LPS(pattern):
    m = len(pattern)
    lps = [0] * m
    j = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1 
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


text = str(input())
n = len(text)
lps = LPS(text)
L = lps[n - 1]

periods = []
periods.append(n)

while L > 0:
    period = n - L
    periods.append(period)
    L = lps[L - 1]

periods.sort()

print(" ".join(str(num) for num in periods))