class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        print(n)
        if n == 0:
            return False
        if n == 1:
            return True
        if not isinstance(n, int) and n > math.floor(n):
            return False
        return self.isPowerOfTwo(n/2)