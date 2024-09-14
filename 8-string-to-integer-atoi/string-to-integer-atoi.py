class Solution:
    def whitespace(self,inputs,store, result, index):
        while index < len(inputs) and inputs[index] == " ":
            index += 1
        if index >= len(inputs) or inputs[index] in store:
            return 0
        return self.signedness(inputs, store, result, index)
    def signedness(self,inputs, store, result, index):
        if inputs[index] == '-':
            result += '-'
            index += 1
        elif inputs[index] == '+':
            index += 1
        if index >= len(inputs) or inputs[index] in store:
            return 0
        return self.conversion(inputs, store, result, index)
    def conversion(self,inputs, store, result, index):
        store.add('+')
        store.add('-')
        store.add(' ')
        non_zero_seen = False
        while index < len(inputs) and inputs[index] not in store:
            if non_zero_seen:
                result += inputs[index]
            elif inputs[index] != '0':
                result += inputs[index]
                non_zero_seen = True
            index += 1
        if index >= len(inputs) or inputs[index] in store:
            if len(result) == 0 or (len(result) == 1 and (result[0] == '+' or result[0] == '-')):
                return 0
        return self.rounding(inputs, store, result, index)
    def rounding(self, inputs, store, result, index):
        curr  = int(result)
        print(curr)
        if curr < -2 ** 31:
            return -2 ** 31
        if curr > (2 ** 31)- 1:
            return (2 ** 31) - 1
        return int(curr)
    def myAtoi(self, s: str) -> int:
        store = set([val for val in string.ascii_lowercase])
        store.add('.')
        ans = self.whitespace(s,store,"", 0)
        return ans