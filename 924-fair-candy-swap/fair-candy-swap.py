class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)

        aliceSizes.sort()
        bobSizes.sort()

        i = len(aliceSizes) - 1
        j = len(bobSizes) - 1

        while(i >= 0 and j >= 0):
            if alice_sum - aliceSizes[i] + bobSizes[j] == bob_sum - bobSizes[j] + aliceSizes[i]:
                return [aliceSizes[i], bobSizes[j]]
            elif alice_sum - aliceSizes[i] + bobSizes[j] > bob_sum - bobSizes[j] + aliceSizes[i]:
                j-=1
            else:
                i-=1
        
        return []

