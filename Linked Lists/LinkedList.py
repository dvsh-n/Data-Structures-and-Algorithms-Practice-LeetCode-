class node():
    def __init__(self, value):
        self.value = value
        self.next = None

class linked_list():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_all(self):
        temp = self.head
        print(str(temp.value), end = ' -> ')
        while temp.next != None:
            temp = temp.next
            print(str(temp.value), end = ' -> ')
        print('End\n')

    def append(self, value):
        new_node = node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            last = self.head    
            while last.next != None:
                last = last.next
            last.next = new_node
            self.tail = new_node
        self.length = self.length + 1

new_list = linked_list()
new_list.append(9)
new_list.append(10)
new_list.append(20)
new_list.append(30)
new_list.print_all()