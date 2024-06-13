class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        one_count = 0
        zero_count = 0

        for index in range(1, len(s)):
            if s[index] == '1':
                one_count += 1

        zero_count = 1 if s[0] == '0' else 0
        
        for index in range(1, len(s)):
            if zero_count + one_count > ans:
                ans = zero_count + one_count
            if s[index] == '1':
                one_count -= 1
            else:
                zero_count += 1
        return ans