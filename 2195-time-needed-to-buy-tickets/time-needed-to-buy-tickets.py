class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        ans = 0

        for index in range(len(tickets)):

            if index <= k:
                if tickets[index] <= tickets[k]:
                    ans += tickets[index]
                else:
                    ans += tickets[k]
            else:
                if tickets[index] >= tickets[k]:
                    ans += tickets[k] - 1
                else:
                    ans += tickets[index]

        return ans