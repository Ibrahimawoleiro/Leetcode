class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        ans = 0
        num = abs(x)
        while num > 0:
            ans *= 10
            ans += num % 10
            num = num // 10
        ans = ans * -1 if negative else ans
        return ans if ans <= (2 ** 31) - 1 and ans >= -(2 ** 31) else 0
