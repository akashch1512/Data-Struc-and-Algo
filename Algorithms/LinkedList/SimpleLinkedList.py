class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.curr = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.curr = self.head
            return
        self.curr.next = Node(data)
        self.curr = self.curr.next


    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.data,end = "->")
            temp = temp.next
        print(None)


ob = LinkedList()

ob.append(1)
ob.append(2)
ob.append(3)
ob.append(4)

ob.print_list()