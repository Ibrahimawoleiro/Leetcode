class Box:
    def __init__(self, val: int,key:int, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = Box(-100, -1000000)
        self.tail = Box(-100, -1000000)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        curr = self.dic[key]
                
        #Update the most recently used
        #Connecting neighbors
        curr.next.prev = curr.prev
        curr.prev.next = curr.next

        #Appending to head
        head_ = self.head
        last_m_r_u = head_.next

        #Connecting last most recently used to current
        curr.next = last_m_r_u
        last_m_r_u.prev = curr

        #Connecting head to current
        curr.prev = head_
        head_.next = curr

        return curr.val


        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
                #We can input directly
                curr = self.dic[key]
                curr.val = value
                #Update the most recently used

                #Updating neighbors
                curr.next.prev = curr.prev
                curr.prev.next = curr.next

                #Appending to head
                head_ = self.head
                last_m_r_u = head_.next

                #Connecting last most recently used to current
                curr.next = last_m_r_u
                last_m_r_u.prev = curr

                #Connecting head to current
                curr.prev = head_
                head_.next = curr

        #We need to replace the value of seen 
        #Update the most recently used
        else:
            if self.capacity > 0:
                #We can input directly
                curr = Box(value, key)
                self.dic[key] = curr

                #Appending to head
                head_ = self.head
                last_m_r_u = head_.next

                #Connecting last most recently used to current
                curr.next = last_m_r_u
                last_m_r_u.prev = curr

                #Connecting head to current
                curr.prev = head_
                head_.next = curr

                self.capacity -= 1
            else:

                #We can't input directly
                curr = Box(value, key)
                self.dic[key] = curr

                #Remove the least recently used
                l_r_u = self.tail.prev
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev
                
                #Deleting LRU from dictionary
                del self.dic[l_r_u.key]
                
                #Appending to head
                head_ = self.head
                last_m_r_u = head_.next

                #Connecting last most recently used to current
                curr.next = last_m_r_u
                last_m_r_u.prev = curr

                #Connecting head to current
                curr.prev = head_
                head_.next = curr


            
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)