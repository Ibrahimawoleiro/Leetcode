class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        m = 0

        left = 0

        right = len(removable) - 1

        while left <= right:

            s_runner = 0

            p_runner = 0

            mid = (left + right) // 2

            curr_skip = removable[0 : mid + 1]
            store = set(sorted(removable[0 : mid + 1]))
            
            while s_runner < len(s) and p_runner < len(p):
                if s_runner in store:
                    s_runner += 1
                    continue
                if s[s_runner] == p[p_runner]:
                    s_runner += 1
                    p_runner += 1
                else:
                    s_runner += 1
            
            if p_runner == len(p):
                if mid + 1 > m:
                    m = mid + 1
                left = mid + 1
            else:
                right = mid - 1


        return m
