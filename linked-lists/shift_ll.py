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
    
    
    def shift(self, k):

        if k == 0:
            print("eq")
            return self.head
        
        size = 0
        current = self.head
            
        while current:
            size+=1
            current = current.next
        
        for i in range(k):
            count = 1
            current = self.head
            while current:
                
                if count == size-1:
                    tmp = current.next
                    current.next = None
                    hd = self.head
                    self.head = tmp
                    self.head.next = hd
                count += 1
                current = current.next
            
                
            
    
        
        

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)
e6 = Element(6)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
ll.append(e6)

print(ll.print_list())
ll.shift(3)
print(ll.print_list())