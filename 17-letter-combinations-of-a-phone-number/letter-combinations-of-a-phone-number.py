class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {
            "2":'abc',
            "3":'def',
            "4":'ghi',
            "5":'jkl',
            "6":'mno',
            "7":'pqrs',
            "8":'tuv',
            "9":'wxyz'
        }

        arr = []
        ans = []
        for val in digits:
            arr.append(dictionary[val])
        
        def helper(combination,index):
            if index == len(digits):
                if len(combination) > 0:
                    ans.append(combination)
                return 
            for val in arr[index]:
                combination = combination + val
                helper(combination , index + 1)
                combination = combination[:-1]

        helper("",0)
        return ans



