from LinkedBinaryTree import LinkedBinaryTree


def create_expression_tree(prefix_exp_str):
    operators = "+-*/"
    prefix_list = prefix_exp_str.split(' ')
    curr_node = None

    for elem in prefix_list:
        if curr_node is None:
            root_node = LinkedBinaryTree.Node(elem)  # creates new node with elem

            tree = LinkedBinaryTree(root_node)
            curr_node = root_node

        elif curr_node.left is None:  # if no left child exists
            if elem in operators:  # if elem is operator --> fill up with children
                new_node = LinkedBinaryTree.Node(elem)

                new_node.parent = curr_node
                curr_node.left = new_node
                curr_node = new_node

            else:  # if elem is a number
                new_node = LinkedBinaryTree.Node(int(elem))  # creates new node with elem

                new_node.parent = curr_node
                curr_node.left = new_node

        elif curr_node.right is None:  # if no right child exists
            if elem in operators:  # if elem is operator --> fill up with children
                new_node = LinkedBinaryTree.Node(elem)

                new_node.parent = curr_node
                curr_node.right = new_node
                curr_node = new_node

            else:  # if elem is a number
                new_node = LinkedBinaryTree.Node(int(elem))  # creates new node with elem

                new_node.parent = curr_node
                curr_node.right = new_node

        else:  # if two children already exist
            while curr_node.right is not None:
                curr_node = curr_node.parent   # traverse tree until you find a node without a rigt child
            if elem in operators:  # if elem is operator --> fill up with children
                new_node = LinkedBinaryTree.Node(elem)

                new_node.parent = curr_node
                curr_node.right = new_node
                curr_node = new_node

            else:  # if elem is a number
                new_node = LinkedBinaryTree.Node(int(elem))  # creates new node with elem

                new_node.parent = curr_node
                curr_node.right = new_node

    return tree


def prefix_to_postfix(prefix_exp_str):
    tree = create_expression_tree(prefix_exp_str)
    post_order_lst = [str(i.data) for i in tree.postorder()]
    return " ".join(post_order_lst)

