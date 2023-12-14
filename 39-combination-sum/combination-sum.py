class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        seen = set()
        self.helper(target, candidates, result, curr, 0, seen)
        return result

    def helper(self, target, checker, main, curr, total, seen):
        if total >= target:
            temp = tuple(sorted(curr))
            if total == target and  temp not in seen:
                seen.add(temp)
                main.append(curr.copy())
            return
        print(curr)
        for val in checker:
            curr.append(val)
            total += val
            self.helper(target,checker, main, curr, total, seen)
            total -= curr.pop()
            