class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(listr)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head

        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return
            
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after :
                node = Node(data_to_insert, itr.next)
                itr.next = node

            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        #index = 0
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                #self.remove_at(index)
                break
            itr = itr.next
            #index += 1

    def moveToFront(self):
        tmp = self.head
        sec_last = None  

        # To maintain the track of the second last node
        # To check whether we have not received
        # the empty list or list with a single node
        if not tmp or not tmp.next:
            return
 
        # Iterate till the end to get
        # the last and second last node
        while tmp and tmp.next:
            sec_last = tmp
            tmp = tmp.next
 
        # point the next of the second
        # last node to None
        sec_last.next = None
 
        # Make the last node as the first Node
        tmp.next = self.head
        self.head = tmp




if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    print('Linked list after_value')
    ll.insert_after_value("mango","apple") # insert apple after mango
    print('Linked list "Move to Front"')
    ll.moveToFront()
    ll.print()
    print('Linked list "Remove By Value"')
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    print('Linked list "Insert at Begining"')
    ll.insert_at_begining("figs")
    ll.print()
    print('Linked list "Length"')
    ll.get_length()
    print('Linked list "Remove By Values"')
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    print('Linked list "Remove By Values"')
    ll.print()