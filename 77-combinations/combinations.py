class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [num + 1 for num in range(n)]
        result = []
        marker = []
        self.helper(result, marker, arr, k, set())
        return result

    def helper(self, result, marker, arr, k, seen):
        if len(marker) == k:
            sorted_marker = tuple(sorted(marker))
            if sorted_marker not in seen:
                seen.add(sorted_marker)
                result.append(marker.copy())
            return

        for index in range(len(arr)):
            current = arr[index]
            marker.append(current)
            self.helper(result, marker, arr[index+1:], k, seen)
            marker.pop()