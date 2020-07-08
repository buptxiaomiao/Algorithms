# coding: utf-8

# https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies/


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        l = [False] * len(candies)

        org_max = 0
        for i in range(len(candies)):
            if candies[i] > org_max:
                org_max = candies[i]

        for i in range(len(candies)):
            if candies[i] + extraCandies >= org_max:
                l[i] = True

        return l



