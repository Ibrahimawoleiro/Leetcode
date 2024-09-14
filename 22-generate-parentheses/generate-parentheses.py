class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursive(combo, op, cl, ans):
            if op == n and cl == n:
                ans.append(combo)
                return 
            #If the number of open brackets in less than n, then we can add an open bracker
            if op < n:
                recursive(combo + '(', op + 1, cl, ans)
            #If the number of open brackets is greater than the number of closing bracket, 
            #then you can add a closing bracket
            if op > cl:
                recursive(combo + ')', op, cl + 1, ans)
        ans = []
        recursive('', 0,0,ans)
        return ans