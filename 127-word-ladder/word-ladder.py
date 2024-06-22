import queue
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = queue.Queue()
        store = set(wordList)
        q.put((beginWord, 1))
        count = 0
        while(not q.empty()):
            curr = q.get()
            if curr[0] == endWord:
                return curr[1]
            word = list(curr[0])
            count = curr[1]
            for i in range(len(word)):
                l = word[i]
                for ch in string.ascii_lowercase:
                    word[i] = ch
                    result = ''.join(word)
                    if result in store:
                        q.put((result, count+1))
                        store.remove(result)
                word[i] = l
        return 0