# def count_of(n):
    
#     freq ={}
#     for i in n:
#         freq[i] = freq.get(i,0)+1

#     return freq.get('3')



# n ='22331122'
# print(count_of(n))



# n = '1324354657465342nbvdagr'

# for i in n:
#     print(i)

# for i in range(len(n)):
#     print(n[i])



# Check if all digits are unique

# "12345" → True
# "1123"  → False



# def unique(n):
#     fre ={}
#     for i in n:
#         fre[i] = fre.get(i,0)+1
        
#     for i in fre:
#         if fre[i]!=1:
#             return False
        
#     return True

# n = '345235'
# print(unique(n))



# #find min and max ele
# def max_ele(n):
#     fre ={}
#     for i in n:
#         fre[i] = fre.get(i,0)+1
        
    
        
#     return min(fre,key=fre.get) #use max

# n = '1223333'
# print(max_ele(n))






# Remove all digits that appear more than once

# "22331122" → "3"


def digit_remove_morethan_one(n):
    freq = {}

    # count frequency
    for ch in n:
        freq[ch] = freq.get(ch, 0) + 1

    # collect digits with frequency == 1
    result = ""
    for ch in n:
        if freq[ch] == 1:
            result += ch

    return result

n = '334553332899'
print(digit_remove_morethan_one(n))


s = "123"
n = int(s)
print(n)        # 123
print(type(n))  # <class 'int'>


# Converting single character digi
ch = "7"
num = int(ch)
print(num)   # 7


Used when looping through strings:

for ch in "3452":
    digit = int(ch)



4️⃣ Convert list of string digits → list of ints
lst = ["1", "2", "3"]
nums = list(map(int, lst))


converting int → str is always safe in Python.

✅ How to convert int to str
Basic way (most common)
n = 123
s = str(n)

print(s)        # "123"
print(type(s))  # str

🔁 Why this is used a LOT in DSA

Once converted to string, you can:

Loop over digits

Use hashing

Use string methods

Example:

n = 34523
for ch in str(n):
    print(ch)

🧠 Common interview use cases
1️⃣ Count digits using string
len(str(12345))  # 5

2️⃣ Convert int → str → list of digits
digits = list(str(123))
# ['1', '2', '3']

3️⃣ Reverse a number
n = 1234
rev = int(str(n)[::-1])

⚠️ Important note

str() never fails for integers

Negative numbers:

str(-123)  # "-123"


If needed:

str(abs(-123))  # "123"

🗣️ One-line interview answer

“We convert an integer to string using str() to process digits easily.”