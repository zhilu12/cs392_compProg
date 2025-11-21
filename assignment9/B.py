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
borders = []
lps = LPS(text)

length = lps[n - 1]
while length > 0:
    borders.append(length)
    length = lps[length - 1]
        
borders.reverse()

print(" ".join(str(num) for num in borders))