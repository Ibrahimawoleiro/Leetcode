class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # #Approach1
        arr1 = []
        arr2 = []
        def helper(string, array):
            for val in string:
                if val == "#" and len(array) > 0:
                    array.pop()
                elif val != '#':
                    array.append(val)
            return array

        return helper(s,arr1) == helper(t,arr2)
                