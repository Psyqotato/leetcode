class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 not in arr: return False
        if arr[start] == 0: return True
        nums = {start}
        def canReach1(i):
            if arr[i] == 0: return True
            if i in nums: return False
            else:nums.add(i)
            return (i + arr[i] < len(arr) and canReach1(i + arr[i])) or (i - arr[i] >= 0 and canReach1(i - arr[i]))
        return (start + arr[start] < len(arr) and canReach1(start + arr[start])) or (start - arr[start] >= 0 and canReach1(start - arr[start]))