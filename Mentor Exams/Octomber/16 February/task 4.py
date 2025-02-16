def find_Anagrams(s, p):
    result = []
    p1 = len(p)
    s1 = len(s)

    if p1 > s1:
        return result
    
    p_count = [0] * 26
    for char in p:
        p_count[ord(char) - ord('a')] += 1

    window_count = [0] * 26
    for i in range(p1):
        window_count[ord(s[i]) - ord('a')] += 1

    if window_count == p_count:
        result.append(0)
    
    for i in range(p1, s1):
        window_count[ord(s[i]) - ord('a')] += 1
        window_count[ord(s[i - p1]) - ord('a')] -= 1

        if window_count == p_count:
            result.append(i - p1 + 1)
    
    return result

print(find_Anagrams('listen', 'silent'))  # [0, 5]