class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        x = 0
        for index in range(len(num)):
            if index == 0:
                x+=num[index]
                continue
            x*=10
            x+=num[index]
        x += k
        ans = []
        while(x > 0):
            ans.append(x % 10)
            x = int(x//10)
        ans.reverse()
        return ans

