class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        
        count = 0

        for index in range(len(points)):
            if index == 0:
                continue
            
            count += max(abs(points[index][0] - points[index - 1][0]), abs(points[index][1] - points[index - 1][1]))
        
        
        return count