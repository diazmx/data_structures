class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = self.last = None
        self.N = 0

    def is_empty(self):
        return self.first == None

    def enqueue(self, data):
        nnode = Node(data)
        if self.is_empty():
            self.first = self.last = nnode
        else:
            self.last.next = nnode
            self.last = nnode
        self.N += 1

    def dequeue(self):
        i = self.first.data
        self.first = self.first.next
        return i

    def print_queue(self):
        i = self.first
        while i:
            print(i.data, end=" -> ")
            i = i.next
        print("None ---- size = {0}".format(self.N))

if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    q.enqueue(6)
    q.enqueue(8)
    q.print_queue()
    q.dequeue()
    q.print_queue()