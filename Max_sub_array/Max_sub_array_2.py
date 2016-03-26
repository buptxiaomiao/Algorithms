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

		(left_low,left_high,left_sum
				) = max_sub_array(low,mid,*arr)

		(right_low,right_high,right_sum
				) = max_sub_array(mid+1,high,*arr)

		(cross_low,cross_high,cross_sum
				) = find_max_crossing_sub_array(low,mid,high,*arr)

	if left_sum>right_sum and left_sum>cross_sum:
		return (left_low,left_high,left_sum)
	elif right_sum>left_sum and right_sum>cross_sum:
		return (right_low,right_high,right_sum)
	else:
		 return (cross_low,cross_high,cross_sum)
if __name__ == '__main__':
	(low,high,sum) = max_sub_array(0,len(a)-1,*a)
	result = a[low:high+1]
	print (result,sum)
