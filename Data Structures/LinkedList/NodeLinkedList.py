class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next

def push(head, data):
    n_node = Node(data)
    n_node.next = head
    return n_node



head = Node(3)
head.next = Node(4)

printList(head)