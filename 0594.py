class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_set, result = collections.Counter(nums), 0
        if len(nums) == 0 or len(nums_set) == 1: return 0
        for i in nums_set:
            if i + 1 in nums_set:
                result = max(result, nums_set[i] + nums_set[i+1])
        return result