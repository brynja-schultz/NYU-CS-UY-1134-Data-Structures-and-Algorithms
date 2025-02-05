from LinkedBinaryTree import LinkedBinaryTree


def min_and_max(bin_tree):
    if bin_tree.is_empty():
        raise Exception("Linked Binary Tree is Empty!")

    def sub_tree_min_and_max(root):
        if root.left is None and root.right is None:  # if subtree is a leaf
            return root.data, root.data

        elif root.left is None:  # left is None and right has data
            right = sub_tree_min_and_max(root.right)  # returns (min,max) of right subtree

            min_value = min(root.data, right[0])  # finds min value of root & subtree
            max_value = max(root.data, right[1])  # finds max value of root & subtree

        elif root.right is None:  # right is None and left has data
            left = sub_tree_min_and_max(root.left)  # returns (min,max) of left subtree

            min_value = min(root.data, left[0])  # finds min value of root & subtree
            max_value = max(root.data, left[1])  # finds max value of root & subtree

        else:  # has two children (left & right)
            left = sub_tree_min_and_max(root.left)  # returns (min,max) of left subtree
            right = sub_tree_min_and_max(root.right)  # returns (min,max) of right subtree

            min_value = min(left[0], right[0])  # finds min of subtrees
            max_value = max(left[1], right[1])  # finds max of subtrees

            min_value = min(min_value, root.data)  # compares subtrees min with root
            max_value = max(max_value, root.data)  # compares subtrees max with root

        return min_value, max_value

    tree_root = bin_tree.root

    if tree_root.left is None and tree_root.right is None:  # if entire tree is only one node (the root)
        return tree_root.data, tree_root.data

    return sub_tree_min_and_max(tree_root)  # returns (min, max)

