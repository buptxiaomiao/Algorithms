#########################################################################
# coding: utf-8
#!/usr/bin/python
# File Name: _quick_sort.py
# Author: buptxiaomiao
# mail: buptwjh@outlook.com
# Created Time: 六  8/18 03:36:15 2018
#########################################################################
import random
# 快速排序

def quick_sort1(arr, left, right):
    # !!!! 不要忘记边界条件
    if left >= right:
        return
    low = left
    high = right
    key = arr[left]
    while left < right:
        # 左右指针未碰撞时，go on
        while left < right and arr[right] > key:
            # 右指针 > 标兵
            right -= 1
        arr[left] = arr[right]

        while left < right and arr[left] <= key:
            # 左指针 <= 标兵
            left += 1
        arr[right] = arr[left]

    # 最后将中间位置置于标兵
    arr[right] = key
    quick_sort1(arr, low, left-1)
    quick_sort1(arr, right+1, high)

if __name__ == '__main__':
    l = [random.randint(-10, 10) for x in xrange(20)]
    print l
    quick_sort1(l, 0, len(l)-1)
    print l

