class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        #For each index, find the index of the smaller val to the left
        #For each index, find the index of the smaller val to the right
        #Each index to the left is a potential start index while each index to the right
        #is a potential end index. So me multiply the length of start index to end index
        left_boundary = [index for index in range(len(arr))]
        right_boundary = [index for index in range(len(arr))]
        min_left_stack = []
        min_right_stack = []
        total = 0
        MOD = 10**9 + 7

        def find_left_boundary(index):
            #Try to find the index with the lower val than curr
            #If such an index cannot be found, put index 0 for the left boundary
            result = 0
            while min_left_stack and arr[index] <= min_left_stack[-1][0]:
                min_left_stack.pop()
            if min_left_stack:
                result = min_left_stack[-1][1] + 1
            min_left_stack.append((arr[index] , index))
            return result

        def find_right_boundary(index):
            result = len(arr) - 1
            while min_right_stack and arr[index] < min_right_stack[-1][0]:
                min_right_stack.pop()
            if min_right_stack:
                result = min_right_stack[-1][1] - 1
            min_right_stack.append((arr[index], index))  
            return result

        for index in range(len(arr)):
            left_boundary[index] = find_left_boundary(index)

        for index in range(len(arr) - 1, - 1, -1):
            right_boundary[index] = find_right_boundary(index)

        print(left_boundary)
        print(arr)
        print(right_boundary)
        for index in range(len(arr)):
            start_points = (index - left_boundary[index]) + 1
            end_points = (right_boundary[index] - index) + 1
            num_of_subarr = start_points * end_points
            curr_total = num_of_subarr * arr[index]
            total = (total + curr_total) % MOD
        return total
        return 0   