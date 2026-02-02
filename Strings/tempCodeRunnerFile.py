# First non-repeating character of given string

# # comments
# # Given a string s of lowercase English letters, the task is to find the first non-repeating character. If there is no such character, return '$'.

# # Examples: 

# # Input: s = "geeksforgeeks"
# # Output: 'f'
# # Explanation: 'f' is the first character in the string which does not repeat.

# # Input: s = "racecar"
# # Output: 'e'
# # Explanation: 'e' is the only character in the string which does not repeat.

# # Input: "aabbccc"
# # Output: '$'
# # Explanation: All the characters in the given string are repeating





# def nonRepeatingChar(s):
#     MAX_CHAR = 26
#     vis = [-1] * MAX_CHAR

#     # First pass: track character occurrence
#     for i in range(len(s)):
#         idx = ord(s[i]) - ord('a')
#         if vis[idx] == -1:
#             vis[idx] = i      # first occurrence
#         else:
#             vis[idx] = -2     # repeating character

#     # Find smallest index of non-repeating character
#     res = float('inf')
#     for i in range(MAX_CHAR):
#         if vis[i] >= 0:
#             res = min(res, vis[i])

#     return '$' if res == float('inf') else s[res]


# # Example
# s = "geeksforgeeks"
# print(nonRepeatingChar(s))  # Output: f

