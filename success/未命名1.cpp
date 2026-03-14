#include<iostream>
#include<stdlib.h>
#define OK 1
#define OVERFLOW -2
#define MAXSIZE 100
#define ERROR -1
using namespace std;
typedef int Status;
typedef char Elemtype;
typedef struct
{
	Elemtype *elem;
	int length;
}sqlist;
Status initlist(sqlist &l)
{
	l.elem=new Elemtype[MAXSIZE];
	if(!l.elem) exit(OVERFLOW);
	l.length=0;
	return OK;
}
void destroylist(sqlist &l)
{
	if(l.elem) delete [] l.elem;	
}
void clearlist(sqlist &l)
{
	l.length=0;	
}
int getlength(sqlist l)
{
	return l.length;
} 
int isempty(sqlist l)
{
	if (l.length==0) return 1;
	else return 0;
}
int getelem(sqlist l,int i,Elemtype &e)
{
	if(i<1 || i>l.length) return ERROR;
	e=l.elem[i-1];
	return OK;
}
int main()
{
	
}
