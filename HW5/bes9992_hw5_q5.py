from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue


def permutations(lst):
    # returns list of all possible permutations of inputted list
    stack = ArrayStack()  # unused elements (LIFO)
    queue = ArrayQueue()  # current collection of permutations (FIFO)
    perm_list = []

    for item in lst:
        stack.push(item)  # creates stack filled with ints in original list

    first_elem = []
    first_elem.append(stack.pop())
    queue.enqueue(first_elem)

    while not stack.is_empty():
        curr_elem = stack.pop()  # 3 stack becomes [2, 1]
        for i in range(len(queue)):
            for j in range(len(queue.first())+1):
                top = queue.first().copy()
                top.insert(j, curr_elem)
                queue.enqueue(top)
            queue.dequeue()

    while not queue.is_empty():
        perm_list.append(queue.dequeue())

    return perm_list

