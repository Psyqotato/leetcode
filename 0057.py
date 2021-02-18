class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []:return [newInterval]
        left, right = -1, -1
        for i in range(0,len(intervals)):
            if newInterval[0] < intervals[i][0] and left == -1:left = i - 0.5
            elif newInterval[0] >= intervals[i][0] and newInterval[0] <= intervals[i][1]:left = i
            elif newInterval[0] >= intervals[i][1]:left = i + 0.5
            if newInterval[1] < intervals[i][0] and right == -1:right = i - 0.5
            elif newInterval[1] >= intervals[i][0] and newInterval[1] < intervals[i][1]:right = i
            elif newInterval[1] >= intervals[i][1]:right = i + 0.5
        if left % 1 != 0 and right % 1 == 0:intervals = intervals[0:int(left+0.5)] + [[newInterval[0],intervals[int(right)][1]]] + intervals[right+1:] 
        elif right % 1 !=0 and left % 1 == 0:intervals = intervals[0:left] + [[intervals[left][0],newInterval[1]]] + intervals[int(right+1):]
        elif left % 1 == 0 and right % 1 == 0:intervals = intervals[0:left] + [[intervals[left][0],intervals[right][1]]] + intervals[right+1:]
        else:intervals = intervals = intervals[0:int(left+0.5)] + [newInterval] + intervals[int(right+1):]
        return intervals