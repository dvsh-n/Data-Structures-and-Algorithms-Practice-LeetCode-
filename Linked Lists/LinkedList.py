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
            print(str(temp.value), end = ' -> ')
            temp = temp.next
        print('\n')

    def add_node(self, value):
        if self.length == 0:
            self.head = node(value)
            self.tail = self.head
        else:
            new_node = self.head
            while new_node.next != None:
                new_node = new_node.next
            new_node.next = node(value)
            self.tail = new_node.next
        self.length = self.length + 1

new_list = linked_list()
new_list.add_node(9)
new_list.add_node(10)
new_list.add_node(20)
new_list.print_all()