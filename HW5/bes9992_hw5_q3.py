from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque


class MidStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.queue = ArrayDeque()
        self.n = 0

    def __len__(self):
        return len(self.stack) + len(self.queue)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.queue.enqueue_last(val)

        if len(self.queue) > len(self.stack):
            mid_val = self.queue.dequeue_first()
            self.stack.push(mid_val)

        self.n += 1

    def top(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        if len(self.queue) > 0:
            return self.queue.last()
        return self.stack.top()

    def pop(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        if len(self.queue) > 0:
            return self.queue.dequeue_last()
        return self.stack.pop()

    def mid_push(self, val):
        self.queue.enqueue_first(val)
        if len(self.queue) > len(self.stack):
            self.queue.dequeue_first()
            self.stack.push(val)







