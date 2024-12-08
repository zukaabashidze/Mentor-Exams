# ჯერ უნდა გამოვთვალოთ GCD
def GCD (a, b):
    while b:
        a, b = b, a % b 
    return a
# შემდეგ ვთვლით LCM-ს
def LCM(a, b):
    return abs(a * b) // GCD(a, b)

# ჯამი არის აქ
def sum (f1, f2):
    num1, def1 = f1
    num2, def2 = f2

    # LCM-ის გამოთვლა ხდება აქ
    comm = LCM(def1, def2)

    #nummer-ის გამოთვლა ხდება
    numer = num1 * (comm // def1) + num2 *(comm // def2)

    # გამარტივდება GCD-ის გამოყენება
    com_GCD = GCD(numer, comm)
    simply = numer // com_GCD
    simply2 = comm // com_GCD

    return (simply, simply2)

print(sum((1, 2), (1, 3)))
print(sum((1, 4), (1, 4)))
print(sum((2, 5,) (1, 5)))
print(sum((3, 4), (5, 6)))
print(sum((5, 12), (7, 15)))

print(sum((4, 15), (3, 18)))
print(sum((1, 11), (8, 13)))
