#########################################################################
#-*- coding:utf-8 -*-
# File Name: Max_sub_array.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月25日 星期五 15时41分49秒
#########################################################################
#!/usr/bin/env python2.7
from copy import deepcopy
a = [-3,5,-8,2,7,10,-1,-2]
b = [10,9,5,-2,1000]
c = [-3,7,9,-6,0,8,-2,3,-5,9,-8,12,7]
d = [-1,-2,-3,-4,-5,-6,-7]
def Max_sub_array(*array):
	temp_sum = 0
	temp_arr = []
	max_sum = -10000
	max_arr = []
	for each in array:
		if temp_sum > 0:#之前的几个数是正的=>加上去#temp_sum + each>each
			temp_sum += each
			temp_arr.append(each)
		else :#之前的和是负的=>使和减小,不要
			temp_sum = each
			temp_arr = []
			temp_arr.append(each)
		if temp_sum > max_sum:
			max_sum = temp_sum
			max_arr = deepcopy(temp_arr)
	return (max_arr,max_sum)
if __name__ == '__main__':
	print Max_sub_array(*b)
	print Max_sub_array(*a)
	print Max_sub_array(*c)
	print Max_sub_array(*d)
