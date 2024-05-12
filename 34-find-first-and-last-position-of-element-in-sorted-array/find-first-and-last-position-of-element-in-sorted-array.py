class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        def lower(start , end, pos):
            while(start <= end):
                #Looking if the number exist in the array
                if pos == -1:
                    mid = (start + end) // 2

                    if nums[mid] == target:
                        pos = mid
                        end = mid - 1
                    elif nums[mid] < target:
                        start = mid + 1
                    else:
                        end = mid - 1
                #Looking for the starting point
                else:
                    mid = (start + end) // 2
                    if nums[mid] == target:
                        pos = mid
                        end = mid - 1
                        print(pos, end)
                    elif nums[mid] < target:
                        start = mid + 1
                    else:
                        end = mid - 1
            return pos
        def upper(start, end , pos):
            while(start <= end):
                #Looking if the number exist in the array
                if pos == -1:
                    mid = (start + end) // 2

                    if nums[mid] == target:
                        pos = mid
                        start = mid + 1
                    elif nums[mid] < target:
                        start = mid + 1
                    else:
                        end = mid - 1
                #Looking for the ending point
                else:
                    mid = (start + end) // 2
                    if nums[mid] == target:
                        pos = mid
                        start = mid + 1
                    elif nums[mid] < target:
                        start = mid + 1
                    else:
                        end = mid - 1
            return pos
        start = lower(0,len(nums) - 1, -1)
        if start == -1:
            return [-1, -1]
        end = upper(0, len(nums) - 1, -1)

        return [start, end]


