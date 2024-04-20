class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        op = set(['+','D','C'])
        for val in operations:
            if val not in op:
                stack.append(int(val))
            else:
                if val == '+':
                    stack.append(int(stack[-1]) + int(stack[-2]))
                elif val == 'D':
                    stack.append(int(stack[-1]) * 2)
                else:
                    stack.pop()

        return sum(stack)