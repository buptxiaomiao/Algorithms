# coding: utf-8

# https://leetcode-cn.com/problems/running-sum-of-1d-array


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        length = len(nums)

        # 预先分配内存
        l = [0] * length
        for i in range(length):
            if i == 0:
                l[0] = nums[0]
            else:
                l[i] = l[i - 1] + nums[i]
        return l

