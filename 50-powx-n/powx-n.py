class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        # If n is negative, convert it to positive and set a flag to invert the result later
        inverse = n < 0
        base = x
        exponent = abs(n)
        ans = 1.0
        
        # Loop to perform fast exponentiation
        while exponent > 0:
            # If the exponent is odd, multiply the current base with the result
            if exponent % 2 == 1:
                ans *= base
            
            # Square the base and halve the exponent
            base *= base
            exponent //= 2
        
        # If the original exponent was negative, invert the result
        return 1 / ans if inverse else ans