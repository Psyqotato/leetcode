class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []
        lenth = len(nums)
        if lenth == 1:return [nums]
        i = 0
        while i < lenth:
            temp = nums.copy()
            temp.remove(nums[i])
            for j in Solution().permuteUnique(temp):solutions.append([nums[i]] + j)
            i += 1
            while i < lenth and nums[i] == nums[i-1]:i += 1
        return solutions