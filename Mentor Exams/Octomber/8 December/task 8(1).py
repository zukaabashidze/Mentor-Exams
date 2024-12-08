def Xbonacci(X, n):
    list = [1] * X

    while len(list) < n:
        list.append(sum(list[-X:]))
            
    return list[:n]


print(Xbonacci(3, 10)) 
print(Xbonacci(2, 10))
print(Xbonacci(4, 6))
print(Xbonacci(5, 8))
print(Xbonacci(3, 1))