# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        leftPointer = 1
        for rightPointer in range(1, len(nums)):
            if nums[rightPointer] != nums[rightPointer - 1]:
                nums[leftPointer] = nums[rightPointer];
                leftPointer += 1;
        return leftPointer;
# leetcode submit region end(Prohibit modification and deletion)

nums = [[1,1,2], [0,0,1,1,1,2,2,3,3,4]];
# 2, nums = [1,2,_]
# 5, nums = [0,1,2,3,4,_,_,_,_,_]

def remove_dupes(nums: list):
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r];
            l += 1;
    print(f"{l}, {nums}")
#===========================
for i, key in enumerate(nums):
    remove_dupes(nums[i]);
