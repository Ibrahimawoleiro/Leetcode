class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(colors) == 1:
            return 0

        l = 0
        r = 1
        time = 0
        while r < len(colors):

            if colors[l] != colors[r]:
                l = r 
            else:
                if neededTime[l] <= neededTime[r]:
                    time += neededTime[l]
                    l = r
                else:
                    time += neededTime[r]
            r += 1
            
        return time