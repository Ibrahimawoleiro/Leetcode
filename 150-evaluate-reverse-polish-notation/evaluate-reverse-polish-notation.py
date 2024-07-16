class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for val in tokens:

            if val in {'+', '-', '*','/'}:

                if val == '+':
                    f = stack.pop()
                    s = stack.pop()
                    stack.append( str(int(f) + int(s) ))
                if val == '-':
                    f = stack.pop()
                    s = stack.pop()
                    stack.append( str(int(s) - int(f) ))
                if val == '*':
                    f = stack.pop()
                    s = stack.pop()
                    stack.append( str(int(s) * int(f) ))
                if val == '/':
                    f = stack.pop()
                    s = stack.pop()
                    curr =int(s) / int(f)
                    if curr > 0:
                        curr = floor(curr)
                    else:
                        curr = ceil(curr)
                    stack.append( curr)
            else:
                stack.append(val)


        return int(stack.pop())

                