# Input: s = ["h","e","l","l","o"] Output: ["o","l","l","e","h"]
s = ["h", "e", "l", "l", "o"];
print(s);

# s[0], s[4] = s[4], s[0]
# s[1], s[3] = s[3], s[1]

# ~0 = -1 so in this case(array of 5):
# s[0], s[4] = s[4], s[0]
# s[1], s[3] = s[3], s[1]
# ==
# s[0], s[~0] = s[~0], s[0]
# s[1], s[~1] = s[~1], s[1]

# We can probably use variables?
# for i in range(len(s)):
#     if i == len(s)//2:
#         break;
#     s[i], s[~i] = s[~i], s[i];
# print(s);

# We can delete the if statement and move // into the for loop.
# This is my final answer
for i in range(len(s)//2):
    s[i], s[~i] = s[~i], s[i];

#====Testing=========================
print("");
if s == ["o","l","l","e","h"]:
    print("Succeed");
else:
    print("Failed");
print(s);