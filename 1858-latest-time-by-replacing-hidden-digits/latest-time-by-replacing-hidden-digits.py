class Solution:
    def maximumTime(self, time: str) -> str:
        x = list(time)
        if x[0] == '?' and x[1] == '?':
            x[0] = '2'
            x[1] = '3'
        elif x[0] == "?":
            if int(x[1]) <= 3:
                x[0] = '2'
            else:
                x[0] = '1'
        elif x[1] == "?":
            if int(x[0]) == 2:
                x[1] = '3'
            else:
                x[1] = '9'

        
        if x[-1] == '?' and x[-2] == '?':
            x[-1] = '9'
            x[-2] = '5'
        elif x[-2] == "?":
            x[-2] = '5'
        elif x[-1] == "?":
            x[-1] = '9'
        

        return ''.join(x)

        