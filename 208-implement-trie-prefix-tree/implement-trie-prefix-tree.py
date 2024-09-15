class Box:
    def __init__(self):
        self.array = [None for _ in range(26)]
        self.flag = False

class Trie:

    def __init__(self):
        self.box = Box()

    def insert(self, word: str) -> None:
        current = self.box
        i = 0
        while i < len(word):
            letter = word[i]
            #Position to place the new Box
            pos = ord(letter) - ord('a')
            #If there's already a box present
            if current.array[pos]:
                current = current.array[pos]
            #If there isn't a box present
            else:
                new_box = Box()
                current.array[pos] = new_box
                current = current.array[pos]
            i += 1
        current.flag = True

    def search(self, word: str) -> bool:
        current = self.box
        i = 0
        while i < len(word):
            letter = word[i]
            #Position to place the new Box
            pos = ord(letter) - ord('a')
            #If there's already a box present
            if current.array[pos]:
                current = current.array[pos]
            #If there isn't a box present
            else:
                return False
            i += 1
        return current.flag

    def startsWith(self, prefix: str) -> bool:
        word = prefix
        current = self.box
        i = 0
        while i < len(word):
            letter = word[i]
            #Position to place the new Box
            pos = ord(letter) - ord('a')
            #If there's already a box present
            if current.array[pos]:
                current = current.array[pos]
            #If there isn't a box present
            else:
                return False
            i += 1
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)