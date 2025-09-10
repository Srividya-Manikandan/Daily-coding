"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque


#BFS is used for serializing and deserializing
#Serialize : tree->string
#Deserialize : string->tree
class Codec:

    def serialize(self, root):
        if not root:
            return ""
        result=[]
        q=deque([root])
        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("null")
        #popping extra nulls at the end
        while result and result[-1]=="null":
            result.pop()
        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None
        tree = data.split(",")
        root1=TreeNode(int(tree[0]))
        i=1
        tree_q=deque([root1])
        while tree_q and i<len(tree):
            root=tree_q.popleft()
            if tree[i] != "null":
                root.left=TreeNode(int(tree[i]))
                tree_q.append(root.left)
            i+=1
            if i>=len(tree):
                break
            if tree[i] != "null":
                root.right=TreeNode(int(tree[i]))
                tree_q.append(root.right)
            i+=1
        return root1
        
if __name__ == "__main__":
    # Build a sample tree:
    #       1
    #      / \
    #     2   3
    #        / \
    #       4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = Codec()
    data = codec.serialize(root)
    print("Serialized:", data)   # Expected like: "1,2,3,null,null,4,5"

    new_root = codec.deserialize(data)
    print("Deserialized root value:", new_root.val)          # 1
    print("Deserialized left child:", new_root.left.val)     # 2
    print("Deserialized right->left:", new_root.right.left.val)  # 4