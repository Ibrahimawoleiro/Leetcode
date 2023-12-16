class Solution:
    def rob(self, nums: List[int]) -> int:
        dictionary = {}

        def helper(index):
            if index + 2 >= len(nums) or index in dictionary:
                if index in dictionary:
                    return dictionary[index]
                if index + 2 >= len(nums):
                    dictionary[index] = nums[index]
                    return dictionary[index]
            
            max_sum = nums[index]

            for val in range(index + 2, len(nums)):

                temp = helper(val)
                max_sum += temp
                print(temp, index, max_sum)
                if index not in dictionary or max_sum > dictionary[index]:
                    print('lion',max_sum)
                    print(temp, index, max_sum)
                    dictionary[index] = max_sum
                    print(dictionary[index],'fhjknhbh')
                max_sum -= temp
            
            return dictionary[index]

        for val in range(0, len(nums)):
            helper(val)

        print(dictionary)

        if 0 in dictionary and 1 in dictionary:
            if dictionary[0] > dictionary[1]:
                return dictionary[0]
            else:
                return dictionary[1]
        if 0 in dictionary:       
            return dictionary[0]
        

