class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        num = len(nums) - 1
        nums.sort()
        x1 , dis, result = 0, abs(nums[0] + nums[1] + nums[2] - target), 0
        if target <= nums[0] + nums[1] + nums[2]:
            return (nums[0] + nums[1] + nums[2])
        elif target >= nums[num] + nums[num - 1] + nums[num - 2]: 
            return (nums[num] + nums[num - 1] + nums[num - 2])
        while (x1 < num-1):
            if (nums[x1] + nums[x1+1] + nums[x1+2] > target) and abs(nums[x1] + nums[x1+1] + nums[x1+2] - target) > dis:break
            if (nums[x1] + nums[num] + nums[num-1] < target) and abs(nums[x1] + nums[num] + nums[num-1] - target) > dis:
                x1 += 1
                continue
            x2, x3 = x1 + 1, num
            while (x2 < x3):
                sum = nums[x1] + nums[x2] + nums[x3]
                if abs(sum - target) <= dis:
                    result = sum
                    dis = abs(sum - target)
                if sum - target < 0:
                    x2 += 1
                elif sum - target > 0:
                    x3 -= 1
                else:return result
            x1 += 1  
        return result