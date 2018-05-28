class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = {}
        i = 0
        while i < len(nums):
            if nums[i] in tmp:
                return [tmp[nums[i]], i]
            else:
                tmp[target-nums[i]] = i
            i += 1
        return []

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target-n], i]
            seen[n] = i
