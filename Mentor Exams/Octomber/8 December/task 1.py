def anagramas(str1, str2):
    if sorted(str1) == sorted(str2): #სტრინგები ალფაბეტური თანმიმდევრობით შევადარე ერთმანეთს
        return "True" #თუ თანხვედრააა , დავაბრუნებთ True-ს 
    return "False" #ხოლო თუ არარის სტრინგებს შორის თანხვედრა დავუბრუნებთ "False"

print(anagramas("listen","silent"))  
print(anagramas("triangle","integral"))
print(anagramas("apple","pale"))
print(anagramas("a","a"))
print(anagramas("rat","car"))

print(anagramas("horse","dog"))
print(anagramas("b","b"))

