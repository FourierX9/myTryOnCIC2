# -*- coding: utf-8 -*-
# @Time         : 3/2/2021 23:02
# @Author       : Chen Weiqing
# @FileName     : main.py
# @Software     : PyCharm
# @Blog         :
# @Description  :


class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if len(self.stack2)<1:
            if len(self.stack1) < 1:
                return -1
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

if __name__ == "__main__":
    cQueue = CQueue()
    a = cQueue.appendTail(3)
    a = cQueue.deleteHead()
    a = cQueue.deleteHead()
    a = cQueue.deleteHead()