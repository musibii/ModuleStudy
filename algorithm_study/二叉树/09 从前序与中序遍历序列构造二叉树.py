# -*- coding: utf-8 -*-
# __file__  : 09 从前序与中序遍历序列构造二叉树.py
# __time__  : 2020/7/23 3:21 PM

"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])

        root_index = inorder.index(root.val)

        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]

        l_left = len(left_inorder)

        left_preorder = preorder[1:l_left + 1]
        right_preorder = preorder[l_left + 1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root
