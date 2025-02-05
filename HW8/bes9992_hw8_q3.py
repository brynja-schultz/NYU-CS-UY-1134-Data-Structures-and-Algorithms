from BinarySearchTreeMap import BinarySearchTreeMap


def restore_bst(prefix_lst):
    bst = BinarySearchTreeMap()

    if len(prefix_lst) == 0:
        return bst

    elif len(prefix_lst) == 1:
        bst.root = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(prefix_lst[0]))
        return bst

    else:
        bst.root = restore_bst_helper(prefix_lst, 1000)[0]
        return bst


def restore_bst_helper(prefix_lst, max_val):
    if len(prefix_lst) == 0:
        return None, []

    elif prefix_lst[0] < max_val:  # left subtree
        root = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(prefix_lst[0]))  # node

        left_subtree, remain = restore_bst_helper(prefix_lst[1:], prefix_lst[0])  # (node or None, list)
        right_subtree, remain = restore_bst_helper(remain, max_val)  # (node or None, list)

        root.left = left_subtree
        root.right = right_subtree

        if left_subtree is not None:
            left_subtree.parent = root

        if right_subtree is not None:
            right_subtree.parent = None

        return root, remain

    else:
        return None, prefix_lst



