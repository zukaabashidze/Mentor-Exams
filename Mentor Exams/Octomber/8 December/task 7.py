def find(start, end):
    primes = [] # სია ციფრებისათვის არის განკუთვნილი
    
    for num in range(start, end + 1):
        if num > 1: # უნდა იყოს 1 ზე მეტი
            for i in range(2, int(num ** 0.5) + 1): 
                # თუ რიცხვი იშლება მას ვერ ვუწოდებთ prime-ს როგორც jake paul-ს 
                if (num % i) == 0:
                    break
            else:
                #ხოლო თუ არ შლება რიცხვი მაშინ prime- არის და მარტო prime კი არაა არამედ Chad ია
                primes.append(num)
    return primes

print(find(10, 20)) 
print(find(1, 10)) 
print(find(20, 30)) 
print(find(24, 25)) 
print(find(1, 1)) 

print(find(27, 40)) 
print(find(15, 30)) 