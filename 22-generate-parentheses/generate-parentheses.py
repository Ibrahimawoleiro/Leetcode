class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(curr,o, c ):
            if len(curr) == 2*n:
                ans.append(curr[:])
                return 
            
            if o > c:
                #Two options: Add ( or add )
                if o < n:
                    curr += '('
                    helper(curr, o + 1, c)
                    curr = curr[:-1]
                curr += ')'
                helper(curr, o, c + 1)
            else:
                if o < n:
                    curr += '('
                    helper(curr, o + 1, c)
                    curr = curr[:-1]
                else:
                    curr += ')'
                    helper(curr, o, c + 1)

        helper('', 0, 0)
        return ans



