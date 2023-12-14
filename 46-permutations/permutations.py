class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        marker = []
        self.helper(marker, result, nums)
        return result
    
    def helper(self,marker, result, curr_arr):
        if not curr_arr:
            result.append(marker.copy())
            return

        for val in range(len(curr_arr)):
            current = curr_arr[0]
            marker.append(current)
            copy = curr_arr[1:len(curr_arr)]
            print(copy)
            self.helper(marker, result, copy)
            marker.pop()
            temp = curr_arr.pop(0)
            curr_arr.append(temp)
