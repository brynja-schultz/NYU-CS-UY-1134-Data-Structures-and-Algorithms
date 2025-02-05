from ArrayStack import ArrayStack


class Queue:  # FIFO
    def __init__(self):
        self.primary_stack = ArrayStack()
        self.flip_stack = ArrayStack()
        self.n = 0
        self.front_value = None

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, elem):
        self.primary_stack.push(elem)
        if self.front_value is None:
            self.front_value = elem
        self.n += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is Empty!")

        for i in range(self.n):
            self.flip_stack.push(self.primary_stack.pop())

        self.n -= 1
        dequeued_val = self.flip_stack.pop()

        for i in range(self.n):
            self.primary_stack.push(self.flip_stack.pop())

        return dequeued_val

    def first(self):
        if self.is_empty():
            raise Exception("Queue is Empty!")

        for i in range(self.n):
            self.flip_stack.push(self.primary_stack.pop())

        first_ind = self.flip_stack.top()

        for i in range(self.n):
            self.primary_stack.push(self.flip_stack.pop())

        return first_ind
