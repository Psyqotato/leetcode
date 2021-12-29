class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i = 1
        # while i <= len(nums) - 1:
        #     if nums[i] == nums[i - 1]:
        #         nums.pop(i)
        #     else:
        #         i += 1
        # return len(nums)
        left, right = 0, 1
        while right <= len(nums) - 1:
            if nums[left] == nums[right]:
                right += 1
            else:
                del nums[left+1:right]
                left, right = left + 1, left + 2
        del nums[left+1:right]
        return len(nums)