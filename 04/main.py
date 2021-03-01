# -*- coding: utf-8 -*-
# @Time         : 1/26/2021 22:39
# @Author       : Chen Weiqing
# @FileName     : main.py
# @Software     : PyCharm
# @Blog         :
# @Description  : 剑指offer 04题
from typing import List

# 从右上角入手
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        width = len(matrix[0])
        height = len(matrix)
        current_column = width - 1
        current_row = 0
        while current_column > -1 and current_row < height:
            temp = matrix[current_row][current_column]
            if matrix[current_row][current_column] > target:
                current_column -= 1
                continue
            if matrix[current_row][current_column] == target:
                return True
            current_row += 1
        return False


if __name__ == '__main__':
    solution = Solution()
    result = solution.findNumberIn2DArray([
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 15)
    result = solution.findNumberIn2DArray([], ())
    result = solution.findNumberIn2DArray([[]], ())
    result = solution.findNumberIn2DArray(
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 19)
    for i in range(1, 26, 1):
        test_result = solution.findNumberIn2DArray(
            [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], i)
        assert test_result == True
    print(result)


class Solution_false:
    # 走斜线方法，遇到实例中的数字15不好计算，卒
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix)
        height = len(matrix[0])
        i = 0
        j = 0
        while i < height and j < width:
            if matrix[i][j] <= target < matrix[i + 1][j + 1]:
                break
            i += 1
            j += 1
        length = i
        for k in range(0, length + 1, 1):
            if matrix[i - k][j] == target or matrix[i][j - k] == target:
                return True
        return False
