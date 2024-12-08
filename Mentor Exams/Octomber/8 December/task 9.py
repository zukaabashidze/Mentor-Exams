def is_prime(num):
    #თუ რიცხვი 1 ზე ნაკლებია ის არ არის Prime boy
    if num <= 1:
        return False
    # თუ რიცხვი არ იყოფა 2-დან და ვამოწმებთ ყველა რიცხვს
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primorial(n):
    #პროდუქთის შემოტანა
    product = 1
    #ვამოწმებთ ყველა რიცხვს თუ ის prime boy-ია (გამრავლებით ვამოწმებთ)
    for i in range(2, n + 1):
        if is_prime(i):
            product *= i
    return product


print(primorial(5))
print(primorial(10))
print(primorial(1))
print(primorial(7))
print(primorial(11))


print(primorial(2))
print(primorial(3))