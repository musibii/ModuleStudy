# -*- coding: utf-8 -*-
# __file__  : 102. 二叉树的层序遍历.py
# __time__  : 2020/8/4 6:30 PM

"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        node = [root]
        while root:
            cur = []
            next_layer = []
            for n in node:
                cur.append(n.val)
                if n.left:
                    next_layer.append(n.left)
                if n.right:
                    next_layer.append(n.right)
            res.append(cur)
            node = next_layer
