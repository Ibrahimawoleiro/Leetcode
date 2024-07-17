class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for val in asteroids:
            if not stack:
                stack.append(val)
            else:
                if stack[-1] < 0:
                    stack.append(val)
                else:
                    if stack[-1] > 0:
                        if val > 0:
                            stack.append(val)
                        elif val < 0:
                            curr = abs(val)
                            curr_win = True
                            while curr_win:
                                if len(stack) > 0:
                                    back_of_stack = stack[-1]
                                    if back_of_stack < 0:
                                        stack.append(val)
                                        break
                                if len(stack) > 0 and curr > back_of_stack:
                                    stack.pop()
                                elif len(stack) == 0:
                                    stack.append(val)
                                    curr_win = False
                                else:
                                    if curr == stack[-1]:
                                        stack.pop()
                                        curr_win = False
                                    else:
                                        curr_win = False

        return stack