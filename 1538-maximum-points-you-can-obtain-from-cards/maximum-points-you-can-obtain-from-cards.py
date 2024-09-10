class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        right_pointer = len(cardPoints)
        left_pointer = k - 1
        sumr = 0
        suml = 0
        ans = 0
        for index in range(k):
            suml += cardPoints[index]
        ans = suml + sumr
        while left_pointer >= -1:
            ans = max(ans, suml + sumr)
            if left_pointer >=0:
                suml -= cardPoints[left_pointer]
            left_pointer -= 1
            right_pointer -= 1
            sumr += cardPoints[right_pointer]
        return ans     