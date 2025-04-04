# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counterDict = defaultdict(int)
        for char in s:
            counterDict[char] += 1;

        for i, char in enumerate(s):
            if counterDict[char] == 1:
                return i;
        return -1;
# leetcode submit region end(Prohibit modification and deletion)

# s = "leetcode" #0
# s = "loveleetcode" #2
# s = "aabb" #-1
# s = "dddccdbba" #8
# print(s);
# print(list(s));
# print(enumerate(list(s)[0]));
# charCounter = {};
# for i in s:
#     charCounter.setdefault(i, 0);
#     charCounter[i] += 1;
#
# for index, key in enumerate(charCounter):
#     print(index, key, charCounter[key])
#     if charCounter[key] == 1:
#         print(f"Answer is {s.index(key)}");
#         break;
#     print(-1);
"""
I'm hash mapping the whole string before processing it, at worst it's O(n²),
but what if it can process from the beginning, and stop when it hit the first key that only has 1?
"dddccdbba"
if we use the in-built function .count(), it'd probably be faster, although idk why it's faster
and if I use .count(), I would no longer need to build a hashmap first.
if i use defaultdict(), I can remove charCounter.setdefault(i, 0);
"""
from collections import defaultdict

def check_unique(s: str) -> int:
    counter = defaultdict(int)
    for char in s:
        counter[char] += 1;

    for i, char in enumerate(s):
        if counter[char] == 1:
            return i;
    return -1;

s = ["leetcode", "loveleetcode", "aabb", "dddccdbba"]
#0, 2, -1, 8
for i in s:
    print(check_unique(i))