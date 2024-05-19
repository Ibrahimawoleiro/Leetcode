class Box:
    def __init__(self):
        self.alphabets = [None for num in range(26)]
        self.e = False

class Trie:

    def __init__(self):
        self.box = Box()

    def insert(self, word: str) -> None:
        curr = self.box
        for l in word:
            index = ord(l) - ord('a')
            if not curr.alphabets[index]:
                curr.alphabets[index] = Box()
                curr = curr.alphabets[index]
            else:
                curr = curr.alphabets[index]

        curr.e = True


    def search(self, word: str) -> bool:
        curr = self.box
        for l in word:
            index = ord(l) - ord('a')
            if not curr.alphabets[index]:
                return False
            else:
                curr = curr.alphabets[index]

        return curr.e

    def startsWith(self, prefix: str) -> bool:
        curr = self.box
        for l in prefix:
            index = ord(l) - ord('a')
            if not curr.alphabets[index]:
                return False
            else:
                curr = curr.alphabets[index]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)