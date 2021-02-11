class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        solutions = []
        i = 0
        while i < len(candidates) and (target - candidates[i]) > 0: 
            for j in Solution().combinationSum(candidates[i:],target - candidates[i]):solutions.append([candidates[i]] + j)
            i += 1
        if target in candidates:solutions.append([target])
        return solutions