class Solution:
    def countBits(self, n: int) -> List[int]:
        #Approach1
        arr = [0 for num in range(n+1)]

        for val in range(len(arr)):
           
            temp = val
            one_count = 0
            while(temp > 0):
                if(temp % 2 ==1):
                    one_count+=1
                temp= int(temp/2)
                print(temp)
            
            arr[val] = one_count

        return arr