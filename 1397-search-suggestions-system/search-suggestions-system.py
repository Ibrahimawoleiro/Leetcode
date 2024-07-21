class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        """
        Sort the products so that words with similar prefix can appear closer to each other.
        For each letter in the searchWord:
            Get the range of words that have the same prefix as searchWord up to letter,
                If the range consist of more than or equal to 3:
                    return 3 among them
                else:
                    return only the ones that match
                
            Then shrink the search to only this words

        """

        products.sort()
        s = 0
        e = len(products) - 1
        ans = []
        for index in range(len(searchWord)):
            l = s
            r = e
            range_start = len(products)
            while l <= r:

                mid = (l + r) // 2
                
                if index < len(products[mid]) and searchWord[index] == products[mid][index]:
                    if mid < range_start:
                        range_start = mid
                    r = mid - 1
                elif index < len(products[mid]) and ord(searchWord[index]) < ord(products[mid][index]):
                    r = mid - 1

                else:
                    l = mid + 1
            if range_start == len(products):
                for i in range(index, len(searchWord)):
                    ans.append([])
                break
            l = s
            r = e
            range_end = -1
            while l <= r:

                mid = (l + r) // 2
                
                if index < len(products[mid]) and searchWord[index] == products[mid][index]:
                    if mid > range_end:
                        range_end = mid
                    l = mid + 1
                elif index < len(products[mid]) and ord(searchWord[index]) < ord(products[mid][index]):
                    r = mid - 1

                else:
                    l = mid + 1
            
            s = range_start
            e = range_end

            if (e - s) + 1 >= 3:
                ans.append(products[s:s+3])
            else:
                ans.append(products[s : e + 1])

        return ans