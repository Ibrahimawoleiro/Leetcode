class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ''
        for index in range(len(num) - 2):
            if (len(ans) == 0 or int(num[index]) > int(ans[0])) and num[index] == num[index + 1] and num[index] == num[index + 2]:
                ans = num[index:index + 3]
        return ans
                