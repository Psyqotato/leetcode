class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        num = len(nums) - 1
        if num < 3:
            return []
        nums.sort()
        x1 , result = 0, []
        while (x1 < num - 2):
            if nums[x1] + nums[x1+1] + nums[x1+2] + nums[x1+3] > target:break
            if nums[x1] + nums[num] + nums[num-1] + nums[num-2] < target:
                x1 += 1
                continue
            x2 = x1 + 1
            while (x2 < num - 1):
                if nums[x1] + nums[x2] + nums[x2+1] + nums[x2+2] > target:break
                if nums[x1] + nums[x2] + nums[num] + nums[num-1] < target:
                    x2 +=1
                    continue
                x3, x4 = x2 + 1, num
                while (x3 < x4):
                    sum = nums[x1] + nums[x2] + nums[x3] + nums[x4]
                    if sum < target:
                        x3 += 1
                    elif sum > target:
                        x4 -= 1
                    else:
                        result.append([nums[x1], nums[x2], nums[x3],nums[x4]])
                        x4 -= 1
                        x3 += 1
                        while (nums[x3] == nums[x3-1]) and (x3 < x4):x3 += 1
                        while (nums[x4+1] == nums[x4]) and (x4 > x3):x4 -= 1
                x2 += 1
                while (nums[x2-1] == nums[x2]) and (x2 < x3): x2 += 1 
            x1 += 1
            while (nums[x1-1] == nums[x1]) and (x1 < x2): x1 += 1    
        return result