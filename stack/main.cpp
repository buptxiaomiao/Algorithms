/*************************************************************************
    > File Name: main.cpp
    > Author: Miao 
    > Mail: buptwjh@outlook.com 
    > Created Time: 2016年04月13日 星期三 00时20分05秒
 ************************************************************************/

#include<iostream>
#include "sharing_stack.h"
using namespace std;

int main(){
	Sharing_Stack q;
	cout<<q.Push(1,100)<<endl;
	cout<< q.Push(2,999)<<endl;
	cout<<q.Push(1,200)<<endl;
	cout<< q.Pop(1)<<endl;
	cout<< q.Pop(2)<<endl;
	cout<< q.Empty(2)<<endl;
	cout<< q.Pop(1)<<endl;
	cout<< q.Empty(1)<<endl;
	return 0;
}


