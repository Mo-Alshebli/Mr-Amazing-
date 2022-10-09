  #include<iostream>
#include<string>
using namespace std;
struct customers{
	int id;
	string name;
	int phone;
	string email;
	int age;
	string movie;
	int copies;
	string cha;
	customers*next;
};
customers*head_c=NULL;
string po;
struct DVD{
	int id;
	string movie;
	string stars;
	string production;
	string director;
	string production_company;
	int copies;
	int rent;
	DVD*next;
	
};
DVD*head=NULL;
int w;
void Back_ground();
void DVD_list();
void customers_list();
void add();
void Display_all();
void Display_special();
void remove();
void remove_c();
void delete_all();
void delete_all_c();
void Display_copies();
void Rent();
void revers();
void revers_D();
void add_customer();
void Display_all_c();
void came_back();
void Display_all_DVD_Rent();
void menu();
void menu_c();
void r();
 void search_c();	
int main(){
	Back_ground();
	
}
void Back_ground(){
	system("cls");      
	int n;
	cout<<"\t\t\twelcome in our store "<<endl;
	cout<<"\t\t     **************************"<<endl<<endl;
	cout<<"\t\t 1- The DVD list"<<endl;
	cout<<"\t\t 2- The customers list"<<endl;
	cout <<"\t\t     Enter number : ";
	cin>>n;
	switch(n)
	{
		case 1:DVD_list();break;
		case 2:customers_list();break;
		default:cout<<"please enter number from 1 to 3"<<endl;menu();	
	}	
}
void DVD_list(){	
	system("cls");      
	int b;
	cout<<"\t\t  the DVD list"<<endl;
	cout<<"\t\t****************"<<endl<<endl;
	cout<<"\t\t1- Add new DVD to list "<<endl;
	cout<<"\t\t2- delete all DVD from list"<<endl;
	cout<<"\t\t3- Display all List of DVD"<<endl;
	cout<<"\t\t4- Display special DVD from list"<<endl;
	cout<<"\t\t5- remove  one DVD"<<endl;
	cout<<"\t\t6- copies  from the DVD"<<endl;
	cout<<"\t\t7- revers the list"<<endl;
	cout<<"\t\t8- Back_ground"<<endl;

	cout<<"\t\tEnte the number : ";cin>>b;
		switch(b)
	{
		case 1:add();break;
		case 2:delete_all();break;
		case 3:Display_all();break;
		case 4:Display_special();break;	
		case 5:remove();break;
		case 6:Display_copies();break;
		case 7:revers();break;
		case 8:Back_ground();break;
		default:cout<<"please enter number from 1 to 7"<<endl;menu();	
	}	
}
void customers_list(){	
	system("cls");      
	int w;
	cout<<"\t\ttustomers list "<<endl<<endl;
	cout<<"\t\t******************"<<endl;
	cout<<"\t\t1- Add new customer "<<endl;	
	cout<<"\t\t2- delete all customer"<<endl;
	cout<<"\t\t3- Rent DVD "<<endl;
	cout<<"\t\t4- cane back "<<endl;
	cout<<"\t\t5- remove one cutomer"<<endl;
	cout<<"\t\t6- Search for one customer"<<endl;
	cout<<"\t\t7- Display all customers"<<endl;
	cout<<"\t\t8- Display all customer Rent"<<endl;
	cout<<"\t\t9- revers the list"<<endl;
	cout<<"\t\t10- Back_ground"<<endl;
	cout<<"\t\tEnter number : ";cin>>w;
		switch(w)
	{
		case 1: add_customer();break;
		case 2:delete_all_c();break;
		case 3:Rent();break;
		case 4:came_back();break;	
		case 5:remove_c();break;	
		case 6:search_c();break;
		case 7:Display_all_c( );break;
		case 8: Display_all_DVD_Rent();break;
		case 9:revers_D();break;
		case 10:Back_ground();break;
		default:cout<<"please enter number from 1 to 8"<<endl;menu_c();	
	}	
}
void add(){
	system("cls");      
	DVD*ADD=new DVD();
	cout<<"Enter the name of movie : ";cin>>ADD->movie;
	cout<<"Enter the name of stars : ";cin>>ADD->stars;
	cout<<"Enter the name of producer : ";cin>>ADD->production;
	cout<<"Enter the name of director : ";cin>>ADD->director;
	cout<<"Enter the name of production_company : ";cin>>ADD->production_company;
	cout<<"Enter the number of copies : ";cin>>ADD->copies;
	ADD->next=NULL;
if(head==NULL){	head=ADD;}
else
{
	DVD*temp=head;
	while(temp->next!=NULL)
	{		temp=temp->next;
	}	
	temp->next=ADD;
	ADD->next=NULL;
}menu();
}
void Display_all(){
	system("cls");      
	DVD*temp=head;
	
	if(head==NULL)
	{
	cout<<"the list of DVD is empty"<<endl;	menu();
	temp=temp->next;
menu();
	}
	else
	{
	temp=head;	
	while(temp!=NULL)
	{
	cout<<"\t================================"<<endl;
	cout<<"\tName of movie : "<<temp->movie<<endl;
	cout<<"\tName of stars : "<<temp->stars<<endl;
	cout<<"\tName of production : "<<temp->production<<endl;
	cout<<"\tName of director : "<<temp->director<<endl;
	cout<<"\tName of production company : "<<temp->production_company<<endl;
	cout<<"\tcopies : "<<temp->copies<<endl;
	cout<<"\tRents : "<<temp->rent<<endl;
	temp=temp->next;
	}	
		
}
menu();		
}
void menu(){
	
	cout<<"\n\n\t*************************\n";
	cout<<"\t1- came back to DVD list"<<endl;
	cout<<"\t2- came back to Back ground "<<endl;
	int b;
	cout<<"\t\tEnter number : ";
	cin>>b;	
	switch(b)
	{
		case 1:DVD_list();break;
		case 2:Back_ground();break;
    }
}
void menu_c(){
	
	cout<<"\n\n\t*************************\n";
	cout<<"\t1- came back to customers list"<<endl;
	cout<<"\t2- came back to Back ground "<<endl;
	int b;
	cout<<"\t\tEnter number : ";
	cin>>b;	
	switch(b)
	{
		case 1:customers_list();break;
		case 2:Back_ground();break;
    }
}
void revers_D()
{
	customers *temp=head_c->next;
	head_c->next=NULL;
	customers *temp2=temp->next;
	while(temp!=NULL)
	{
		temp->next=head_c;
		head_c=temp;
		temp=temp2;
		if(temp2!=NULL)
		temp2=temp2->next;
	}
	menu();
}
void revers()
{
	DVD *temp=head->next;
	head->next=NULL;
	DVD *temp2=temp->next;
	while(temp!=NULL)
	{
		temp->next=head;
		head=temp;
		temp=temp2;
		if(temp2!=NULL)
		temp2=temp2->next;
	}
	cout<<head->movie<<endl;
	menu();
}
void Display_special(){
	system("cls");      
	int po;
	int pos=0;
	cout<<"Enter the number of the DVD that you want to display : ";
	cin>>po;
	DVD*temp;
	if(head==NULL)
	{	cout<<"the list of DVD is empty"<<endl;menu();	}
	else
	{
	temp=head;	
	while(temp!=NULL)
	{
	if(pos==(po-1))
	{
	cout<<"\t============================="<<endl;
	cout<<"\tName of movie : "<<temp->movie<<endl;
	cout<<"\tName of stars : "<<temp->stars<<endl;
	cout<<"\tName of production : "<<temp->production<<endl;
	cout<<"\tName of director : "<<temp->director<<endl;
	cout<<"\tName of production company : "<<temp->production_company<<endl;
	cout<<"\tcopies : "<<temp->copies<<endl;
	cout<<"\tREnt : "<<temp->rent<<endl;
	}
	temp=temp->next;
	pos++;
	}		
	}
menu();	
}
void delete_all(){
	DVD*temp1,*temp;
	for(temp=head;temp;temp=temp1)
	{
		temp1=temp->next;
		delete temp;	
	}
	menu();
}
void delete_all_c(){
	customers*temp1,*temp;
	for(temp=head_c;temp;temp=temp1)
	{
		temp1=temp->next;
		delete temp;	
	}
menu_c();	
	}
