class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        """
        Reverse all the list in boxTypes
        Sort all list in decending order
        Create a variable unit_count
        Create a variable count that counts the number of boxes we put on the truck
        Create a variable that serves as index and only moves if the curr[1] == 0.
        As you move from index to index, keep adding as long as value of count is less than 
        truckSize
            when count >=truck size:
                break out of the loop
        
        return the value
        """
        
        for List in boxTypes:
            List.reverse()
            
        boxTypes.sort(reverse = True)
        
        unit_count = 0
        count = 0
        index = 0
        
        while count < truckSize and index < len(boxTypes):
            if boxTypes[index][1] > 0:
                unit_count += boxTypes[index][0]
                boxTypes[index][1]-=1
                count+=1
                if boxTypes[index][1] == 0:
                    index+=1
        return unit_count
                