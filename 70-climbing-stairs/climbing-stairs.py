class Solution:
    def climbStairs(self, n: int) -> int:
        # #Approach 1
        # dictionary = {
        #     0:1,
        #     1:1
        # }

        # for val in range(n+1):
        #     if val in dictionary:
        #         continue
        #     dictionary[val] = dictionary[val-1] + dictionary[val-2]
        
        # return dictionary[n] if n in dictionary else 0


        # #Approach 2
        # arr = [0 for val in range(n+1)]
        # arr[0] = 1
        # arr[1] = 1

        # for val in range(n+1):
        #     if val == 0 or val == 1:
        #         continue
            
        #     arr[val] = arr[val - 1] + arr[val - 2]

        # return arr[n]

        #Approach 3
        current = 1
        previous = 1
        
        for val in range(n+1):
            if val == 0 or val == 1:
                continue
            
            temp = current
            current = previous + current
            previous = temp

        return current


        