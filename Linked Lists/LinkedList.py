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
        self.length += 1

    def append_many(self, *args):
        for i in args:
            self.append(i)

    def traverse(self, index):
        temp = self.head
        i = 0
        while i != index:
            temp = temp.next
            i += 1
        return temp.value
        


new_list = linked_list()
new_list.append_many(9,10,20,30,22)
print(new_list.traverse(0))
new_list.print_all()