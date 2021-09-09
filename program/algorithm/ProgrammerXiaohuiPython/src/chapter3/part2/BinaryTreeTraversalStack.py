class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_binary_tree(input_list=[]):
    if input_list is None or len(input_list) == 0:
        return None
    data = input_list.pop(0)
    if data is None:
        return None
    node = TreeNode(data)
    node.left = create_binary_tree(input_list)
    node.right = create_binary_tree(input_list)
    return node


def pre_order_traversal_with_stack(node):
    stack = []
    while node is not None or len(stack) > 0:
        while node is not None:
            print(node.data)
            stack.append(node)
            node = node.left
        if len(stack) > 0:
            node = stack.pop()
            node = node.right


my_input_list = list([3, 2, 9, None, None, 10, None, None, 8, None, 4])
root = create_binary_tree(my_input_list)
print("前序遍历：")
pre_order_traversal_with_stack(root)




