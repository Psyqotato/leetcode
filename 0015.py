class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num = len(nums) - 1
        if num < 2:
            return []
        nums.sort()
        if nums[0] > 0 or nums[-1] < 0:
            return []
        x1 , result = 0, []
        while (x1 < num-1):
            if nums[x1] + nums[x1+1] + nums[x1+2] > 0:break
            if nums[x1] + nums[num] + nums[num-1] < 0:
                x1 += 1
                continue
            x2, x3 = x1 + 1, num
            while (x2 < x3):
                sum = nums[x1] + nums[x2] + nums[x3]
                if sum < 0:
                    x2 += 1
                elif sum > 0:
                    x3 -= 1
                else:
                    result.append([nums[x1], nums[x2], nums[x3]])
                    x3 -= 1
                    x2 += 1
                    while (nums[x2] == nums[x2-1]) and (x2 < x3):x2 += 1
                    while (nums[x3+1] == nums[x3]) and (x3 > x2):x3 -= 1
            x1 += 1
            while (nums[x1-1] == nums[x1]) and (x1 < x2): x1 += 1    
        return result