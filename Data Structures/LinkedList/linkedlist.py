class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = self.last = None
        self.lenght = 0

    def print(self):
        i = self.head
        while i:
            print(i.data, end=" -> ")
            i = i.next
        print("None")

    # Verificar si está vacía la lista
    def is_empty(self):
        return self.head == None

    # aggregar elemento al final de la lista
    def push(self, data):
        # crear el objeto
        n_node = Node(data)

        # Si está vacía la lista
        if self.is_empty():
            self.head = self.last = n_node
        else:
            n_node.next = self.head
            self.head = n_node

        self.lenght += 1

    def append(self, data):
        n_node = Node(data)
        if self.is_empty():
            self.head = self.last = n_node
        else:
            self.last.next = n_node
            self.last = n_node

    def insert_after_index(self, prev_node, data):
        i = self.head
        n_node = Node(data)

        if self.is_empty():
            self.head = self.last = n_node
        else:
            while prev_node > 0:
                i = i.next
                prev_node -= 1
            n_node.next = i.next
            i.next = n_node

    def delete_after_index(self, k):
        i = self.head
        while k > 1 and i:
            i = i.next
            k -= 1
        i.next = i.next.next

# Main fuction

ll = LinkedList()

ll.push(2)
ll.push(3)
ll.append(5)
ll.push(4)
ll.insert_after_index(2, 6)
ll.print()
ll.delete_after_index(5)
ll.print()

    