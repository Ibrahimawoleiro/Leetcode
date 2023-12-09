class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # #Approach1
        # for val in range(len(letters)):
        #     if letters[val] > target:
        #         return letters[val]
        
        # return letters[0]

        #Approach2
        front = 0
        back = len(letters) - 1
        first_greater = 0
        while front <= back:
            mid = int((front + back ) / 2)
            print(mid)
            if(letters[mid] == target):
                front= mid + 1
            if letters[mid] > target:
                first_greater = mid
                back = mid - 1
            elif letters[mid] < target:
                front = mid + 1
        
        return letters[first_greater]
