class Solution:
    def brute_force(self,s, k):
        #We use each index as a start point while making sure that we do not replace more than k letters
            #So we need to keep track of the letter with the maximum frequency to know how many replacement we made
            #when we've made more replacement than we are allowed, we stop for the current start point
        ans = 0
        for start_point in range(len(s)):
            index = start_point
            max_freq = 0
            tracker = [0 for _ in range(26)]
            while index < len(s):
                curr = s[index]
                tracker[ord(s[index]) - ord('A')] += 1
                max_freq = max(max_freq, tracker[ord(s[index]) - ord('A')])
                subarr_length = index - start_point + 1
                if subarr_length - max_freq > k:
                    break
                ans = max(ans, subarr_length)
                index += 1
        return ans

    def optimized(self,s, k):
        # The first optimization that we can do is to not have to go back in our traversals
            # We can prevent this by using a two pointer approach
            # But this would mean that we would need to loop through the tracker array to find the letter with max freq in the array
        ans = 0
        left = 0
        right = 0
        max_freq = 0
        tracker  = [0 for _ in range(26)]
        while right < len(s):
            tracker[ord(s[right]) - ord('A')] += 1
            max_freq = max(max_freq, tracker[ord(s[right]) - ord('A')])
            subarr_length = right - left + 1
            while subarr_length - max_freq > k:
                print('kkkk')
                tracker[ord(s[left]) - ord('A')] -= 1
                left += 1
                subarr_length = right - left + 1
                max_freq = max(tracker)
            ans = max(ans , subarr_length)
            right += 1
        return ans
            
    def characterReplacement(self, s: str, k: int) -> int:
        return self.optimized(s, k)