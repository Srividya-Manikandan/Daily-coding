"""
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 """
class Node:
   def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
   def __repr__(self):
      return f"Node({self.value!r})"
   # def unival(self):
   #    if self.left is None and self.right is None:
   #       return (True,1)
   #    left_unival,left_count=self.left.unival()
   #    right_unival,right_count=self.right.unival()
   #    total=left_count+right_count
   #    if left_unival and right_unival:
   #       if self.left.value!=self.right.value or self.value!=self.right.value or self.left.value!=self.value:
   #          return (False,total)
   #       else:
   #          return (True,total+1)
   #    return (False,total)
   def unival(self):
      if self.left is None and self.right is None:
         return (True,1)
      if self.left is not None:
         left_unival, left_count = self.left.unival()
      else:
         left_unival, left_count = True, 0   # Treat missing child as “valid”
      if self.right is not None:
         right_unival, right_count = self.right.unival()
      else:
         right_unival, right_count = True, 0   # Treat missing child as “valid”
      total=left_count+right_count
      if left_unival or right_unival:
         if self.left is not None and self.right is not None:
            if self.left.value!=self.right.value or self.value!=self.right.value or self.left.value!=self.value:
               return (False,total)
            else:
               return (True,total+1)
         elif self.left is None:
            if self.value!=self.right.value:
               return (False,total)
            else:
               return (True,total+1)
         elif self.right is None:
            if self.value!=self.left.value:
               return (False,total)
            else:
               return (True,total+1)
      return (False,total)
   
# Example usage:
# Constructing the tree:
#        0
#       / \
#      1   0
#         / \
#        1   0
#       / \   \
#      1   1   0
# Output: 6 unival subtrees
root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.right.left = Node(1)
root.right.right = Node(0)
root.right.left.left = Node(1)
root.right.left.right = Node(1)
root.right.right.right = Node(0) 
_, count=root.unival()  # Output: 6
print("Number of unival subtrees:", count)  # Output: 6
