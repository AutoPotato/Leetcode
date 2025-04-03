# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        charCounter = {};
        for i in s:
            charCounter.setdefault(i, 0);
            charCounter[i] += 1;
        for i in range(len(s)):
            if charCounter[s[i]] == 1:
                return i;
        return -1;
# leetcode submit region end(Prohibit modification and deletion)


# dictionary = a collection consist of {key:value} pairs.
# Ordered and changeable. No duplicates allowed.
# s: str = "loveleetcode";
# print(list(s));
# charCounter = {"a": "test", "b": "test2"}
# print(charCounter["a"]);
# for i in range(len(list(s))):
#     print(i);
#     charCounter.update({i: 1})
# print(charCounter)

# the .update function finally worked
# but now how do I add 1 for every key?
# probably need an integer for that.
# print(charCounter[0])
# print(charCounter[0] + 1) #yay this works, +1 adds value to the key value

# Testing
s: str = "loveleetcode"; #3
s = "aabb"; #-1
s = "dddccdbba" #8
charCounter = {};
for i in list(s):
    charCounter.setdefault(i, 0);
    charCounter[i] += 1;
print(charCounter)
print(s[0])
print(charCounter[s[0]])
for i in range(len(s)):
    if charCounter[s[i]] == 1:
        print(i);



    # if charCounter[i] == 1:
    #     print(s.index(i))
    #     break;
# for i in charCounter is O(n), s.index() is also O(n); at worst can make it O(n) * O(n) = O(n²)?

# # don't forget the -1 condition
# # if all keys > 1, then return False.
# # if "> 1 checking" reached "len(list(charCounter))" times, return False.
# print()
#
# checkedTime: int =  0;
# for i in list(charCounter):
#     print(i)
#     checkedTime += 1;
#     if checkedTime == len(charCounter):
#             print("There's no non-repeating character.")
#             break;
#     if charCounter[i] == 1:
#         print("Found unique character.")
#         break

# Answer
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         charCounter = {};
#         for i in s: #Create a hashmap for every word, default value starts from 0
#             charCounter.setdefault(i, 0);
#             charCounter[i] += 1;
#
#         for i in range(len(s)): #Return True when found the non-repeating character.
#             if charCounter[s[i]] == 1:
#                 return i;
#
#         return -1; #Return -1 when all is done and there's no answer.

# Thoughts
# I should learn enumerate() for this.