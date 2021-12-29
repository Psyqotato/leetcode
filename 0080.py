class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:return len(nums)
        left, right = 0, 1
        while right <= len(nums) - 1:
            if nums[left] == nums[right]:
                right += 1
            else:
                del nums[left+1:right-1]
                left, right = left + 1, left + 2
        del nums[left+1:right-1]
        return len(nums)