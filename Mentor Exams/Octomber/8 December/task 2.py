def unique(text):
    words = text.lower().split() # ტექსტი გადავაქციე პატარა ასოებად და გავყავი როგორც რომეო და ჯულიეტა
    unique = [ ] # ეს არის სია უუუნიკალურესი სიტყვებისათვის
    for word in words: # ეხა გადავამოწმე თითეული სიტყვა როგორც მაფიაშია :D
        if word not in unique: # აქაც გადავამოწმე რომელი სიტყვა არარის უუუნიკალურესი
            unique.append(word) # თუ სიტყვა უუუნიკალურესია დაემატება სიაში
    return str(len(unique)) # და ახლა სიტყვების რაოდენობა  დავაბრუნე 

print(unique("The quick brown fox jumps over the lazy dog"))
print(unique("Hello hello world!"))
print(unique(""))
print(unique("Python is fun. Python is cool."))
print(unique("One word"))

print(unique("ar mowio bioi bioi klavs! dzirs bioi dzirs bioi"))
print(unique("tezel xelou vici ro amowmeb chem namushevars"))