# 1. Given an array containing n-1 numbers taken from the range 1 to n, write a function to find the missing number. There are no duplicates in the array.
# 1. [1, 2, 4, 5] -> 3, [1] -> 2, [2, 3, 1, 5] -> 4

def missing_num(arr):
    list = len(arr) + 1

    t_sum = list * (list + 1) // 2

    arrcher_sum = sum(arr)

    missing = t_sum - arrcher_sum 

    return missing



print(missing_num([1, 2, 4, 5]))
print(missing_num([1]))
print(missing_num([2, 3, 1, 5]))










# 2. Write a function to find the longest common prefix among an array of strings. If there is no common prefix, return an empty string.
# 2. ["flower", "flow", "flight"] -> "fl", ["dog", "racecar", "car"] -> "", ["apple", "apple", "apple"] -> "apple"

def long_common(aura):
    if not aura:
        return " "

    prefiqsi = aura[0]

    for i in range(len(prefiqsi)):
        for h in aura:
            if i >= len(h) or h[i] != prefiqsi[i]:
                return prefiqsi[:i]
    return prefiqsi

print(long_common(["flower", "flow", "flight"]))
print(long_common(["dog", "racecar", "car"]))
print(long_common(["apple", "apple", "apple"]))












# 3. Given an array of size n, find the majority element. The majority element is the element that appears more than n // 2 times. You may assume that
# 3. [3, 2, 3] -> 3, [2, 2, 1, 1, 2] -> 2, [1, 1, 1, 1, 1] -> 1

def majorit(nums):
    count = {}

    for num in nums:
        if num in count:
            count[num] += 1
        
        else:
            count[num] = 1
        
        if count[num] > len(nums) // 2:
            return num

print(majorit([3, 2, 3]))
print(majorit([2, 2, 1, 1, 2]))
print(majorit([1, 1, 1, 1, 1]))












# 4. Write a function to return the nth number in the Fibonacci sequence. Solve it both recursively and iteratively.
# 4. 0 -> 0, 5 -> 5, 10 -> 55

def Fibonacci_sequence(s):
    if s == 0:
        return 0
    elif s == 1:
        return 1
    else:
        return Fibonacci_sequence(s - 1) + Fibonacci_sequence

print(Fibonacci_sequence(0))
print(Fibonacci_sequence(5))
print(Fibonacci_sequence(10))