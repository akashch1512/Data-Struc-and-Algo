# One go with 100 speed and one go with 50 ! 

# to find the mid of an linked list
# one will run with 1 node at a time 
# 2 nd node 1/2 node a time ! 

def middleNode(head): # head for a linked list
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow