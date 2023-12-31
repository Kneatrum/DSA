
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    # Empty circular linked list
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    '''
    # Circular linked list with one node.
    def __init__(self, value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1
    '''

    # Method to print our circular linked list
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += " -> "
        return result


    # Adding a new node to the end or at the beginning of the list
    def append(self, value):
        new_node = Node(value)
        # If the linked list is empty, create a new node and let the tail point to itself.
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.tail.next = new_node
        # If the linked list has one or more nodes, add the newo one and let the tail point to the head.
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1


    # Add a node to the beginning of the linked list (prepending).
    def prepend(self, value):
        new_node = Node(value)
        # If the linked list is empty, create a new node and let the tail point to itself.
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        # Else let the tail point to the new head, and the new node point to the existing head, then set the new node as the new head.
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length += 1

    
    # Insert a node at any given position in the linked list.
    def insert(self, value, index):
        # Check if the index is within the bounds of the linked list
        if index > self.length or index < 0:
            raise Exception("Index out of bounds")
        new_node = Node(value)
        if index == 0:
            # If the list is empty, insert a new node.
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = self.head
            # Prepend the new node to the head of the linked list.
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head
        # If the index is equal to the length of the list, we add the new node after the tail and set the next.pointer and the new tail and
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        # If the index is anywhere between the head and the tail
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1


    # Traversing the linked list.
    def traverse(self):
        temp_node = self.head
        while temp_node is not None:
            print(str(temp_node.value) + " ", end='')
            temp_node = temp_node.next
            if temp_node == self.head:
                print() # Optional. This prints a new lin character
                break

    
    # Searching for an element in the linked list
    def search(self, target):
        temp_node = self.head
        while temp_node is not None:
            if temp_node.value == target:
                return True
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return False
    

    # Returning a value from a specific index.
    def get(self, index):
        if index >= self.length or index < -1:
            raise Exception("Index out of range")
        elif index == -1:
            return self.tail
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current
        
    
    # Setting or updating a value in a specific index.
    def set(self, index, value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False
    

    # Removing the first element from the linked list.
    def pop_first(self):
        temp = self.head
        # If the list is empty, return nothing.
        if self.head == None:
            return None
        # if the list only has one element, set the self.head and self.next to None.
        elif self.length == 1:
            self.head = None
            self.tail = None
        # Set the second element as the new head and set the tail to the new head.
        else:
            self.head = temp.next
            temp.next = None
            self.tail.next = self.head
        self.length -= 1
        return temp
        
    
    # Removing the last element
    def pop_last(self):
        # If the list is empty, return nothing.
        if self.head == None:
            return None
        popped = self.tail
        # If the length of the list is 1, remove the only present element
        if self.length == 1:
            self.head = None
            self.tail = None
            return popped
        # Else loop to the second last element and set it as the new tail
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            self.tail.next = self.head
            popped.next = None
        self.length -= 1
        return popped
    

    # Remove an element from the linked list
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            self.pop_first()
        elif index == self.length - 1:
            self.pop_last()
        else:
            prev = self.get(index - 1)
            to_pop = prev.next
            prev.next = to_pop.next
            to_pop.next = None
            self.length -= 1
            return to_pop
        
        
    # Deleting all noded from the linked list
    def delete_all(self):
        if self.length == 0:
            return
        self.head = None
        self.tail.next = None
        self.tail = None
        self.length = 0







