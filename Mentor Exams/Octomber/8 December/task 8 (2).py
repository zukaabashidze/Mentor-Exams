def kth_smallest(arr, k):
    #ესეეგი აქ უკვე დალაგებულ მასივში (სიაში) ვალაგებთ ელემენტებს რაც მოცემული გვექნება
    arr.sort()
    #ვაბრუნებთ k - უმცირესებს
    return arr[k - 1]

print(kth_smallest([3, 2, 1, 5, 6, 4] , 2))
print(kth_smallest([3, 2, 1, 5, 6, 4] , 4))
print(kth_smallest([7, 10, 4, 3, 20, 15], 3))
print(kth_smallest([1, 2, 3, 4, 5], 1))
print(kth_smallest([1, 2, 3, 4, 5], 5))


print(kth_smallest([12, 3, 7, 5, 19] , 2))
print(kth_smallest([2, 8, 7, 10, 9, 3] , 4))
