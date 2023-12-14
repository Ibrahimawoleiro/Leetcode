class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        marker = []
        self.helper(marker, result, nums)
        return result
    
    def helper(self,marker, result, curr_arr,seen=None):
        if seen == None:
            seen = set()

        if not curr_arr:
            result.append(marker.copy())
            return

        for val in range(len(curr_arr)):
            current = curr_arr[0]
            if current not in seen:
                seen.add(current)
            else:
                temp = curr_arr.pop(0)
                curr_arr.append(temp)
                continue
            marker.append(current)
            print(marker)
            copy = curr_arr[1:len(curr_arr)]
            self.helper(marker, result, copy)
            marker.pop()
            temp = curr_arr.pop(0)
            curr_arr.append(temp)