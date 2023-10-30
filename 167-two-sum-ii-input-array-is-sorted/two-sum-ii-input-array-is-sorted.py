class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        end = len(numbers)-1
        beginning = 0

        while(beginning < end):
            if numbers[beginning] + numbers[end] == target:
                return [beginning+1,end+1]

            if numbers[beginning] + numbers[end] > target:
                end -=1

            if numbers[beginning] + numbers[end] < target:
                beginning +=1
