# -*- coding: utf-8 -*-
# @Time         : 3/1/2021 21:12
# @Author       : Chen Weiqing
# @FileName     : main.py
# @Software     : PyCharm
# @Blog         :
# @Description  :


class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')



if __name__ == '__main__':
    s = "We are happy."
    solution = Solution()
    print(solution.replaceSpace(s))