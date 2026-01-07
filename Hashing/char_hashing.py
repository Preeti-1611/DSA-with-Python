# Count how many times each character in q appears in string s

# This is called character hashing.



s = "azyayyzaca"
q = ["a", "a", "y", "z"]

# Step 1: Build frequency map
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Step 2: Answer queries
for ch in q:
    print(ch, "->", freq.get(ch, 0))







s = "azyayyzaca"
q = ["a", "y", "z"]

freq = [0] * 26

for ch in s:
    freq[ord(ch) - ord('a')] += 1

for ch in q:
    print(ch, "->", freq[ord(ch) - ord('a')])










s = "AZYAYYZACA"
q = ["A", "Y", "Z"]

freq = [0] * 26

for ch in s:
    freq[ord(ch) - ord('A')] += 1

for ch in q:
    print(ch, "->", freq[ord(ch) - ord('A')])












s = "aZy1@AyYzA2CA#"
q = ["a", "Z", "1", "@", "#"]

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in q:
    print(ch, "->", freq.get(ch, 0))









s = "aZy1@AyYzA2CA#"
q = ["a", "Z", "1", "@", "#"]

# ASCII has 128 characters
freq = [0] * 128

# Step 1: Count frequency
for ch in s:
    freq[ord(ch)] += 1

# Step 2: Answer queries
for ch in q:
    print(ch, "->", freq[ord(ch)])
