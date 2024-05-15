import heapq

class Box:
    def __init__(self, key : int, value: int, prev= None, next= None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        #key -> nodes
        self.key_storage = {}

        #node -> frequencies
        self.node_storage = {}

        #min heap
        self.rankings = []

        #rank -> [freq, [head, tail]]
        self.rank_freq = {}

    def get(self, key: int) -> int:
        if key not in self.key_storage:
            return -1
        
        #Get the node at key
        node = self.key_storage[key]

        #Get the current rank where node stands
        prev_curr_rank = self.node_storage[node]

        #Now remove node from prev_curr_rank
        node.prev.next = node.next
        node.next.prev = node.prev

        #Now reduce the count at prev_curr_rank
        self.rank_freq[prev_curr_rank][0] -= 1
        
        #Increase the number of operations on that node in Node Storage
        curr_rank = prev_curr_rank + 1

        self.node_storage[node] = curr_rank

        #Now append node to curr rank list
        if curr_rank in self.rank_freq:
            #Add to curr_rank group of nodes
            curr_rank_arr = self.rank_freq[curr_rank]
            #Increase the curr_rank count
            curr_rank_arr[0] += 1
            #Get the head of current arr to curr to the linkedlist at curr_rank
            head_ = curr_rank_arr[1][0]
            next_ = head_.next
            node.next = next_
            next_.prev = node
            node.prev = head_
            head_.next = node
        #If the rank is absent in the ranking

        else:
            #Create a new head, tail,and freq count for the current rank
            new_rank_freq = [1,self.head_tail_factory()]
            head_ = new_rank_freq[1][0]
            tail_ = new_rank_freq[1][1]
            node.next = tail_
            tail_.prev = node
            node.prev = head_
            head_.next = node
            self.rank_freq[curr_rank] = new_rank_freq

            #Add the new rank to rankings
            heapq.heappush(self.rankings, curr_rank) 
        
        return node.value

    def put(self, key: int, value: int) -> None:
        #If the key is already seen 

        if key in self.key_storage:
            #Get the node at key
            curr = self.key_storage[key]
            curr.value = value
            #Update the number of operations done on current key
            prev_curr_rank = self.node_storage[curr]

            #Now reduce the count at prev_curr_rank
            self.rank_freq[prev_curr_rank][0] -= 1
            
            #Now remove curr from prev_curr_rank
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            #Prevent memory leakages
            curr.prev = None
            curr.next = None
            #Add it to curr_rank. That is update the number of operations on the node
            curr_rank = prev_curr_rank + 1
            self.node_storage[curr] = curr_rank
            #If the rank is present in the ranking
            if curr_rank in self.rank_freq:
                #Add to curr_rank group of nodes
                curr_rank_arr = self.rank_freq[curr_rank]
                #Increase the curr_rank count
                curr_rank_arr[0] += 1
                #Get the head of current arr to curr to the linkedlist at curr_rank
                head_ = curr_rank_arr[1][0]
                next_ = head_.next
                curr.next = next_
                next_.prev = curr
                curr.prev = head_
                head_.next = curr
            #If the rank is absent in the ranking
            else:
                #Create a new head, tail,and freq count for the current rank
                new_rank_freq = [1,self.head_tail_factory()]
                head_ = new_rank_freq[1][0]
                tail_ = new_rank_freq[1][1]
                curr.next = tail_
                tail_.prev = curr
                curr.prev = head_
                head_.next = curr
                self.rank_freq[curr_rank] = new_rank_freq

                #Add the new rank to rankings
                heapq.heappush(self.rankings, curr_rank)

        #If it is a new key 
        else:
            #If there is space
            if self.capacity > 0:
                #You can add directly without removing anything
                #Create the new box to add
                new_box = Box(key, value)
                #Add new_box to node_storage with count of 1
                self.node_storage[new_box] = 1
                self.key_storage[key] = new_box
                #Add the new_box to the rank of 1 if it is present
                if 1 in self.rank_freq:
                    #Get it and add new box to its linked list
                    one_rank_arr = self.rank_freq[1]
                    #Add box to one
                    head_ = one_rank_arr[1][0]
                    next_ = head_.next
                    new_box.next = next_
                    next_.prev = new_box
                    new_box.prev = head_
                    head_.next = new_box
                    #Increase the count at 1
                    one_rank_arr[0] += 1

                #If 1 is not in self.rank_freq
                else:
                    new_rank_freq = [1,self.head_tail_factory()]
                    head_ = new_rank_freq[1][0]
                    tail_ = new_rank_freq[1][1]
                    new_box.next = tail_
                    tail_.prev = new_box
                    new_box.prev = head_
                    head_.next = new_box
                    self.rank_freq[1] = new_rank_freq
                    #Add the new rank to rankings
                    heapq.heappush(self.rankings, 1)
                self.capacity -= 1
                    
            #If there's no space
            else:
                #Remove the LFU
                while(True):
                    #Get the lowest rank from rankings -> This is the number
                    lowest_rank = heapq.heappop(self.rankings)
                    if self.rank_freq[lowest_rank][0] <= 0:
                        del self.rank_freq[lowest_rank]
                        continue
                    else:
                        #This is the node itself
                        lowest_ranker = self.rank_freq[lowest_rank]
                        #Remove LFU from where it is in rank
                        tail_ = lowest_ranker[1][1]
                        l_f_u = tail_.prev
                        tail_.prev = l_f_u.prev
                        l_f_u.prev.next = tail_

                        #Remove lfu key from key storage 
                        if l_f_u.key in self.key_storage:
                            del self.key_storage[l_f_u.key]
                        #Remove lfu from node storage
                        if l_f_u in self.node_storage:
                            del self.node_storage[l_f_u]

                        #Prevent memory leakages
                        l_f_u.prev = None
                        l_f_u.next = None
                        #Reduce the count of lowest_ranker
                        lowest_ranker[0] -= 1
                        #if the freq of the rank is now zero, remove from the rank_freq
                        #and don't replace in rankings
                        if lowest_ranker[0] <= 0:
                            del self.rank_freq[lowest_rank]
                        else:
                            heappush(self.rankings, lowest_rank)

                        #Create the new box to add
                        new_box = Box(key, value)
                        #Add new_box to node_storage with count of 1
                        self.node_storage[new_box] = 1
                        self.key_storage[key] = new_box
                        #Add the new_box to the rank of 1 if it is present
                        if 1 in self.rank_freq:
                            #Get it and add new box to its linked list
                            one_rank_arr = self.rank_freq[1]
                            #Add box to one
                            head_ = one_rank_arr[1][0]
                            next_ = head_.next
                            new_box.next = next_
                            next_.prev = new_box
                            new_box.prev = head_
                            head_.next = new_box
                            #Increase the count at 1
                            one_rank_arr[0] += 1
                        
                        #If 1 is not in self.rank_freq
                        else:
                            new_rank_freq = [1,self.head_tail_factory()]
                            head_ = new_rank_freq[1][0]
                            tail_ = new_rank_freq[1][1]
                            new_box.next = tail_
                            tail_.prev = new_box
                            new_box.prev = head_
                            head_.next = new_box
                            self.rank_freq[1] = new_rank_freq

                            #Add the new rank to rankings
                            heapq.heappush(self.rankings, 1)

                        break

    def head_tail_factory(self):
        head = Box(-1,-100000)
        tail = Box(-1,-100000)
        head.next = tail
        tail.prev = head
        return [head, tail]


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)