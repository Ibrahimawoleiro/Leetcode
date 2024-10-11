class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        r = 0
        while num > 0:
            r *= 10
            r += num % 10
            num //= 10
        return x == r