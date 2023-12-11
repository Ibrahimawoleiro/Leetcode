class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) / n != m:
            return []
        result = []
        holder = []

        for val in original:
            holder.append(val)
            if len(holder) == n:
                result.append(holder)
                holder = []
        
        return result