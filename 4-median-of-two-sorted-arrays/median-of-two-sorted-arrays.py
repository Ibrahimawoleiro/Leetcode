class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        holder=[]
        for num in nums1:
            holder.append(num)
        
        for num in nums2:
            holder.append(num)

        holder.sort()

        if(len(holder) % 2 == 1):
            return holder[floor(len(holder)/2)]

            print(len(holder)/2)
        return (holder[floor(len(holder)/2)] + holder[floor(len(holder)/2)-1])/2