class Solution:
    def largestGoodInteger(self, num: str) -> str:
        store = ['999', '888','777','666','555','444','333','222','111','000']

        for numb in store:
            if numb in num:
                return numb

        return ''

                