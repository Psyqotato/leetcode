class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        solutions = []
        i = 0
        while i < len(candidates) and (target - candidates[i]) > 0: 
            for j in Solution().combinationSum2(candidates[i+1:],target - candidates[i]):solutions.append([candidates[i]] + j)
            i += 1
            while i < len(candidates):
                if candidates[i] == candidates[i-1]:i += 1
                else:break
        if target in candidates:solutions.append([target])
        return solutions