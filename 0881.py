class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        for i in range(len(people) - 1, -1, -1):
            if people[i] < limit:
                right = i
                break
        left, count, result = 0, people[right], len(people) - 1 - i
        while left <= right:
            if left < right and count + people[left] <= limit:
                result, left, right = result + 1, left + 1, right -1
                count = people[right]
            elif left == right:
                result += 1
                break
            else:
                result, right = result + 1, right - 1
                count = people[right]    
        return result