def pascal(n):
    samkutxedi = [[1]] # პასლალის სამკუთხედი იწყება პირველი რიგით ანუ რაც აქ მიწერია [[1]] ეს აღნიშნავს პირველ რიგს 
    for i in range(1, n): # თითოეულ რიგს გადავუვლი როგორც მანქანა  
        row = [1] * (i + 1) #  თითოეული რიგირ იწყება 1 - ით და აქვს 1 ელემენტიი
        for j in range(1, i):
            row[j] = samkutxedi [i - 1][j - 1] + samkutxedi [i - 1][j]  # ახლა დავთვალე დანარჩენი ელემენტები
        samkutxedi.append(row) # აქ კი დავუმატე რიგს
    return samkutxedi

for row in pascal(5):
    print(row)



print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(5))
print(pascal(0))
