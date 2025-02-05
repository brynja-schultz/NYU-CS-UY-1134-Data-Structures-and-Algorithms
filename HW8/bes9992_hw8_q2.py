from BinarySearchTreeMap import BinarySearchTreeMap


def create_chain_bst(n):
    bst = BinarySearchTreeMap()  # creates tree object

    for i in range(1, n+1):
        bst[i] = None

    return bst


def create_complete_bst(n):
    # n = 2^k - 1, so n is always odd

    bst = BinarySearchTreeMap()  # creates tree object
    add_items(bst, 1, n)
    return bst  # returns complete tree


def add_items(bst, low, high):
    if low == high:  # final node --> if low > high nothing happens
        bst.insert(low)

    elif low < high:
        mid = (low + high)//2
        bst.insert(mid)  # root of subtree
        add_items(bst, low, mid-1)  # left subtree
        add_items(bst, mid+1, high)  # right subtree

