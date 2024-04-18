class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        s = [False for index in range(len(arr))]
        p = [False for index in range(len(arr))]

        for index in range(len(arr)):
            if index == 0:
                s[index] = True
                continue
            if s[index - 1] == False:
                s[index] = False
                continue
            if arr[index] > arr[index - 1]:
                s[index] = True

        for index in range(len(arr) - 1 , -1, -1):
            if index == len(arr) - 1:
                p[len(arr) - 1] = True
                continue
            if p[index + 1] == False:
                p[index] = False
                continue
            if arr[index] > arr[index + 1]:
                p[index] = True
            
        for index in range(len(arr)):
            if index == 0 or index == len(arr) - 1:
                continue
            if s[index] and p[index]:
                return True
        return False