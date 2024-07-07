from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        # Prefix sums for the first and second rows
        prefix1 = [0] * (n + 1)
        prefix2 = [0] * (n + 1)

        for i in range(n):
            prefix1[i + 1] = prefix1[i] + grid[0][i]
            prefix2[i + 1] = prefix2[i] + grid[1][i]

        # Initializing minimum score the second robot can be forced to get
        min_second_robot_score = float('inf')

        for i in range(n):
            # The second robot's possible scores after the first robot picks up (i + 1)-th cell
            score_top = prefix1[n] - prefix1[i + 1]  # score if the second robot goes through the top row after i-th cell
            score_bottom = prefix2[i]  # score if the second robot goes through the bottom row before i-th cell

            # The second robot will choose the path giving the maximum score out of the two
            second_robot_score = max(score_top, score_bottom)
            
            # Minimize the maximum score the second robot can get
            min_second_robot_score = min(min_second_robot_score, second_robot_score)

        return min_second_robot_score
