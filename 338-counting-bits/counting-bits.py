class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0 for val in range(n+1)]
        power = -1
        target = 0
        for index in range(len(arr)):
            if index == 0:
                continue
            if index == 2 ** target:
                power+=1
                target+=1
            arr[index] = arr[index - 2 ** power] + 1
            
             
        
        return arr
            