class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for arr in grid:
            for number in arr:
                if number < 0:
                    count+=1
        return count