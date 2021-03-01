# -*- coding: utf-8 -*-
# @Time         : 3/1/2021 22:13
# @Author       : Chen Weiqing
# @FileName     : main.py
# @Software     : PyCharm
# @Blog         :
# @Description  :

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 类型注解 : 后面的表示变量的类型     -> 后面的表示函数的返回类型
    def reversePrint(self, head: ListNode) -> List[int]:
        resList = []
        while head:
            resList.append(head.val)
            head = head.next
        return resList[::-1]

if __name__ == "__main__":
    solution = Solution()
    testListNode = ListNode(1)
    testListNode.next = ListNode(3)
    testListNode.next.next = ListNode(2)
    # 注意函数的输入参数是ListNode类型，不是List类型
    a = solution.reversePrint(testListNode)
    print("")
