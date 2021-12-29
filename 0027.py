class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val not in nums: return len(nums)
        if len(set(nums)) == 1 and nums[0] == val: return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            while nums[left] != val: left += 1
            while nums[right] == val: right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        return right + 1