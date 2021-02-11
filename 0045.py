class Solution:
    def jump(self, nums: List[int]) -> int:
        i = len(nums) - 1
        if i == 0:return 0
        k, x = 0, 0
        while i - k > nums[k]:
            p = k + 1
            for j in range(k+2, nums[k]+k+1):
                if nums[j] + j > nums[p] + p:p = j
            k = p
            x = x + 1
        return x+1