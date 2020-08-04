# -*- coding: utf-8 -*-
# __file__  : 25. K 个一组翻转链表.py
# __time__  : 2020/8/4 3:04 PM


"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

 

示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

 

说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 设置一个头头结点
        hair = ListNode(0)
        # 将头头结点指向 head
        hair.next = head
        # 头头结点相当于 pre 结点
        pre = hair

        while head:
            # 双指针，将 pre 结点即是头头结点也是尾结点
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                # 循环找出要反转的尾结点
                tail = tail.next
                # 如果 tail 为 None 的话，则说明这之后的不用反转
                if not tail:
                    return hair.next
            # 保存下一次反转的头结点
            temp = tail.next
            # 将头尾结点反转
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = temp
            pre = tail
            head = tail.next

        return hair.next
