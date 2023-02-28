"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

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

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next = self.head
        self.head = e_insert

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        temp = self.head
        if temp == None:
            return None
        s= temp
        self.head = temp.next
        return s

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        temp = self.ll.head
        while temp.next :
            temp = temp.next
        temp.next = new_element

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        if self.ll.head.next == None :
            temp = self.ll.head
            e= temp
            temp = None
            return e
        elif self.ll.head.next:
            temp = self.ll.head
            while temp.next.next:
                   temp = temp.next
            e= temp.next
            temp.next = None
            return e
        return None
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print stack.pop().value
print stack.pop().value
print stack.pop().value
print stack.pop()
stack.push(e4)
print stack.pop().value