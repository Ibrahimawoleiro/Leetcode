class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for val in range(len(strs)):
            curr =sorted(strs[val])
            curr = "".join(curr)
            if curr not in dic:
                dic[curr] = [strs[val]]
            else:
                dic[curr].append(strs[val])
            
        return list(dic.values())