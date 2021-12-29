class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left_count, right_count, result = 0, 0, 0
        for i in range(int(len(s)/2)):
            if s[i] == "L": left_count += 1
            else: left_count -= 1
            if s[len(s)-i-1] == "L": right_count += 1
            else: right_count -= 1
            if left_count == 0: result += 1
            if right_count == 0: result += 1
        if left_count != 0 and right_count != 0 and left_count + right_count == 0: result += 1
        return result