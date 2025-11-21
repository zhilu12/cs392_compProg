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

def KMP(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = LPS(pattern)
    i = 0
    j = 0
    count = 0
    last = -1

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == m:
                start = i - m
                end = i - 1

                # if interval starts after the last changed pos
                if start > last:
                    count += 1
                    last = end
                
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return count

text = str(input())
pattern = str(input())

print(KMP(text, pattern))