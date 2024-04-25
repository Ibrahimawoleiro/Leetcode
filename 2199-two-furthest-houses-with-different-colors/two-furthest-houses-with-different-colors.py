class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_distance = 0
        i = 0
        j = len(colors) - 1
        while(i < len(colors)):
            if colors[j] != colors[i]:
                if j - i > max_distance:
                    max_distance = j - i
                j = len(colors) - 1
                i+=1
            else:
                if j != i:
                    j -= 1
                else:
                    i+=1
                    j = len(colors) - 1
        return max_distance