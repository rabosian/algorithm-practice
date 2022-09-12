class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = node()
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
    def length(self):
        cur = self.head
        len = 0
        while cur.next:
            cur = cur.next
            len += 1
        return len
    def display(self):
        elems = []
        cur = self.head
        while cur.next:
            cur = cur.next
            elems.append(cur.data)
        print(elems)
        
    def get(self, index):
        if index >= self.length():
            print("index out of range")
            return None
        cur_index = 0
        cur = self.head
        while cur.next:
            cur = cur.next
            if cur_index == index:
                return cur.data
            cur.index += 1
    def remove(self, index):
        if index >= self.length():
            print("index out of range")
            return None
        cur_index = 0
        cur = self.head
        while cur.next:
            lastNode = cur
            cur = cur.next
            if cur_index == index:
                lastNode.next = cur.next
            cur_index += 1

myLink = linkedList()

myLink.append(1)
