class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        

        for val in s:
            if val != ']':
                stack.append(val)
            else:
                helper_stack = []
                curr  = stack.pop()
                while curr != '[':
                    helper_stack.append(curr)
                    curr = stack.pop()
                helper_stack.reverse()
                curr = ''.join(helper_stack)
                count = []
                while stack and stack[-1].isdigit():
                    count+=stack.pop()
                count.reverse()
                print(count)
                count = int(''.join(count))
                word = ''.join(helper_stack)
                print(count, curr, word)

                for val in range(count - 1):
                    curr += word
                print(curr, 'usjeklrsdnjfd')
                stack.append(curr)
        return ''.join(stack)