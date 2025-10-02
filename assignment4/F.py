numTests = int(input())

for _ in range(numTests):
    n = int(input())
    arr = list(map(int, input().split()))

    l, r = 0, n - 1

    while l < r:
        m = (l + r) // 2

        indices = list(range(l, m + 1))
        print("?", len(indices), *[i + 1 for i in indices], flush=True)
        ans = int(input())

        expected = sum(arr[i] for i in indices)
        

        if ans == expected:
            l = m + 1
        else:
            r = m

    print("!", l + 1)