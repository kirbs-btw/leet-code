class Solution(object):
    def searchInsert(self, nums, target):
        if target > nums[-1]:
            return len(nums)

        for i, j in enumerate(nums): 
            if j == target:
                return i
            elif j > target:
                return i
