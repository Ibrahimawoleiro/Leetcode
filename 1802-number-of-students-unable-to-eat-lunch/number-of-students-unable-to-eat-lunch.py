class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        c = 0
        s = 0

        for val in students:
            if val == 0:
                c+=1
            
            else:
                s += 1
        
        for val in sandwiches:
            if val == 0 and c == 0 or val == 1 and s == 0:
                return c + s
            
            elif val == 0:
                c -= 1
            else:
                s -= 1
        return c + s
