class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count, result, i = 0, 0, 0
        if len(nums) < 3: return 0
        while i < len(nums) - 2:
            while i < len(nums) - 2 and nums[i + 2] - nums[i + 1] == nums[i + 1] - nums[i]:
                count, i = count + 1, i + 1
            result, i, count =  result + int(((1 + count) * count) / 2), i + 1, 0
        return result