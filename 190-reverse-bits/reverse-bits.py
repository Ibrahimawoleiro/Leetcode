class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        curr = n
        for bit in range(32):
            if curr & 1 > 0:
                ans |= (1 << (31 - bit))
            curr >>= 1
        return ans