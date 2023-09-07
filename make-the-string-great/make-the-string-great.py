class Solution:
    def makeGood(self, s: str) -> str:
        ans = []
        
        for letter in s:
            if len(ans) == 0:
                ans.append(letter)
                continue
            if (ans[-1].upper() == letter and ans[-1] != ans[-1].upper()) or (ans[-1].lower() == letter and ans[-1] != ans[-1].lower()):
                ans.pop()
                continue
            ans.append(letter)
        
        return "".join(ans)