class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.right = None
        self.left = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        if not self.root:
            self.root = new_node
            return
        cur = self.root
        while True:
            if key < cur.key:
                if not cur.left:
                    cur.left = new_node
                    return
                cur = cur.left
            elif key > cur.key:
                if not cur.right:
                    cur.right = new_node
                    return
                cur = cur.right
            else:
                cur.val = val
                return 

    def get(self, key: int) -> int:
        cur = self.root
        while cur != None:
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return cur.val
        return -1

    def getMin(self) -> int:
        cur = self.root
        while cur and cur.left:
            cur = cur.left
        return cur.val if cur else -1

    def getMax(self) -> int:
        cur = self.root
        while cur and cur.right:
            cur = cur.right
        return cur.val if cur else -1

    def _find_min(self, node: TreeNode)-> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, cur: TreeNode, key: int) -> TreeNode:
        if cur == None:
            return None
        if key > cur.key:
            cur.right = self.removeHelper(cur.right, key)
        elif key < cur.key:
            cur.left = self.removeHelper(cur.left, key)
        else:
            if cur.left == None:
                return cur.right
            elif cur.right == None:
                return cur.left
            else:
                min_node = self._find_min(cur.right)
                cur.key = min_node.key
                cur.val = min_node.val
                cur.right = self.removeHelper(cur.right, min_node.key)

        return cur


    def getInorderKeys(self) -> List[int]:
        result  = []
        self.inorderTraversal(self.root, result)
        return result
    
    def inorderTraversal(self, root, result):
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)
        return

             


