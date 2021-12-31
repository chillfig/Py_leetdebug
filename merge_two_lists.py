# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    input = None
    answer = None

    def __init__(self, l1, l2) -> answer:
        self.input = input
        self.answer = self.mergeTwoLists(l1, l2)
        
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1:
            return list2
        if not list2:
            return list1
            
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
example1 = Solution(l1, l2)