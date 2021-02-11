class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:return [-1,-1]
        if target < nums[0] or target > nums[-1]:return [-1,-1]
        left, right, t = 0, len(nums) - 1, -1
        while right - left > 1:
            mid = ((right - left) // 2) + left
            if target == nums[mid]:
                t = 0
                break
            elif target > nums[mid]:left = mid + 1
            else:right = mid
        if target == nums[left]:
            mid = left
            t = 0
        if target == nums[right]:
            mid = right
            t = 0
        if t == -1:return [-1,-1]
        else:
            right1, left1 = mid, mid
            while right1 - left > 1:
                mid1 = ((right1 - left) // 2) + left
                if target == nums[mid1]:right1 = mid1
                else:left = mid1
            while right - left1 > 1:
                mid1 = ((right - left1) // 2) + left1
                if target == nums[mid1]:left1 = mid1
                else:right = mid1
            if nums[left] < target:left += 1
            if nums[right] > target:right -= 1
            return[left, right]