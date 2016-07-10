#LL
########################################################################
class Node:
    """""" 
    #----------------------------------------------------------------------
    def __init__(self, value, next_element):
        """Constructor"""
        self.value = value
        self.next_element = next_element
        
########################################################################
class LinkedList:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.head = None
        self.size = 0
        
    #----------------------------------------------------------------------
    def append(self, data):
        """"""
        if not self.head:
            self.head = Node(data, None)
            print "head"
        else:
            n = self.head
            while n.next_element:
                n = n.next_element
            node = Node(data, None)
            n.next_element = node
    #----------------------------------------------------------------------
    def fetch(self, value):
        """"""
        n = self.head
        if n.value == value:
            return n 
        else:
            while n.next_element:
                if n.value == value:
                    return n
                n = n.next_element

LL = LinkedList()
LL.append(2)
LL.append(3)
LL.append(4)
print LL.fetch(3).next_element.value
    
    