"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


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
        current = self.head
        count = 1
        
        while current:
            if count == position:
                return current
            current = current.next
            count += 1
        return None
    
    def insert(self, new_element, position):
        
        current = self.head
        count = 1
        
        if position == 1:
            tmp = self.head
            self.head = new_element
            self.head.next = tmp
        
        while current:
            if count == position - 1:
                # make the prev node point to new node
                # make new node point to next node
                tmp = current.next
                current.next = new_element
                current.next.next = tmp
                    
            current = current.next
            count += 1
        
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
    
    
    def delete(self, value):
        
        current = self.head
        count = 1
        
        while current:
            
            if current.value == value and count == 1:
                self.head = current.next
            
            if current.next == None:
                return
            
            if current.next.value == value:
                current.next = current.next.next
            
            current = current.next
            count +=1
    
    def print_list(self):
        current = self.head
        
        arr = []
        while current:
            arr.append(str(current.value))
            current = current.next
            
        return " -> ".join(arr)
        
        

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element("this is a string")
e6 = Element("hello")

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
ll.insert(e5, 2)
ll.insert(e6, 1)
# Should print 4 now
print(ll.get_position(3).value)

print(ll.print_list())


# Test delete
ll.delete(4)
print(ll.print_list())

# # Should print 2 now
# print(ll.get_position(1).value)
# # Should print 4 now
# print(ll.get_position(2).value)
# # Should print 3 now
# print(ll.get_position(3).value)