class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        if k < arr[0]:
            return k
         
        left_boundary = 0

        right_boundary = len(arr) - 1

        floor_index = len(arr) - 1

        while left_boundary <= right_boundary:

            current = (left_boundary + right_boundary) //  2

            if arr[current] - (current + 1) < k:

                floor_index = current

                left_boundary = current + 1 

            else:

                right_boundary = current - 1

        missing = k - (arr[floor_index] - (floor_index + 1)) 

        return arr[floor_index] + missing

