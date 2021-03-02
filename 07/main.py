# -*- coding: utf-8 -*-
# @Time         : 3/1/2021 22:55
# @Author       : Chen Weiqing
# @FileName     : main.py
# @Software     : PyCharm
# @Blog         :
# @Description  :

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0 and len(inorder)==0:
           return None
        rootIndex = inorder.index(preorder[0])
        currentNode = TreeNode(preorder[0])
        currentNode.left = self.buildTree(preorder[1:1+rootIndex:1], inorder[0:rootIndex:1])
        currentNode.right = self.buildTree(preorder[1+rootIndex::], inorder[1+rootIndex::])
        return currentNode

if __name__ == "__main__":
    root = Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])
