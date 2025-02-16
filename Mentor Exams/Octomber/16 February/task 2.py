def missing(arr):
    nums = set(arr)
    n = 1 
    while n in nums:
        n += 1
        return n
    
print(missing([1, 2, 4, 5]))  # Output: 3