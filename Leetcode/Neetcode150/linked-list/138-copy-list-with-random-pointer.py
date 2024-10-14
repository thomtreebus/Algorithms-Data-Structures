"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {None: None} # old -> new
        current = head
        # create new nodes for each node in list
        while current:
            nodes[current] = Node(current.val)
            current = current.next

        current = head
        # set next and random pointers for new nodes
        while current:
            new_node = nodes[current]
            new_node.next = nodes[current.next]
            new_node.random = nodes[current.random]
            current = current.next

        return nodes[head]