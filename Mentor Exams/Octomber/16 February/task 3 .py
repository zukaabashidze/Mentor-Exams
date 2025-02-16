def rotate(r , x): 
    n = len(r)
    x = x % n
    return r[-x:] + r[:-x]

print(rotate([1, 2, 3, 4, 5], 2))  # [3, 4, 5, 1, 2]