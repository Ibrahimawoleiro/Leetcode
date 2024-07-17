class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0 for num in temperatures]
        for index in range(len(temperatures) - 1, -1, -1):
            curr = temperatures[index]
            if not stack:
                stack.append((curr, 0))
            else:
                count = 0
                while stack:
                    if stack[-1][0] <= curr:
                        count += stack[-1][1]
                        stack.pop()
                    else:
                        count += 1
                        break

                if stack:
                    ans[index] = count
                    stack.append((curr, count))
                else:
                    stack.append((curr, count)) 

        return ans