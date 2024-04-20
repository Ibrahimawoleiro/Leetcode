class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        checker = set(candyType)
        if len(checker) <= len(candyType) // 2:
            return len(checker)
        else:
            return len(candyType) //2