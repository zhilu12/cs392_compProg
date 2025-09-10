
def arrSum(arr):
    n = len(arr)
    for i in range(1,  n):
        arr[i] = arr[i - 1] + arr[i]

    return max(arr)

def combineArr(a, b):
    res = []
    i, j = 0, 0
    while i < len(a) or j < len(b):
        if i < len(a):
            res.append(a[i])
            i += 1
        if j < len(b):
            res.append(b[j])
            j += 1

    return res


numTests = int(input())
end_res = []
for i in range(numTests):
    n = int(input())
    n_arr = list(map(int, input().split()))

    m = int(input())
    m_arr = list(map(int, input().split()))

    comb_arr = combineArr(n_arr, m_arr)
    
    end_res.append(max(0, arrSum(comb_arr)))


for num in end_res:
    print(num)