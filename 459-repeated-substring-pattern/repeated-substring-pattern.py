class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for ending in range(len(s) // 2):
            curr = s[0: ending + 1]
            l = 0
            r = ending
            jump = r - l + 1
            while r < len(s):
                check = s[l: r + 1]
                if check != curr:
                    break
                l += jump
                r += jump
                if l < len(s) and r >= len(s):
                    return False
                if r > len(s) - 1:
                    return True
        return False