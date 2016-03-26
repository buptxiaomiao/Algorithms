#########################################################################
#-*- coding:utf-8 -*-
# File Name: Max_sub_array_VIOLENCE.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月27日 星期日 03时16分07秒
#########################################################################
#!/usr/bin/env python2.7

a = [1,2,-3,4,6,4,-5,1,3,1]
def violence(*arr):
	length = len(arr)
	low_index = 0
	high_index = length-1
	temp_sum = 0
	max_sum = -100000
	
	for low  in range(0,length+1):
		for high in range(low,length+1):
			temp_sum = sum(arr[low:high+1])
			if temp_sum > max_sum:
				high_index = high
			if temp_sum >= max_sum:
				max_sum = temp_sum
				low_index = low
	return (low_index,high_index,max_sum)
if __name__ == '__main__':
	(low,high,sum) = violence(*a)
	print (a[low:high+1],sum)
