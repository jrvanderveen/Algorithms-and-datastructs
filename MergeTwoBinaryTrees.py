# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def mergeTrees(self, t1, t2):
        if not t1 or not t2:
            return t1 if not t2 else t2

        t1Head = t1
        self.dfsTreesAndBuild(t1, t2)
        return t1Head

    def dfsTreesAndBuild(self, t1, t2):
        t1.val += t2.val if t2 else 0
        if t1.left or (t2 and t2.left):
            if not t1.left:
                t1.left = TreeNode()
            self.dfsTreesAndBuild(t1.left, t2.left if t2 else None)
        if t1.right or (t2 and t2.right):
            if not t1.right:
                t1.right = TreeNode()
            self.dfsTreesAndBuild(t1.right, t2.right if t2 else None)
