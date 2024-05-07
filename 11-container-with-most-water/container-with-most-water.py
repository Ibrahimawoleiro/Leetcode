class Solution:
    def maxArea(self, height: List[int]) -> int:
        # #Brute force
        # #This is the maximum area seen so far
        # m=0
        # #loop through the array
        # for left in range(len(height)):
        #     #loop through every right border for left
        #     for right in range(left + 1, len(height)):
        #         #distance
        #         d = right - left
        #         #height
        #         h = min(height[left], height[right])

        #         #current area
        #         curr = d * h

        #         if curr > m:
        #             m = curr
        # return m

        #maximize height and distance
        l = 0
        r = len(height) - 1
        m = 0
        while(l < r):
            #distance 
            d = r - l
            # height
            h = min(height[l], height[r])
            #current area
            curr = d * h
            if curr > m:
                m = curr
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return m

