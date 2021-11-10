class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        left_c, right_c, solutions, plates = [], [], [], []
        left, right, plate = -1, len(s), 0
        for i in range(len(s)):
            plates.append(plate)
            if s[i] == '|':
                left = i
            else:
                plate += 1
            left_c.append(left)
            if s[0 - i - 1] == '|':
                right = len(s) - i - 1
            right_c.append(right)
        for query in queries:
            right, left = left_c[query[1]], right_c[0 - query[0] - 1]
            solutions.append(plates[right] - plates[left] if right > left else 0)
        return solutions