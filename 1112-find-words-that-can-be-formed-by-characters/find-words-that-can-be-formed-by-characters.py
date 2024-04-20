class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        store = {}
        for index in range(len(chars)):
            if chars[index] not in store:
                store[chars[index]] = 1
            else:
                store[chars[index]] += 1
        print(store)
        total = 0
        for word in words:
            curr_store = store.copy()
            i = 0
            while(i < len(word)):
                if word[i] not in curr_store:
                    break
                else:
                    curr_store[word[i]]-=1
                    if curr_store[word[i]] == 0:
                        del curr_store[word[i]]
                i+=1
            if i == len(word):
                total += len(word)
        return total
