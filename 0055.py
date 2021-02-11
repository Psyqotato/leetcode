class Solution:
    def canJump(self, nums: List[int]) -> bool:
        k = len(nums)
        i = k - 1
        if i == 0:
            return True 
        while (i < k):
            k = i
            for j in range(i-1,-1,-1):
                if (int(nums[j]+j)) >= i:
                    i = j
                    break
        if i == 0:return True
        else:return False