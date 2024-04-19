class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        ans = [False for index in range(len(candies))]
        for index in range(len(candies)):
            if candies[index] + extraCandies >= max_candies:
                ans[index] = True
        return ans