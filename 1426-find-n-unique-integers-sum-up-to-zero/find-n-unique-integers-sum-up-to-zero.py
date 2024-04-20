class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [k+1 for k in range(n)]

        balancer = ((n-1)*(n))//2

        ans[-1] = -1 * balancer

        return ans