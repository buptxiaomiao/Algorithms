#########################################################################
#-*- coding:utf-8 -*-
# File Name: Max_sub_array_2.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月25日 星期五 20时31分18秒
#########################################################################
#!/usr/bin/env python2.7
a = [-5,9,5,-1,6,2,-4,3,1,2]

from find_max_crossing_sub_array import find_max_crossing_sub_array
def max_sub_array(low,high,*arr):
	if low == high:
		return (low,high,arr[low])
	else:
		mid = (low+high)//2
		left_result = max_sub_array(low,mid,*arr)
		right_result = max_sub_array(mid+1,high,*arr)
		cross_result = find_max_crossing_sub_array(low,mid,high,*arr)
	if left_result(2)>right_result(2) and left_result(2)>cross_result(2):
		return left_result
	elif right_result(2)>left_result(2) and right_result(2)>cross_result(2):
		return right_result
	else:
		 return cross_result
if __name__ == '__main__':
	max_sub_array(0,len(a)-1,*a)
