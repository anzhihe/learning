from queue import Queue


def level_order_traversal(node):
    queue = Queue()
    queue.put(node)
    while not queue.empty():
        node = queue.get()
        print(node.data)
        if node.left is not None:
            queue.put(node.left)
        if node.right is not None:
            queue.put(node.right)


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


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


my_input_list = list([3, 2, 9, None, None, 10, None, None, 8, None, 4])
root = create_binary_tree(my_input_list)
print("层序遍历：")
level_order_traversal(root)




