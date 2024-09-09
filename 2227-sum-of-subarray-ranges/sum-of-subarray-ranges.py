class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        '''
        Case 1: [1, 2, 3]
        Subarrays including 1       Subarrays including 2           Subarrays including 3

        [1]            -> 1         [2]       -> 2                  [3]          -> 3
        [1, 2]         -> 1         [2, 3]       -> 2
        [1, 2, 3]      -> 1


        Case 2: [2, 1, 3]
        Subarrays including 1       Subarrays including 2           Subarrays including 3

        [2]         -> 2            [1]         -> 1                [3]          -> 3
        [2, 1]      -> 1            [1, 3]      -> 1
        [2, 1, 3]   -> 1
        '''
        def find_sum_min_subarray(nums):
            sum_of_lsa = 0
            pst = []
            nst = []
            next_smaller = [0 for _ in range(len(nums))]
            prev_smaller = [0 for _ in range(len(nums))]

            def find_smaller_left(index):
                result = 0
                while pst and nums[index] <= pst[-1][0]:
                    pst.pop()
                if pst:
                    result = pst[-1][1] + 1
                pst.append((nums[index] , index))
                return result

            def find_smaller_right(index):
                result = len(nums) - 1
                while nst and nums[index] < nst[-1][0]:
                    nst.pop()
                if nst:
                    result = nst[-1][1] - 1
                nst.append((nums[index] , index))
                return result
            for index in range(len(nums)):
                curr = find_smaller_left(index)
                prev_smaller[index] = curr

            for index in range(len(nums) - 1, -1 , -1):
                curr = find_smaller_right(index)
                next_smaller[index] = curr

            for index in range(len(nums)):
                sum_of_lsa += (index - prev_smaller[index] + 1) * (next_smaller[index] - index + 1) * nums[index]

            return sum_of_lsa

        def find_sum_max_subarray(nums):
            sum_of_msa = 0
            pst = []
            nst = []
            next_larger = [0 for _ in range(len(nums))]
            prev_larger = [0 for _ in range(len(nums))]

            def find_larger_left(index):
                result = 0
                while pst and nums[index] >= pst[-1][0]:
                    pst.pop()
                if pst:
                    result = pst[-1][1] + 1
                pst.append((nums[index] , index))
                return result

            def find_larger_right(index):
                result = len(nums) - 1
                while nst and nums[index] > nst[-1][0]:
                    nst.pop()
                if nst:
                    result = nst[-1][1] - 1
                nst.append((nums[index] , index))
                return result
            for index in range(len(nums)):
                curr = find_larger_left(index)
                prev_larger[index] = curr

            for index in range(len(nums) - 1, -1 , -1):
                curr = find_larger_right(index)
                next_larger[index] = curr

            for index in range(len(nums)):
                sum_of_msa += (index - prev_larger[index] + 1) * (next_larger[index] - index + 1) * nums[index]

            return sum_of_msa

        return find_sum_max_subarray(nums) - find_sum_min_subarray(nums)

            