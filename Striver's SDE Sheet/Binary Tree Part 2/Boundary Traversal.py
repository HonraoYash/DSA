# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def addLeft(self, node):
        if not node or (not node.left and not node.right):
            return
        self.res.append(node.data)
        if node.left:
            self.addLeft(node.left)
        else:
            self.addLeft(node.right)

    def addLeaves(self, node):
        if not node:
            return
        if not node.left and not node.right:
            self.res.append(node.data)
        self.addLeaves(node.left)
        self.addLeaves(node.right)

    def addRight(self, node):
        if not node:
            return
        stack = []
        while node:
            if not node.left and not node.right:
                break
            stack.append(node)
            if node.right:
                node = node.right
            elif node.left:
                node = node.left

        while stack:
            self.res.append(stack.pop().data)


    def boundary(self, root):
        #your code goes here
        self.res = []
        if not root:
            return self.res 

        self.res.append(root.data)

        self.addLeft(root.left)
        self.addLeaves(root.left)
        self.addLeaves(root.right)
        self.addRight(root.right)

        return self.res

    # Time Complexity - O(Height of the Tree)(left boundary) + O(Height of the Tree)(right boundary) + O(N)(leaves) = O(N)
    # Space Complexity - O(N)(for the stack)






