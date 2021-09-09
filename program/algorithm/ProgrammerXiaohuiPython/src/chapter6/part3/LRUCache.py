class LRUCache:
    def __init__(self, limit):
        self.limit = limit
        self.hash = {}
        self.head = None
        self.end = None

    def get(self, key):
        node = self.hash.get(key)
        if node is None:
            return None
        self.refresh_node(node)
        return node.value

    def put(self, key, value):
        node = self.hash.get(key)
        if node is None:
            # 如果key不存在，插入key-value
            if len(self.hash) >= self.limit:
                old_key = self.remove_node(self.head)
                self.hash.pop(old_key)
            node = Node(key, value)
            self.add_node(node)
            self.hash[key] = node
        else:
            # 如果key存在，刷新key-value
            node.value = value
            self.refresh_node(node)

    def remove(self, key):
        node = self.hash.get(key)
        if node is None:
            return
        self.remove_node(node)
        self.hash.remove(key)

    def refresh_node(self, node):
        # 如果访问的是尾节点，无需移动节点
        if node == self.end:
            return
        # 移除节点
        self.remove_node(node)
        # 重新插入节点
        self.add_node(node)

    def remove_node(self, node):
        if node == self.head and node == self.end:
            # 移除唯一的节点
            self.head = None
            self.end = None
        elif node == self.end:
            # 移除节点
            self.end = self.end.pre
            self.end.next = None
        elif node == self.head:
            # 移除头节点
            self.head = self.head.next
            self.head.pre = None
        else:
            # 移除中间节点
            node.pre.next = node.pre
            node.next.pre = node.pre
        return node.key

    def add_node(self, node):
        if self.end is not None:
            self.end.next = node
            node.pre = self.end
            node.next = None
        self.end = node
        if self.head is None:
            self.head = node


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


lruCache = LRUCache(5)
lruCache.put("001", "用户1信息")
lruCache.put("002", "用户2信息")
lruCache.put("003", "用户3信息")
lruCache.put("004", "用户4信息")
lruCache.put("005", "用户5信息")
print(lruCache.get("002"))
lruCache.put("004", "用户4信息更新")
lruCache.put("006", "用户6信息")
print(lruCache.get("001"))
print(lruCache.get("006"))






