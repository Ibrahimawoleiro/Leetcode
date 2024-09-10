class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        lss = []
        rss = []
        left_length = [index for index in range(len(heights))]
        right_length = [index for index in range(len(heights))]
        ans = 0
        def gl_span(index):
            result = index
            while lss and heights[index] <= lss[-1][0]:
                result = lss.pop()[1]
            lss.append((heights[index], result))
            return result   
        def gr_span(index):
            result = index
            while rss and heights[index] < rss[-1][0]:
                result = rss.pop()[1]
            rss.append((heights[index], result))
            return result
        for index in range(len(heights)):
            left = gl_span(index)
            left_length[index] = left
        for index in range(len(heights) - 1, -1 ,-1):
            right = gr_span(index)
            right_length[index] = right
        for index in range(len(heights)):
            ans = max(ans, (right_length[index] - left_length[index] + 1) * heights[index])
        return ans

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        print(matrix)
        helper = [[0 for val in range(len(matrix[0]))] for val in range(len(matrix))]
        ans = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r == 0:
                    helper[r][c] = int(matrix[r][c])
                    continue
                if matrix[r][c] == '1':
                    helper[r][c] = int(matrix[r][c]) + helper[r - 1][c]
        for row in helper:
            ans = max(ans, self.largestRectangleArea(row))
        return ans