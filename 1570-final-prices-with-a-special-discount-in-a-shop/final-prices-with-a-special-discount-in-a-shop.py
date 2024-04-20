import heapq
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        i = len(prices) - 1
        ans_r = []
        stack = []
        while(i>=0):
            if len(stack) == 0:
                stack.append(prices[i])
                ans_r.append(prices[i])
            else:
                while len(stack) > 0 and prices[i] < stack[-1]:
                    stack.pop()

                if len(stack) > 0:
                    ans_r.append(prices[i]-stack[-1])
                    stack.append(prices[i])
                else:
                    stack.append(prices[i])
                    ans_r.append(prices[i])
            i-=1
        ans_r.reverse()

        return ans_r