class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opening_count = 0
        closing_count = 0
        count = 0
        ans = ''
        helper = []

        for i in range(len(s)):
            if (s[i] != ')') or s[i] == ')' and count > 0:
                helper.append(s[i])
                if s[i] == '(':
                    opening_count += 1
                    count += 1

                elif s[i] == ')':
                    closing_count += 1
                    count -= 1
        
        o = 0
        c = 0
        for char in helper:
            if char == '(' and o < closing_count or char == ')' and c < closing_count:
                ans += char
                if char =='(':
                    o += 1
                if char == ')':
                    c += 1
            elif char != '(' and char != ')':
                ans += char

        return ans