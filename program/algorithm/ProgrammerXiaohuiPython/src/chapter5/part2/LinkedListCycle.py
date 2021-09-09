class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def is_cycle(head):
    p1 = head
    p2 = head
    while p2 is not None and p2.next is not None:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return True
    return False


node1 = Node(5)
node2 = Node(3)
node3 = Node(7)
node4 = Node(2)
node5 = Node(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2
print(is_cycle(node1))

