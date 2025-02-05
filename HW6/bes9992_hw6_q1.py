from DoublyLinkedList import DoublyLinkedList


class LinkedQueue:
    def __init__(self):
        self.list = DoublyLinkedList()

    def __len__(self):
        return len(self.list)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, data):
        self.list.add_last(data)

    def first(self):
        if self.is_empty():
            raise Exception("LinkedQueue is empty!")
        else:
            return self.list.header.next.data

    def dequeue(self):
        if self.is_empty():
            raise Exception("LinkedQueue is empty!")
        else:
            return self.list.delete_node(self.list.header.next)


