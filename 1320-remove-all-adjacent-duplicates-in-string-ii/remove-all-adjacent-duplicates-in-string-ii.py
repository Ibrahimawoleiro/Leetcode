class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []

        for val in s:
            if not stack:
                stack.append((val, 1))

            else:
                if stack[-1][0] == val:
                    curr = stack.pop()
                    letter = curr[0]
                    count = curr[1] + 1
                    
                    if count != k:
                        stack.append((letter, count))
                else:
                    stack.append((val, 1))

        i = 0
        ans = ''
        while i < len(stack):
            for _ in range(stack[i][1]):
                ans += stack[i][0]
            i += 1

        return ans
