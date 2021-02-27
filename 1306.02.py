class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 not in arr:return False
        if arr[start] == 0:return True
        arr1 = [start]
        nums = {start}
        while arr1 != []:
            start = arr1[0]
            arr1.remove(start)
            for i in [start + arr[start], start - arr[start]]:
                if 0 <= i < len(arr) and i not in nums:
                    if arr[i] == 0: return True
                    else:
                        arr1.append(i)
                        nums.add(i)
        return False