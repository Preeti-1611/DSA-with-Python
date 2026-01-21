arr = [1, 2, 3, 2, 4, 2, 5, 3]

freq = {}

for i in arr:
    freq[i] = freq.get(i, 0) + 1

most = max(freq, key=freq.get)
least = min(freq, key=freq.get)



print(freq[3])
print("Most frequent and value :", most,freq[most])
print("Least frequent  and its value:", least,freq[least])






s = "programming"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(max(freq, key=freq.get))
