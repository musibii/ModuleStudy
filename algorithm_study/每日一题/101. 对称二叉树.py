# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : 101. 对称二叉树.py
# __time__  : 2020/6/1 8:11 下午

import typing

"""
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
 

进阶：

你可以运用递归和迭代两种方法解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(root1, root2):
            if root1 == root2: return True
            if not root1 or not root2: return False
            if root1.val != root2.val: return False
            return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
        if not root: return True
        return dfs(root.left, root.right)
