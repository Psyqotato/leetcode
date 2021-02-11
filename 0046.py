class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        lenth = len(nums)
        if lenth == 1:return [nums]
        i = 0
        while i < lenth:
            temp = nums.copy()
            temp.remove(nums[i])
            for j in Solution().permute(temp):solutions.append([nums[i]] + j)
            i += 1
        return solutions