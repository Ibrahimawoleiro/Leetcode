class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        i = 0
        j = 0
        ans = ''
        o_count = 1
        c_count = 0
        while(j < len(s)):
            if i == j:
                j+=1
                continue
            if s[j] == '(':
                o_count+=1
            elif s[j] == ')':
                c_count+=1
                if o_count == c_count:
                    ans += s[i+1:j]
                    i = j+1
                    o_count = 1
                    c_count = 0
            j+=1
        
        return ans