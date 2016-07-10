class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position == 1:
            return self.head
        else:
            counter = 1
            n = self.head
            while n.next:
                n = n.next
                counter += 1
                if counter == position:
                    return n
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if position == 1:
            x = self.head
            self.head = Element(new_element)
            self.head.next = x
        elif position == 2:
            temp = self.head.next
            self.head.next = Element(new_element)
            self.head.next.next = temp
        else:
            counter = 1
            n = self.head
            while n.next:
                if position-1 == counter:
                    temp = n.next
                    n.next = new_element
                    n.next.next = temp
                    return
                n = n.next
                counter += 1
    
    def delete(self, value):
        """Delete the first node with a given value."""
        n = self.head
        if n.value == value:
            if n.next:
                self.head = n.next
            else:
                self.head = None
        else:
            while n.next:
                if n.next.value == value:
                    n.next = n.next.next
                    return "Done"
                n = n.next
        return "Done"