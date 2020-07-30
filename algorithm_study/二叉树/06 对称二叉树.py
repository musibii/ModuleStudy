# -*- coding: utf-8 -*-
# __file__  : 06 对称二叉树.py
# __time__  : 2020/7/23 1:44 PM

"""
给定一个二叉树，检查它是否是镜像对称的。



例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3


但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3


进阶：

你可以运用递归和迭代两种方法解决这个问题吗？
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def Traversal(left, right):
            if left is None and right is None:#如果是叶节点，直接返回True
                return True
            #如果左右节点相同，继续判断左-左和右-右，以及左-右和右-左
            elif left and right and left.val == right.val:
                return Traversal(left.left, right.right) and Traversal(left.right, right.left)
            else:
                return False
        return Traversal(root.left, root.right)


