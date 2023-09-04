class Solution:
    def countElements(self, arr: List[int]) -> int:
        dict = {}
        for num in arr:
            if num in dict:
                dict[num]+=1
                continue
            dict[num]=1
        
        ans = 0
        
        for key in dict.keys():
            if key+1 in dict:
                ans+=dict[key]
                
        
        return ans
            