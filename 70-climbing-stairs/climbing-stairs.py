class Solution:
    def climbStairs(self, n: int) -> int:
        # Approach 1
        # if n==1:
        #     return 1
        # if n==2:
        #     return 2

        # arr = [0 for number in range(n)]

        # arr[0] = 1

        # arr[1] = 2
  
        # for num in range(n):
        #     print(arr, num)
        #     if num == 0 or num == 1:
        #         continue

        #     arr[num] = arr[num-1] + arr[num-2]
        # return arr[n-1]

        if n==1:
            return 1
        if n==2:
            return 2
        dictionary = {}

        for val in range(n):
            if val == 0 or val == 1:
                dictionary[val+1] = val + 1
            else:
                dictionary[val+1] = dictionary[val] + dictionary[val - 1]
        
        return dictionary[n]

        