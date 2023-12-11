class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        arr_s = []
        arr_t = []

        for val in s:
            if val !='#':
                arr_s.append(val)
            else:
                if len(arr_s) != 0:
                    arr_s.pop()
        
        for val in t:
            if val !='#':
                arr_t.append(val)
            else:
                if len(arr_t) != 0:
                    arr_t.pop()

        return arr_s == arr_t