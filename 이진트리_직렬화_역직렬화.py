# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Codec:
#
#     def serialize(self, root):
#         """Encodes a tree to a single string.
#
#         :type root: TreeNode
#         :rtype: str
#         """
#         queue = deque([root])
#         ans = ['#']
#         while queue:
#             node = queue.popleft()
#             if node is not None:
#                 ans.append(node.val)
#                 queue.append(node.left)
#                 queue.append(node.right)
#             else:
#                 ans.append('#')
#
#         ans = [str(x) for x in ans]
#         print(ans)
#         return ' '.join(ans)  # 문자열로 리턴
#
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
#
#         :type data: str
#         :rtype: TreeNode
#         """
#
#         if data == '# #':
#             return None

nodes = ['#','1','2','3','#','#','4','5','#','#','#','#']
root = TreeNode(int(nodes[1]))  # 0번째는 #이므로 1부터시작

queue = deque([root])
index = 2

while queue:
    node = queue.popleft()
    if nodes[index] != '#':
        node.left = TreeNode(int(nodes[index]))
        queue.append(node.left)

    index += 1
    if nodes[index] != '#':
        node.right = TreeNode(int(nodes[index]))
        queue.append(node.right)
    index += 1


test_queue=deque([root])

while test_queue:
    a=test_queue.popleft()
    print(a.val,a.left,a.right)
    if a.left:
        test_queue.append(a.left)
    if a.right:
        test_queue.append(a.right)

#         return root
#
# # Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# answer = deser.deserialize(ser.serialize(root))