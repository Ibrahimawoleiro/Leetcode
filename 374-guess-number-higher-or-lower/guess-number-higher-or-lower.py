# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        h = n
        count = 10
        while l <= h:
            mid = (l + h) // 2
            r = guess(mid)
            if r == 0:
                return mid
            elif r == 1:
                l = mid + 1
            else: 
                h = mid - 1
        
        return 0