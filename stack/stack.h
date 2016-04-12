/*************************************************************************
    > File Name: stack.h
    > Author: Miao 
    > Mail: buptwjh@outlook.com 
    > Created Time: 2016年04月12日 星期二 23时58分45秒
 ************************************************************************/

#include<iostream>
using namespace std;

const int SIZE = 20;
class Stack{
	private:
		int data[SIZE];
		int top;
	public:
		Stack(){top = -1;}
		int Push(int);
		int Pop();
		bool Empty();
		bool Full();
};

int Stack::Push(int s){
	if(Full()){	
		cout<<"The Stack is full,can not push in anything.";
		return 0;
	}
	else{
		data[top+1] = s;
		top++;
		return s;
	}
}
int Stack::Pop(){
	if(Empty()){
		cout<<"The Stack is Empty,can not pop anything.";
		return 0;
	}
	else{
		top--;
		return data[top+1];
	}
}
bool Stack::Empty(){
	if(top == -1)
		return true;
	else
		return false;
}
bool Stack::Full(){
	if (top == SIZE-1)
		return true;
	else 
		return false;
}

