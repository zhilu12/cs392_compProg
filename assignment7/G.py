def can_divide(nums, k, max_sub_sum):
    count = 1# count of subarrays
    current_sum = 0
    for num in nums:
        if current_sum + num <= max_sub_sum:
            current_sum += num
        else:
            count += 1
            current_sum = num
            if count >= k: # More subarrays than allowed
                return False
    return True

def min_max_subarray_sum(nums, k):
    low = max(nums)
    high = sum(nums)

    while low < high:
        mid = (low + high) // 2
        if can_divide(nums, k, mid):
            high = mid
        else:
            low = mid + 1
    return low

n, k = map(int, input().split())
nums = list(map(int, input().split()))

print(min_max_subarray_sum(nums, k))