void Display_copies(){
	system("cls");  
	string po;
	cout<<"Enter the name of the DVD that you want to display number of copies : ";
	cin>>po;
	DVD*temp;
	if(head==NULL)
	{	cout<<"the list of DVD is empty"<<endl;menu();	}
	else
	{
	temp=head;	
	while(temp!=NULL)
	{
	if(po==temp->movie)
	{
	cout<<"==========="<<endl;    
	cout<<"\t"<<temp->copies<<endl;	cout<<"==========="<<endl;    }
	temp=temp->next;
	}		
	}
menu();	
}
void remove(){
	
	int po;
	int pos=1;
	cout<<"Enter the number of the DVD that you want to delete : ";
	cin>>po;
	DVD*temp,temp2;
	if(po==1)
	{
	temp=head;
	head=head->next;
	
	delete temp;
	
		}
		else
		{
			temp=head;
			while((temp->next!=NULL)&&(pos<(po-1)))
			{
				temp=temp->next;
				pos++;
			}
		DVD*temp2=temp->next;
			temp->next=temp->next->next;
			delete temp2;
		}
		menu();
}
void remove_c(){
	
	int 
	po;
	int pos=1;
	cout<<"Enter the number of the DVD that you want to delete : ";
	cin>>po;
	customers*temp,temp2;
	if(po==1)
	{
	temp=head_c;
	head_c=head_c->next;
	delete temp;
		}
		else
		{
			temp=head_c;
			while((temp->next!=NULL)&&(pos<(po-1)))
			{
				temp=temp->next;
				pos++;
			}
		customers*temp2=temp->next;
			temp->next=temp->next->next;
			delete temp2;
		}
		menu_c();
}
void add_customer(){
	system("cls");      
	customers*ADD=new customers();
	cout<<"Enter the ID : ";cin>>ADD->id;
	cout<<"Enter the Name : ";cin>>ADD->name;
	cout<<"Enter the phone number : ";cin>>ADD->phone;
	cout<<"Enter the your age : ";cin>>ADD->age;
	cout<<"Enter the your e_mail : ";cin>>ADD->email;


	ADD->next=NULL;
if(head_c==NULL){	head_c=ADD;}
else
{
	customers*temp=head_c;
	while(temp->next!=NULL)
	{		temp=temp->next;
	}	
	temp->next=ADD;
}menu_c();
}	
void Display_all_c(){
		system("cls");  
	customers*temp;	
	if(head_c==NULL)
	{cout<<" the list is empty"<<endl;
	menu_c();
	temp=temp->next;}
	else
	{
	temp=head_c;	
	while(temp!=NULL)
	{
cout<<"\t=================="<<endl;		
	cout<<"\tID : "<<temp->id<<endl;
	cout<<"\tName : "<<temp->name<<endl;
	cout<<"\tage : "<<temp->age<<endl;
	cout<<"\tphone : "<<temp->phone<<endl;
	cout<<"\te_mail : "<<temp->email<<endl;
	cout<<"\tmovies : "<<temp->movie<<endl;
	cout<<"\tcpies : "<<temp->copies<<endl;

	temp=temp->next;
	}		
}
menu_c();	
}
void search_c(){
system("cls");
	int po;
	int pos=0;
	cout<<"Enter the ID of the customer that you want to display : ";
	cin>>po;
	customers*temp;
	if(head_c==NULL)
	{
		cout<<"the list of DVD is empty"<<endl;	
	}
	else
	{
	temp=head_c;	
	while(temp!=NULL)
	{
	if(pos==(po-1))
	{cout<<"\t===================="<<endl;
	cout<<"\tID : "<<temp->id<<endl;
	cout<<"\tName of customer : "<<temp->name<<endl;
	cout<<"\tMovie :"<<temp->movie<<endl;
	cout<<"\tphone :"<<temp->phone<<endl;
	cout<<"\tE_mail : "<<temp->email<<endl;
	cout<<"\tcopies :"<<temp->copies<<endl;
	}
	temp=temp->next;
	pos++;
	}		
	}
	menu_c();	
}
void Display_all_DVD_Rent(){
	system("cls");  
	DVD*rent=head;
	if(head==NULL)
	{cout<<" our DVD is empty"<<endl;menu_c();	}
else if(rent->next==NULL)
	{
		cout<<"\t====================="<<endl;
			cout<<"\t   the movie : "<<rent->movie<<endl;
		cout<<"\t   rent"<<rent->rent<<endl;
	menu_c();	
	}
	else 
	while(rent!=NULL)
	{		cout<<"\t====================="<<endl;
		cout<<"\t   the movie : "<<rent->movie<<endl;
		cout<<"\t   rent"<<rent->rent<<endl;	
	rent=rent->next;	
	}

	menu_c();

}
void Rent(){
	l:
	DVD*D=head;
	customers*c=head_c;
	int e;
	cout<<"enter your ID : ";cin>>e;
	if(head_c==NULL)
	{
		cout<<"the list is empty"<<endl;
		menu_c();
	}
	if(c->next==NULL)
	{
		if(e==c->id)
		{
k:

	DVD*D=head;
	string g;
	cout<<"Enter the name of movie that you want rent it from us : ";cin>>g;
	if(head==NULL)
	{
		cout<<"the list is empty "<<endl;
		menu();
	}
	if (D->next==NULL)
	{
		if(g==D->movie)
		{
			if(g!=c->movie)
			{
			
			int h;
			cout<<"Enter How many copies you want rent : ";cin>>h;
			if(h<D->copies)
			{
				c->movie=g;
				cout<<" the rent have done"<<endl;
				D->copies=D->copies-h;
				D->rent=D->rent+h;
				c->copies=c->copies+h;
				menu();	
		}
		else{
			goto k;
		}
		
		
	}
}else
{
	cout<<" you have just one movie to rent it !!!!!!!!"<<endl;
	menu_c();
}
}
	else
	{
		while(D->next!=NULL)
		{
			if(g==D->movie)
			{
				n:
				int h;
			cout<<"Enter How many copies you want rent : ";cin>>h;
			if(h<D->copies)
			{
				int i;
								c->movie=g;

				cout<<" the rent have done!!!!!!!!!!!"<<endl;
				D->copies=D->copies-h;
				D->rent=D->rent+h;
				c->copies=c->copies+h;	
		
				menu_c();
			}
			
				
				
			}
			else
			{
				D=D->next;
			}
			
	
		}
		if (D->next==NULL)
	{
		
	if(g==D->movie)
			{
				nn:
				int h;
			cout<<"Enter How many copies you want rent : ";cin>>h;
			if(h<D->copies)
			{
				int i;				c->movie=g;

				cout<<" the rent have done!!!!!!!!!!!"<<endl;
				D->copies=D->copies-h;
				D->rent=D->rent+h;
				c->copies=c->copies+h;	
		
				menu_c();
			}
			else
			{
				cout<<" the nuber is big !!!!!!!!"<<endl;
				goto nn;
			}
				
				
			}
			else 
			{
				cout<<"the movie is not fount try again !!!!!!!!"<<endl;
				goto k;
			}
}
	}			
		}
		else
		{
			cout<<" your id wrong please try again "<<endl;
			
			goto l;
		}
		
}
	else
	{
		c=head_c;
		while(c->next!=NULL)
		{
		
		if(e==c->id)
		{
k1:

	DVD*D=head;
	string g;
	cout<<"Enter the name of movie that you want rent it from us : ";cin>>g;
	if(head==NULL)
	{
		cout<<"the list is empty "<<endl;
		menu_c();
	}
	if (D->next==NULL)
	{
		if(g==D->movie)
		{
			int h;
			cout<<"Enter How many copies you want rent : ";cin>>h;
			if(h<D->copies)
			{				c->movie=g;

				cout<<" the rent have done"<<endl;
				D->copies=D->copies-h;
				D->rent=D->rent+h;
					
		}
		else{
			goto k1;
		}
		
		
	}
}
	else
	{
		while(D->next!=NULL)
		{
			if(g==D->movie)
			{
				n1:
				int h;
			cout<<"Enter How many copies you want rent : ";cin>>h;
			if(h<D->copies)
			{				c->movie=g;

				int i;
				cout<<" the rent have done!!!!!!!!!!!"<<endl;
				D->copies=D->copies-h;
				D->rent=D->rent+h;
				c->copies=c->copies+h;	
		
				menu_c();
			}
			
				
			cout<<"the movie is not fount try again !!!!!!!!"<<endl;
				goto n1;	
			}
			else
			{
				D=D->next;
			}
			
			
		}
		if (D->next==NULL)
	{
	if(g==D->movie)
			{
				nn1:
				int h;
			cout<<"Enter How many copies you want rent : ";cin>>h;
			if(h<D->copies)
			{
				int i;				c->movie=g;
				cout<<" the rent have done!!!!!!!!!!!"<<endl;
				D->copies=D->copies-h;
				D->rent=D->rent+h;
				c->copies=c->copies+h;	
		
				menu_c();
			}
			else
			{
				cout<<" the nuber is big !!!!!!!!"<<endl;
				goto nn1;
			}			
			}
			else 
			{
				cout<<"the movie is not fount try again !!!!!!!!"<<endl;
				goto k;
			}
}
	}		
	}
		else
		{
			c=c->next;
		}
	}
	if(c->next==NULL)
	{
		if(e==c->id)
		{
			k2:

	DVD*D=head;
	string g;
	cout<<"Enter the name of movie that you want rent it from us : ";cin>>g;
	if(head==NULL)
	{
		cout<<"the list is empty "<<endl;
		menu_c();
	}
	if (D->next==NULL)
	{
		if(g==D->movie)
		{
			int h;
			cout<<"Enter How many copies you want rent : ";cin>>h;
			if(h<D->copies)
			{				c->movie=g;
				cout<<" the rent have done"<<endl;
				D->copies=D->copies-h;
				D->rent=D->rent+h;			
		}
		else{
			goto k2;
		}
	}
}
	else
	{
		while(D->next!=NULL)
		{
			if(g==D->movie)
			{
				n2:
				int h;
			cout<<"Enter How many copies you want rent : ";cin>>h;
			if(h<D->copies)
			{
				int i;				c->movie=g;
				cout<<" the rent have done!!!!!!!!!!!"<<endl;
				D->copies=D->copies-h;
				D->rent=D->rent+h;
				c->copies=c->copies+h;	
				menu_c();
			}
			cout<<"the movie is not fount try again !!!!!!!!"<<endl;
				goto n2;	
			}
			else
			{
				D=D->next;
			}		
		}
		if (D->next==NULL)
	{
	if(g==D->movie)
			{ 
				nn3:
				int h;
			cout<<"Enter How many copies you want rent : ";cin>>h;
			if(h<D->copies)
			{
				int i;				c->movie=g;
				cout<<" the rent have done!!!!!!!!!!!"<<endl;
				D->copies=D->copies-h;
				D->rent=D->rent+h;
				c->copies=c->copies+h;	
				menu_c();
			}
			else
			{
				cout<<" the nuber is big !!!!!!!!"<<endl;
				goto nn3;
			}			
			}
			else 
			{
				cout<<"the movie is not fount try again !!!!!!!!"<<endl;
				goto k;
			}
}
	}
		}
		else
		{
			cout<<" your id wrong please try again "<<endl;	
			goto l;
		}		
	}	
}
}
void came_back(){
	customers*b=head_c;
	DVD*d=head;
int r;
cout<<"Enter your ID : ";cin>>r;
	if(head_c==NULL)
	{
		cout<<"the list is empty !!!!!!!!!!!1"<<endl;
		menu_c();
	}
	if(b->next==NULL)
	{
		if(r==b->id)
		{int w;
			cout<<"Enter How many copies you want to came back : ";cin>>w;
		b->copies=b->copies-w;
		d->copies=d->copies+w;
		d->rent=d->rent-w;
		menu_c();
		}
		else
		{
			cout<<"You enter a wrong id pleas try againe :"<<endl;
			menu_c();	
		}
	}
	else
	{
		while(b->next!=NULL)
		{
				if(r==b->id)
		{int w;
			cout<<"Enter How many copies you want to came back : ";cin>>w;
		b->copies=b->copies-w;
		d->copies=d->copies+w;
		d->rent=d->rent-w;
		menu_c();
		}
		else
		{		b=b->next;		
		}
		}	
	}
		if(b->next==NULL)
	{
		if(r==b->id)
		{int w;
			cout<<"Enter How many copies you want to came back : ";cin>>w;
		b->copies=b->copies-w;
		d->copies=d->copies+w;
		d->rent=d->rent-w;
		menu_c();
		}
		else
		{
			cout<<"You enter a wrong id pleas try againe :"<<endl;
			menu_c();
			
		}	
	}	
}
	
	
	
	
	
	
	
	
	
