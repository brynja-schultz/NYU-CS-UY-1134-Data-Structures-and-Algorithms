from ArrayStack import ArrayStack


class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.max_num = None

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        if self.max_num is None:
            self.max_num = val

        self.data.push((val, self.max_num))  # adds tuple to data of value and the max of the numbers before the val

        if val > self.max_num:
            self.max_num = val

    def top(self):
        if self.is_empty():
            raise Exception("maxS is empty")
        return self.data.top()[0]

    def pop(self):
        if self.is_empty():
            raise Exception("maxS is empty")
        (data, prev_max) = self.data.pop()
        self.max_num = prev_max
        return data

    def max(self):
        if self.is_empty():
            raise Exception("maxS is empty")
        else:
            return self.max_num




