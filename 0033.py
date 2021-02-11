class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target == nums[0]:return 0
        elif target == nums[-1]:return len(nums) - 1
        left, right, mid = 0, len(nums) - 1, 0 
        if nums[-1] < nums[0]:
            mid = int(round(right - left) / 2)
            while nums[mid] < nums[mid + 1]:
                if nums[mid] > nums[left]:left = mid
                else:right = mid
                mid = int(round(right - left) / 2) + left
        nums1 = nums[mid+1:] + nums[:mid+1]
        left, right = 0 , len(nums1) - 1
        if target == nums1[right]:return mid
        elif target == nums1[left]:return mid + 1
        while right - left > 1:
            mid1 = int(round(right - left) / 2) + left
            if target == nums1[mid1]:
                if mid1 + mid + 1 > len(nums):return mid1 + mid - len(nums) + 1
                else:return mid1 + mid + 1
            if target > nums1[mid1]: left = mid1
            else:right =  mid1   
        return -1