class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
            
        hashed = 0
        power = 0
        count = 1
        store = {}
        checker = 0
        for i in range(len(needle)):
            if needle[i] in store:
                continue
            store[needle[i]] = count
            count += 1
        
        for i in range(len(haystack)):
            if haystack[i] in store:
                continue
            store[haystack[i]] = count
            count += 1

        for i in range(len(needle) - 1, -1, -1):
            checker += store[haystack[i]] * (10 ** power)
            hashed += store[needle[i]] * (10 ** power)
            power += 1
        
        power -= 1

        if checker == hashed:
            return 0
        count = 0
        for i in range(len(needle), len(haystack)):
            count += 1

            checker = checker % 10 ** power

            checker = checker * 10 + store[haystack[i]] 

            if checker == hashed:
                return count
        
        return -1