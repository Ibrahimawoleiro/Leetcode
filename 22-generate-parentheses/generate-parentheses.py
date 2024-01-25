class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def helper(build, no_open, no_close):
            if no_open == n and no_close == n:
                ans.append(build)
                return 
            
            if no_open == no_close:
                build = build + "("
                no_open += 1
                helper(build, no_open, no_close)
            else:
                if no_open < n:
                    build = build + "("
                    no_open += 1
                    helper(build, no_open, no_close)
                    no_open -= 1
                    build = build[:-1]
                    build = build + ")"
                    no_close += 1
                    helper(build, no_open, no_close)
                else:
                    build = build + ")"
                    no_close += 1
                    helper(build, no_open, no_close)

        helper("",0,0)
        return ans
