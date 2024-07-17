class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        i = 0
        index = 0
        while index < len(pushed):
            if pushed[index] == popped[i]:
                i += 1
            elif len(stack) > 0 and stack[-1] == popped[i]:
                stack.pop()
                i += 1
                continue
            else:
                stack.append(pushed[index])
            index += 1

        while stack:
            if stack[-1] == popped[i]:
                stack.pop()
                i += 1
            else:
                return False

        return True