from LinkedBinaryTree import LinkedBinaryTree


def is_height_balanced(bin_tree):
    if bin_tree.is_empty():
        return True

    tree_root = bin_tree.root

    if tree_root.left is None and tree_root.right is None:  # if entire tree is only the root
        return True

    else:
        return is_subtree_height_balanced(tree_root)


def is_subtree_height_balanced(root):
    # returns False or (node, current height)
    if root.left is None and root.right is None:  # no children
        return root, 1

    elif root.left is None:  # only right child
        right = is_subtree_height_balanced(root.right)

        if right is False:
            return False

        elif right[1] > 1:
            return False

        return root, right[1] + 1  # increase height

    elif root.right is None:  # only left child
        left = is_subtree_height_balanced(root.left)

        if left is False:
            return False

        elif left[1] > 1:
            return False

        return root, left[1] + 1  # increase height

    else:  # two children
        left = is_subtree_height_balanced(root.left)
        right = is_subtree_height_balanced(root.right)

        if left is False or right is False:  # false if either subtree is unbalanced
            return False

        elif (left[1] - right[1]) > 1 or (left[1] - right[1]) < -1:  # false if difference in heights is more than 1
            return False

        else:
            return root, max(left[1], right[1]) + 1  # increase height

