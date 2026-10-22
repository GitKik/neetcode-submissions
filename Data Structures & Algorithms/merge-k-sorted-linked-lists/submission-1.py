# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq 

class TupleList: 
    def __init__(self, index:int, list_node:Optional[ListNode]):
        self.index = index
        self.list_node = list_node

    def __cmp__(self, other):
        return cmp(self.index, other.index)
    def __lt__(self, other):
        return self.index < other.index
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for list_ in lists :
            heapq.heappush(h, TupleList(list_.val, list_.next))
        temp_list = []
        while h :
            tuple_list = heapq.heappop(h)
            if tuple_list.list_node : 
                heapq.heappush(h, TupleList(tuple_list.list_node.val, 
                                            tuple_list.list_node.next))
            temp_list.append(tuple_list.index)
        list_node = None
        for elem in temp_list[::-1] :
            previous = list_node
            list_node = ListNode(elem, previous)
        return list_node

        