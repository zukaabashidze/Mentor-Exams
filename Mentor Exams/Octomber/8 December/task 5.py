def cesar(text, shift):
    return ' '.join(chr((ord(s) - 97 + shift)% 26 + 97) if s.islower() else s for s in text) #ოო აქ დავწერე რომ მხოლოდ პატარა ასოებზე იმუშაოს კოდმა 

print(cesar("abc", 2))
print(cesar("xyz", 3))
print(cesar("Hello, World!", 5))
print(cesar("Python", 0))
print(cesar("abc",-1))

print(cesar("zuka", 0))
print(cesar("cesari", 3))