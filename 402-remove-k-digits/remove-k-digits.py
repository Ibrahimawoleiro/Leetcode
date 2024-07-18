class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []

        for n in num:
            if not stack:
                if n == '0':
                    continue
                stack.append(n)
            else:
                if int(stack[-1]) <= int(n):
                    stack.append(n)
                else:
                    while stack and int(stack[-1]) > int(n) and k > 0:
                        stack.pop()
                        k -= 1
                    
                    if not stack and n == '0':
                        continue
                    else:
                        stack.append(n)
        if k > 0:
            while k > 0 and stack:
                stack.pop()
                k -= 1
        return ''.join(stack) if stack else '0'
                        
