class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t) or s and not t:
            return False
        if not s and t:
            return True
        s_pointer = 0
        t_pointer = 0

        while(t_pointer < len(t)):
            if s[s_pointer] == t[t_pointer]:
                s_pointer +=1
                if s_pointer >= len(s):
                    return True
            t_pointer+=1
        return s_pointer >= len(s)