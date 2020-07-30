class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.N = 0

    def is_empty(self):
        return self.top == None

    def size(self):
        return self.N

    def push(self, data):
        n_node = Node(data)
        if self.is_empty():
            self.top = n_node
        else:
            n_node.next = self.top
            self.top = n_node
        self.N += 1
    
    def pop(self):
        if self.is_empty():
            return -1
        else:
            item = self.top.data
            self.top = self.top.next
            return item

    def print_stack(self):
        i = self.top
        while i:
            print(i.data, end=" -> ")
            i = i.next
        print("None ***** size = {0}".format(self.N))

def parentheses(st):
    stack = Stack()
    for i in len(st):
        if st[i] in ['[','(','{']:
            if st[i] == '[':
                stack.push(1)
            if st[i] == '(':
                stack.push(2)
            if st[i] == '{':
                stack.push(3)
        else:
            if st[i] == stack.top

st = Stack()
st.push(2)
st.push(3)
st.print_stack()
st.pop()
st.print_stack()