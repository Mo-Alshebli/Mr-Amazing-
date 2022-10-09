#include<iostream>
#include<string>
#include<algorithm>
#include<math.h>
using namespace std;
struct node{
	float data;
	node*next;
};
struct node_n{
char dat;
node_n *nextn;	
};
node*top=NULL;
node_n*top_n=NULL;
void push(float value);
void push_n(int value);
float pop();
char pop_n();
bool isEmpty();
bool isEmpty_n();
void dis();
void disn();
int operat(char c);
void infix(string in);
float test(float x, float y,char z);
int main(){
p:
string input;

cout<< "the operation is = ";
cin>>input;
cout<<endl;
infix(input);
cout<<"============================"<<endl;
goto p;
}
void push(float value){
node*temp=new node();
temp->data=value;
temp->next=top;
top=temp;
}
void push_n(int value){
node_n*temp=new node_n();
temp->dat=value;
temp->nextn=top_n;
top_n=temp;
}
float pop(){
node*temp=top;
float x= top->data;
top=temp->next;
delete temp;
return x;
}
char pop_n(){
node_n*temp=top_n;
char x= top_n->dat;
top_n=temp->nextn;
delete temp;
return x;
}
bool isEmpty(){
	return (top==NULL);
}
bool isEmpty_n(){
		return (top_n==NULL);
}
void dis(){
	node*temp=top;
	if(top==NULL)
	{
	cout<<"the list is empty"<<endl;
	}
	else
	{
		node*temp2=top;
		while(temp2!=NULL)
		{
			cout<<temp2->data<<endl;
			temp2=temp2->next;
		}
	}
}
void disn(){
	node_n*temp=top_n;
	if(top_n==NULL)
	{
	cout<<"the list is empty"<<endl;
	}
	else
	{
		node_n*temp2=top_n;
		while(temp2!=NULL)
		{
			cout<<temp2->dat<<endl;
			temp2=temp2->nextn;
		}
	}
}
 int operat(char c){
 	 if(c=='+'||c=='-')return 1;
 	else if(c=='*'||c=='/')return 2;
 	else if(c=='^')return 3;
 	else return 0;
 }
void infix(string in){
	int n=0;
	for(int i=0;i<in.length();i++)
	{
		if(in[i]==' ')continue;
		if(isalpha(in[i]))
				{
					cout<<" the enter is wrong "<<endl;
					break;
				}
		else if(isdigit(in[i]))
				{
					
					push(in[i]-'0');
				}
		else if(in[i]=='(')
				{
					push_n(in[i]);
				}
		else if(in[i]==')')
				{	
					while(top_n->dat!='(')
				{
					float x=pop();
					float y=pop();
					char z=pop_n();
					float c=test(x,y,z);
					push(c);
				}
					pop_n();
				}
		else if(in[i]=='+'||in[i]=='-'||in[i]=='*'||in[i]=='/'||in[i]=='^')
				{
					if(isEmpty_n())
				{
					push_n(in[i]);
				}
		else if(operat(top_n->dat)>=operat(in[i]))
				{
					float x=pop();
					float y=pop();
					char z=pop_n();
					float c=test(x,y,z);
					push_n(in[i]);
					push(c);																
				}
		else	
				{
					push_n(in[i]);
				}
				}
				{
				}																	
				}	
		while(top_n!=NULL)
				{
					float x=pop();
					float y=pop();
					char z=pop_n();
		    		float c=test(x,y,z);
					push(c);	
				}
					cout<<"result = "<<(top->data)<<endl;
}
float test(float x, float y,char z){
	switch(z)
	{
		case '+': return y+x; break;
		case '*': return y*x; break;
		case '/': return y/x; break;
		case '-': return y-x; break;
		case '^': return pow(y,x); break;
		default:return 1;break;
	}
}
