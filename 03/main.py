class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while i != nums[i]:
                temp = nums[i]
                # 似乎不能用：nums[i], nums[nums[i]] = nums[nums[i]], nums[i] 因为交换过程中nums[i]变了
                nums[i] = nums[temp]
                nums[temp] = temp
                if nums[temp] == temp:
                    return temp


if __name__ == '__main__':
    solution = Solution()
    result = solution.findRepeatNumber([2, 3, 1, 0, 2, 5, 3])
    print(result)
