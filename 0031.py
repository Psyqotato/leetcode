class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num = len(nums)
        if num != 1:
            high = low = 0
            for i in range(num-2,-1,-1):
                if nums[i] < nums[i + 1]:
                    high = i + 1
                    break
            for i in range(num-2,-1,-1):
                if nums[i] > nums[i + 1]:
                    low = i + 1
                    break
            if high == 0 and nums[num - 1] == nums[low]:
                nums.sort()
            elif high > low:
                nums[high], nums[high - 1] = nums[high - 1], nums[high]
            elif high < low:
                if (max(nums[high+1:]) <= nums[high-1]):
                    nums[high-1], nums[high] = nums[high], nums[high-1]
                else:
                    for i in range(num-1,high,-1):
                        if nums[i] > nums[high - 1]:
                            x = i
                            break
                    nums[high-1], nums[x] = nums[x], nums[high-1]
                for i in range(0,int((num - 1 - high)/2)+1):
                    nums[high + i], nums[num - 1 - i] = nums[num - 1 - i], nums[high + i]