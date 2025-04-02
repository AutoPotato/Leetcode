# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            return sorted(s) == sorted(t);
# leetcode submit region end(Prohibit modification and deletion)

#testing
# s, t= "anagram", "nagaram";
# print(list(t));
# print(s.count("a"));
# print(sorted(t));
# print(sorted(t).count("a"));

# if we just sort them all and compare the sorted result
# that'd be the answer, right?
# if sorted(s) == sorted(t):
#     print("Succeed!");
# else:
#     print("Failed.")

# if it's in a function:
# will return true if they are equal, false if they're not.
# return sorted(s) == sorted(t);