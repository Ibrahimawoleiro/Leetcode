

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        digits = '123456789'
        n_low, n_high = len(str(low)), len(str(high))
        
        for length in range(n_low, n_high + 1):
            for start in range(10 - length):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    result.append(num)
                    
        return result
