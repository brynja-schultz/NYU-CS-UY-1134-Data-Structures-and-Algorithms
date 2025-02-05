from BinarySearchTreeMap import BinarySearchTreeMap


def find_min_abs_difference(bst):
    # requires linear runtime
    if bst.is_empty():
        return None

    else:
        return find_min_abs_difference_helper(bst.root)[0]


def find_min_abs_difference_helper(root):  # returns (int/None, min_node, max_node)
    if root.left is None and root.right is None:  # if a leaf
        return None, root, root

    elif root.left is None:  # if 1 right child
        right_diff, min_node, max_node = find_min_abs_difference_helper(root.right)

        if right_diff is None or abs(root.item.key - min_node.item.key) < right_diff:
            return abs(root.item.key - min_node.item.key), root, root.right
        else:
            return right_diff, root, root.right

    elif root.right is None:  # if 1 left child
        left_diff, min_node, max_node = find_min_abs_difference_helper(root.left)

        if left_diff is None or abs(root.item.key - max_node.item.key) < left_diff:
            return abs(root.item.key - max_node.item.key), root.left, root

        else:
            return left_diff, root.left, root

    else:  # if 2 children
        right_diff, r_min_node, r_max_node = find_min_abs_difference_helper(root.right)
        left_diff, l_min_node, l_max_node = find_min_abs_difference_helper(root.left)

        if left_diff is None and right_diff is not None:  # left node is a leaf
            if right_diff < abs(root.item.key - l_max_node.item.key) and left_diff < abs(root.item.key - r_min_node.item.key):
                return right_diff, l_min_node, r_max_node

            elif abs(root.item.key - l_max_node.item.key) < abs(root.item.key - r_min_node.item.key):
                return abs(root.item.key - l_max_node.item.key), l_min_node, r_max_node

            else:
                return abs(root.item.key - r_min_node.item.key), l_min_node, r_max_node

        elif left_diff is not None and right_diff is None:  # right node is a leaf
            if left_diff < abs(root.item.key - l_max_node.item.key) and left_diff < abs(root.item.key - r_min_node.item.key):
                return left_diff, l_min_node, r_max_node

            elif abs(root.item.key - l_max_node.item.key) < abs(root.item.key - r_min_node.item.key):
                return abs(root.item.key - l_max_node.item.key), l_min_node, r_max_node

            else:
                return abs(root.item.key - r_min_node.item.key), l_min_node, r_max_node

        elif left_diff is None and right_diff is None:  # both nodes are leaves
            if abs(root.item.key - l_max_node.item.key) < abs(root.item.key - r_min_node.item.key):
                return abs(root.item.key - l_max_node.item.key), l_min_node, r_max_node

            else:
                return abs(root.item.key - r_min_node.item.key), l_min_node, r_max_node

        else:  # both right_diff and left_diff exist
            if left_diff < right_diff and left_diff < abs(root.item.key - l_max_node.item.key) and left_diff < abs(root.item.key - r_min_node.item.key):
                return left_diff, l_min_node, r_max_node

            elif right_diff < left_diff and right_diff < abs(root.item.key - l_max_node.item.key) and right_diff < abs(root.item.key - r_min_node.item.key):
                return right_diff, l_min_node, r_max_node

            elif abs(root.item.key - l_max_node.item.key) < right_diff and abs(root.item.key - l_max_node.item.key) < left_diff and abs(root.item.key - l_max_node.item.key) < abs(root.item.key - r_min_node.item.key):
                return abs(root.item.key - l_max_node.item.key), l_min_node, r_max_node

            else:
                return abs(root.item.key - r_min_node.item.key), l_min_node, r_max_node
