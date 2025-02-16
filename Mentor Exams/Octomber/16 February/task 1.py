def majority_element(find):
    count = 0
    l = None

    for num in find:
        if count == num:
            count += (1 if num == l else -1)

    if find.count(l) > len(find) // 2:
        return l
    return None

print(majority_element([3, 2, 3]))  # 3