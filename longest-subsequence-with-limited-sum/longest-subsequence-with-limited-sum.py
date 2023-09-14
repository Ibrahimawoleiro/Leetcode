class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        result=[]
        for val in range(len(nums)):
            if val == 0:
                ans.append(nums[0])
                continue
            ans.append(ans[-1]+nums[val])
            
        #print(ans)
        #print(queries)
            
        for index in range(len(queries)):
            #print(list(range(len(queries))))
            #print("kkkk")
            right = len(ans)-1
            left = 0
            mid = 0
            saver = mid
            while(left <= right):
                print(mid,"jk")
                mid = int((left + right)/2)
                if mid >= len(nums):
                    break
                if ans[mid] == queries[index]:
                    result.append(mid+1)
                    break;
                if ans[mid] > queries[index]:
                    right = mid - 1
                elif ans[mid] < queries[index]:
                    left = mid + 1
                #print(index)
                print(mid)
            if  ans[mid] != queries[index]:
                result.append(left)
                
        return result