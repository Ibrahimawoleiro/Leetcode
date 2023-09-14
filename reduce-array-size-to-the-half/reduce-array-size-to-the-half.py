class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        """
        Create a dictionary to keep track of the frequency of the numbers seen
        Get the value of the frequency into a List called values
        Now sort the list in descending order
        Create a variable len of arr called length
            Then subtract each index from length as long as length >0 while keeping count 

        """
        
        dic = {}
        
        for num in arr:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        
        values = list(dic.values())
        values.sort(reverse = True)
        print(values)
        count = 0
        length = round(len(arr)/2)
        
        for val in values:
            length -= val
            count+=1
            if length <=0:
                return count