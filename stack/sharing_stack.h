/*************************************************************************
    > File Name: sharing_stack.h
    > Author: Miao 
    > Mail: buptwjh@outlook.com 
    > Created Time: 2016年04月13日 星期三 00时28分57秒
 ************************************************************************/

#include<iostream>
using namespace std;

const int SIZE = 1024;
class Sharing_Stack{
	private:
		int data[SIZE];
		int top1;
		int top2;
	public:
		Sharing_Stack();
		int Push(int head_tail,int s);
		int Pop(int head_tail = 1);
		bool Empty(int head_tail);
		bool Empty();
		bool Full();
};
Sharing_Stack::Sharing_Stack(){
	top1 = -1;
	top2 = SIZE;
}
int Sharing_Stack::Push(int head_tail,int s){
	if(not Full()){
		if(head_tail == 1){
			top1++;
			data[top1] = s;
			return s;
		}
		else{
			top2--;
			data[top2] = s;
			return s;
		}
	}
	else{
		cout<<"The Stack has already full.";
		return 0;
	}
}
int Sharing_Stack::Pop(int head_tail){
	if(not Empty(head_tail)){
		if(head_tail == 1){
			top1--;
			return data[top1+1];
		}
		else{
			top2++;
			return data[top2-1];
		}
	}
	else{
		cout<<"The Stack is Empty,can not pop anything.";
		return 0;
	}
}
bool Sharing_Stack::Empty(int head_tail){
	if(head_tail == 1 && top1 == -1)
		return true;
	else if(head_tail == 2 && top2 == SIZE)
		return true;
	else
		return false;
}
bool Sharing_Stack::Empty(){
	if(top1 == -1 && top2 == SIZE)
		return true;
	else 
		return false;
}
bool Sharing_Stack::Full(){
	if(top1+1 == top2)
		return true;
	else
		return false;
}
