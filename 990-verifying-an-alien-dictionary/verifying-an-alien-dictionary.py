class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create a dictionary to store the order of characters
        alien_order = {char: i for i, char in enumerate(order)}
        
        # Compare each pair of adjacent words
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            # Compare characters in corresponding positions
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if alien_order[word1[j]] > alien_order[word2[j]]:
                        return False  # The order is violated
                    break  # No need to compare further, move to the next pair
            
            # If one word is a prefix of the other, it should come before in sorted order
            else:
                if len(word1) > len(word2):
                    return False  # The order is violated
        
        # All words are sorted according to the alien alphabet
        return True