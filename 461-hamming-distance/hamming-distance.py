class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = x ^ y
        count = 0
        while result > 0:
            if result & 1 > 0:
                count += 1
            result >>= 1
        return count