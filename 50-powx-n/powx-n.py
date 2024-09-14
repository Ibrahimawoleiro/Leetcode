class Solution:
    def myPow(self, x: float, n: int) -> float:
        inverse = n < 0
        base = x
        exponent = abs(n)
        ans = 1.0
        #We keep on looping as long as exponent > 0
        while exponent > 0:
            if exponent % 2 == 0:
                base *= base 
                exponent /= 2
            else:
                ans *= base
                exponent -= 1
        return 1 / ans if inverse else ans