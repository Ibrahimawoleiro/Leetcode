# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []

        dic = {}

        for node in lists:
            while(node):
                next_ = node.next
                node.next = None
                if node.val not in dic:
                    dic[node.val] = []
                    dic[node.val].append(node)
                    heapq.heappush(heap, node.val)
                else:
                    dic[node.val].append(node)
                node = next_
        
        print(dic)

        ans = ListNode()
        itr = ans
        while(heap):
            curr = heapq.heappop(heap)
            while(len(dic[curr]) > 0):
                itr.next = dic[curr].pop()
                itr = itr.next
            del dic[curr]

        print(ans.val)

        return ans.next
            