class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        ans = []

        def findPairs(left: int , right: int, curr: int):
            
            start_index = len(potions)

            while left <= right:

                mid = (left + right) // 2

                if potions[mid] * curr >= success:
                    if mid < start_index:
                        start_index = mid
                        right = mid - 1
                else:
                    left = mid + 1

            return start_index

        
        for index in range(len(spells)):

            start = findPairs(0, len(potions) - 1, spells[index])

            if start < len(potions):
                ans.append(len(potions) - start)
            else:
                ans.append(0)

        return ans