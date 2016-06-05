class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self):
        self.head = Node(None)
    def append(self,data):
        if not self.head.next:
            self.head.next = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)
    def pprint(self):
        cur = self.head
        while cur:
            print cur
            cur = cur.next

ll = LinkedList()
ll.append(5)
ll.append(20)
ll.pprint()
