class Solution:
    def isValid(self, s: str) -> bool:
        checker = []
        for val in s:
            print(1)
            if val == "(" or val =="{" or val == "[":
                checker.append(val)
           
            elif val == "}" or val=="]" or val ==")":
                print("kldsnkdskl")
                if not checker:
                    return False
                end_of_stack = checker.pop()
                print(end_of_stack, val)
                if end_of_stack == "{" and val == "}" or end_of_stack == "(" and val == ")" or end_of_stack == "[" and val == "]":
                    print(end_of_stack, val)
                    continue
                else:
                    return False

        return not checker