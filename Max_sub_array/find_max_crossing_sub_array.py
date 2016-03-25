#########################################################################
#-*- coding:utf-8 -*-
# File Name: find_max_crossing_sub_array.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月25日 星期五 20时13分35秒
#########################################################################
#!/usr/bin/env python2.7
q = [-1,5,6,5,2,3,-5,-6,2,8]
def find_max_crossing_sub_array(low,mid,high,*arr):
	left_sum = -10000
	temp_sum = 0
	left_index = low
	for i in reversed(range(low,mid+1)):
		temp_sum += arr[i]
		if temp_sum > left_sum:
			left_sum = temp_sum
			left_index = i
	right_sum = -1000
	temp_sum = 0
	right_index = high
	for i in range(mid+1,high+1):
		temp_sum += arr[i]
		if temp_sum > right_sum:
			right_sum = temp_sum
			right_index = i
	return (left_index,right_index,left_sum+right_sum)
if __name__ =='__main__':
	print find_max_crossing_sub_array(0,(len(q)-1)//2,len(q)-1,*q)
