class Solution:
    def mySqrt(self, x: int) -> int:
        return self.helper(1, x)
    
    def helper(self, x:int, target:int):
        if x * x > target:
            return x - 1
        elif x * x == target:
            return x
        else:
            return self.helper(x+1, target)
