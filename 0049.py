class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solutions = {}
        for str1 in strs:
            key = tuple(sorted(str1))
            solutions[key] = solutions.get(key, []) + [str1]
        return list(solutions.values())