# coding: utf-8

# https://leetcode-cn.com/problems/diving-board-lcci/


class Solution(object):

    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []

        if k == 1:
            return [shorter, longer]

        if shorter == longer:
            return [shorter * k]

        delta = longer - shorter

        # short k块板子排列，longer 从0-k块板子替换
        return [
            shorter * k + delta * i
            for i in range(k + 1)
        ]

