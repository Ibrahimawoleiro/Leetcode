class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        def no_neighbor(curr):
            if curr < 0 or curr >= len(flowerbed):
                return True
            
            return False if  flowerbed[curr] == 1 else True

        
        for index in range(len(flowerbed)):
            if no_neighbor(index - 1) and no_neighbor(index + 1) and flowerbed[index] == 0:
                n -= 1
                flowerbed[index] = 1
        return n <= 0
                