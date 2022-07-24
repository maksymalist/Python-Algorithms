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
    
    def reverse(self):
        prev, current = None, self.head
        while current:
            next = current.next
            current.next = prev # None 1 -> None 
            prev = current      # 1
            current = next      # 
        print(prev.value)
        self.head = prev
            

        
        


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)

print(ll.print_list())

ll.reverse()

print(ll.print_list())
    
