# For each element in m, print how many times it appears in num”

num = [3,5,2,3,5,3,5,7,6,7,0]
m = [4,5,3,7,2,0]

# Step 1: Build frequency dictionary
freq = {}

for x in num:
    freq[x] = freq.get(x, 0) + 1

# Step 2: Query frequencies for elements in m
for x in m:
    print(x, "->", freq.get(x, 0))



# for i in range(0,n):
#     freq[num[i]] = freq.get(num[i],0)+1
