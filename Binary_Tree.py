from collections import deque

class Node(object):

    def __init__(self, data):  # val : 부모노드, left,right : 자식노드들
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(Node):

    def __init__(self):
        self.root = None

    # 삽입
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None


    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)

            else:
                node.right = self._insert_value(node.right, data)

        return node

    # 탐색
    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None

        elif key < root.data:
            return self._find_value(root.left, key)

        else:
            return self._find_value(root.right, key)

    # 삭제
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                # replace the node to the leftmost of node.right
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted


array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
bst = BinarySearchTree()
for x in array:
    bst.insert(x)



queue=deque([bst])
depth=0

print(queue)
while queue:
    print(queue.popleft())
# while queue:
#     depth+=1
#     len_queue=len(queue)
#     for _ in range(len_queue):
#         cur_root=queue.popleft()
#         print(cur_root)
#
#         if cur_root.left:
#             queue.append(cur_root.left)
#         if cur_root.right:
#             queue.append(cur_root.right)



# # Delete
# print(bst.delete(55))  # True
# print(bst.delete(14))  # True
# print(bst.delete(11))  # False