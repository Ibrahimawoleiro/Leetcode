class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        i = 0

        while(i<len(flowerbed)):
            left = False
            right = False
            if flowerbed[i] == 0:
                if i - 1 < 0 or flowerbed[i - 1] == 0:
                    left = True
                if i + 1 >= len(flowerbed) or flowerbed[i + 1] == 0:
                    right = True
                if left and right:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
            i+=1