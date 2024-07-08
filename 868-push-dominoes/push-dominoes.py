import queue
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        q = queue.Queue()
        for index in range(len(dominoes)):
            if dominoes[index] == 'R' or dominoes[index] =='L':
                q.put((dominoes[index], index))
        q.put(None)
        c = list(dominoes)
        #Indexes to be changed and what to
        arr = []
        while not q.empty():

            curr = q.get()

            if curr == None:
                for coordinate in arr:
                    index = coordinate[1]
                    val = coordinate[0]
                    c[index] = val
                arr = []
                if q.empty():
                    break
                else:
                    q.put(None)
                
            else:
                action = curr[0]
                position = curr[1]

                if action == 'L':
                    if position == 0:
                        continue
                    if position == 1:
                        if c[position - 1] == '.':
                            arr.append(('L',position - 1))
                            q.put(('L', position - 1))
                    else:
                        if c[position - 2] != 'R' and c[position - 1] == '.':
                            arr.append(('L', position - 1))
                            q.put(('L', position - 1))
                else:
                    if position == len(dominoes) - 1:
                        continue
                    if position == len(dominoes) - 2 and c[position + 1] == '.':
                        arr.append(('R',position + 1))
                        q.put(('L', position + 1))
                    else:
                        if position + 2 < len(c) and c[position + 2] != 'L' and c[position + 1] == '.':
                            arr.append(('R', position + 1))
                            q.put(('R', position + 1))

        return ''.join(c)