class Solution:
    def countBits(self, n: int) -> List[int]:
        # #Approach1
        # arr = [0 for num in range(n+1)]

        # for val in range(len(arr)):
           
        #     temp = val
        #     one_count = 0
        #     while(temp > 0):
        #         if(temp % 2 ==1):
        #             one_count+=1
        #         temp= int(temp/2)
            
        #     arr[val] = one_count

        # return arr

        #Approach2
        arr = [0 for num in range(n+1)]
        time_to_change = 2
        checker = 0
        for val in range(n+1):
            if val == 0 or val == 1:
                arr[val] = val
                continue
            if val == time_to_change:
                time_to_change*=2
                checker+=1 
            arr[val] = 1 + arr[val - 2**checker]
        
        return arr