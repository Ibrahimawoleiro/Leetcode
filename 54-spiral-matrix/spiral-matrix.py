class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = 0
        r = len(matrix[0]) - 1
        u = 0
        d = len(matrix) - 1
        arr = []
        while(l<=r):
            i = l
            j=u

            while(i <= r):

                arr.append(matrix[j][i])
                if i == r:
                    break
                i+=1
            j = u + 1
            if(j>d):
                break
            while(j <= d):

                arr.append(matrix[j][i])
                if j==d:
                    break
                j+=1
            i-=1
            if i<l:
                break
            while(i>= l):
                print(i,l)
                arr.append(matrix[j][i])
                if i==l:
                    break
                i-=1
            j-=1

            if(j<=u):
                break
            while(j>=u+1):

                arr.append(matrix[j][i])
                if j==u+1:
                    break
                j-=1

            l+=1
            r-=1
            u+=1
            d-=1

        return arr
            
