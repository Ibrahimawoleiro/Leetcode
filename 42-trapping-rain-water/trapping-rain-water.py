class Solution:
    def trap(self, height: List[int]) -> int:
        max_right = [0 for _ in range(len(height))]
        max_left = [0 for _ in range(len(height))]
        right_stack = []
        left_stack = []
        total = 0
        def find_right_boundary(index):
            result = height[index]
            while right_stack and height[index] >= right_stack[-1]:
                right_stack.pop()
            if right_stack:
                result = right_stack[-1]
            else:
                right_stack.append(height[index])
            return result

        def find_left_boundary(index):
            result = height[index]
            while left_stack and height[index] >= left_stack[-1]:
                left_stack.pop()
            if left_stack:
                result = left_stack[-1]  
            else:
                left_stack.append(height[index])
            return result
        
        for index in range(len(height)):
            curr = find_left_boundary(index)
            max_left[index] = curr

        for index in range(len(height) - 1, -1, -1):
            curr = find_right_boundary(index)
            max_right[index] = curr

        for index in range(len(height)):
            water_at_curr = min(max_left[index], max_right[index]) - height[index]
            total += water_at_curr
        return total