# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        # find middle of list
        if not head: return []
        one_step, two_step = head, head
        while two_step.next and two_step.next.next:
            one_step = one_step.next
            two_step = two_step.next.next
        
        # reverse second half of list
        previous, current = None, one_step.next
        while current:
            remainder = current.next
            current.next = previous
            previous = current
            current = remainder  
        one_step.next = None
        
        # merge two lists
        head1, head2 = head, previous
        while head2:
            next_node = head1.next
            head1.next = head2
            head1 = head2
            head2 = next_node

