class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        store = {}
        def helper(r,i, store):
            if r >= len(triangle):
                return 0
            if (r, i) in store:
                return store[(r, i)]
            for index in range(i,i + 1):
                curr = triangle[r][index]
                min_path = curr + min(helper(r+1, i,store), helper(r+1, i+1,store))
                store[(r, index)] = min_path

            return store[(r, i)]

        ans = helper(0, 0, store)
        print(store)
        return ans

        # [-1],
        # [2,3],
        #[1,-1,-3]
                    