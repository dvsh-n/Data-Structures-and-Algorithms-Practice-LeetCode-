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
        self.length += len(args)

    def traverse_to_index(self, index):
        temp = self.head
        i = 0
        if index >= 0:
            while i != index:
                temp = temp.next
                i += 1
        else:
            while i != (self.length + index):
                temp = temp.next
                i += 1
        return temp

    def insert(self, value, index):
        prev_Node = self.traverse_to_index(index - 1)
        next_Node = prev_Node.next
        new_Node = node(value)
        new_Node.next = next_Node
        prev_Node.next = new_Node
        self.length += 1        

    # def reverse(self):
    #     for i in range(int(self.length/2)):




new_list = linked_list()
new_list.append_many(9,10,20,30,22)
new_list.insert(35,2)
print(new_list.traverse_to_index(-3).value)
new_list.print_all()