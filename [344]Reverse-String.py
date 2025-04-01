# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[-i-1] = s[-i-1], s[i];
# leetcode submit region end(Prohibit modification and deletion)

# Testing
# s = ["h", "e", "l", "l", "o"]
# print(s);
# print(s[0], s[1], s[2]);
# s_length = len(s);
# print(s_length);
# s = list(reversed(s)); # this creates a new list, instead of edit in-place, so it doesn't work.
# print(s);
# s[:] = reversed(s); #this worked but I have no idea why.
# s.reverse(); Works also, it makes more sense to me tho.

# Probably should write a normal one and actually think about the problem...
# Else I'm not learning anything at all...

# Input: s = ["h","e","l","l","o"] Output: ["o","l","l","e","h"]
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
# for i in range(len(s)//2):
#     s[i], s[~i] = s[~i], s[i];

# Not using tilde(~)
#     s[i], s[-i-1] = s[~i], s[-i-1];