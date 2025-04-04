# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counterDict = Counter(s);
        for i, char in enumerate(s):
            if counterDict[char] == 1:
                return i;
        return -1;
# leetcode submit region end(Prohibit modification and deletion)
"""
This time I'm trying counter()
It literally generates a list with {key: count}, it suits this exact purpose.
Essentially we replaced:
        counterDict = defaultdict(int)
        for char in s:
            counterDict[char] += 1;

After submitting, it beats 45% more user than using defaultdict(int), nice.
"""
from collections import Counter;
# ===================================================
def check_unique(s: str) -> int:
    counterDict = Counter(s);
    for i, char in enumerate(s):
        if counterDict[char] == 1:
            return i;
    return -1;
# ===================================================
s = ["leetcode", "loveleetcode", "aabb", "dddccdbba"]
#0, 2, -1, 8
for i in s:
    print(check_unique(i))