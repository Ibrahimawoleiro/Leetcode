class Solution:
    def myPow(self, x: float, n: int) -> float:
        MOD = 10 ** 9 + 7
        inverse = n < 0
        base = x
        exponent = abs(n)
        ans = 1
        #We keep on looping as long as exponent > 0
        while exponent > 0:
            if exponent % 2 == 0:
                base = (base * base ) % MOD
                exponent //= 2
            else:
                ans = (ans * base) % MOD
                exponent -= 1
        return int(1 / ans if inverse else ans)

    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        five_power = (n + 1) // 2
        four_power = n // 2
        return (self.myPow(5, five_power) * self.myPow(4, four_power) ) % MOD