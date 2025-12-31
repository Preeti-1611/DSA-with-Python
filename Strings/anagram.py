def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    char_count = {}

    # Count characters in s1
    for ch in s1:
        char_count[ch] = char_count.get(ch, 0) + 1

    # Decrease count using s2
    for ch in s2:
        char_count[ch] = char_count.get(ch, 0) - 1

    # Check if all values are zero
    for value in char_count.values():
        if value != 0:
            return False

    return True


# Driver code
s1 = "geeks"
s2 = "kseeg"

print(are_anagrams(s1, s2))  # True
