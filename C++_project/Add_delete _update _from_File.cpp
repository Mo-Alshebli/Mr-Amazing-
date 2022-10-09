#include<iostream>
#include<string>
#include<fstream>
using namespace std;
void password();
void displayall_t();
void background();
void studen();
void Teacher();
void Outher();
void add_t();
void add();
void displayall();
void search();
void search_t();
void delet();
void delet_t();
void update();
void update_t();
struct student{
	char num[250];
	int ID;
	char name[25];
	int age;
	int year;
	int specialty;
	double Account;
	double  Reduction;
	double total;
}v;
int main()
{

	password();
	system("pause");

}
void password()//this is the profile of the programm it has the bassword and username
{
c:
	system("cls");
	int o;
	int pass = 1;
	string user = "q";
	int passwored;
	string username;
	cout << "\n\n\t\t=======================\n";
	cout << "\t\tenter the username \n\t\t-----------------";
	cin >> username;
	cout << "\t\t=======================\n";
	cout << "\t\tenter the password \n\t\t------------------";
	cin >> passwored;
	if (passwored == pass&&username == user)
	{
		cout << "your password and username is correct !!!!!!!\n";
		background();
	}
	else {
		cout << "your password and username is wrong !!!!!!!\n";
		cout << "you want try again \n 1- Yes \n 2- NO and go out \n";
		cin >> o;
		switch (o)
		{
		case 1:goto c;
		case 2:exit(0);
		default:cout << "pleas choose 1 or 2 \n";
			break;
		}
	}
	system("pause");
}
void background()//this is the background after the bassword it has three option one for information of student the other for teacher the last on for other information 
{
	int ope;
	system("cls");

	cout << "\n\n\n\t==========================================================\n";
	cout << "                      welcome to our programe \n";
	cout << "\t==========================================================\n\n";
	cout << " \t\t1- Student information\n\n";
	cout << " \t\t2- Teacher information\n\n";
	cout << " \t\t3-Outher information about our university\n\n";
	cout << "\t==========================================================\n";
	cout << "\t\tenter the opreation : \n\t\t---------------------"; cin >> ope;		system("cls");
	switch (ope){
	case 1:studen(); break;
	case 2:Teacher(); break;
	case 3:Outher(); break;
	default:cout << "the number is wrong enter between 1----->3\n";
		system("cls");
	}
}
void studen()//this is the first option in the background and it has many options like add new studen , delete,search,update,displayall student information and came back to background 
{
	int op;
	do
	{
		cout << "\n\n\t=============================================\n";
		cout << "                Welcome to our university \n";
		cout << "\t==============================================\n";
		cout << "\t\t1- add new student\n\n";
		cout << "\t\t2- Display_all student\n\n";
		cout << "\t\t3- search \n\n";
		cout << "\t\t4- update \n\n";
		cout << "\t\t5- Delete \n\n";
		cout << "\t\t6- come back to the main menu \n\n";
		cout << "\t\t7- exit \n\n";
		cout << "\t\t========================================\n";
		cout << "\t\tEnter the opreation  : \n";
		cout << "\t\t-----------------------"; cin >> op;
		switch (op)
		{
		case 1:add(); break;
		case 2:displayall(); break;
		case 3:search(); break;
		case 4:update(); break;
		case 5:delet(); break;
		case 6:background(); break;
		case 7:exit(0); break;
		default:cout << "the number is wrong enter between 1----->7\n";
		}
	} while (op<7);
	system("cls");
	if (op>7)
	{
		cout << "the number is wrong enter between 1----->7\n";
		student();
	}
}
void Teacher()//this is the second option in the background and it has many options like add new teacher , delete,search,update,displayall teacher information and came back
{
	int oo;
	cout << "\t\t============================================\n";
	cout << "\t\t\tteacher infromation\n";
	cout << "\t\t============================================\n";
	cout << "\t\t\t1- add new teacher\n" << "\t\t\t2- display all  \n" << "\t\t\t3- search  \n" << "\t\t\t4- update  \n" << "\t\t\t5- Delete  \n" << "\t\t\t6- back to the main mune\n" << "\t\t\t7- exit\n ";
	cout << "\t\t=================================================\n";
	cout << "Enter the opeartion  : \n";
	cout << "-----------------------"; cin >> oo;
	cout << endl << endl;
	switch (oo)
	{
	case 1:add_t(); break;
	case 2:displayall_t(); break;
	case 3:	search_t(); break;
	case 4:	update_t(); break;
	case 5:	delet_t(); break;
	case 6:background(); break;
	case 7:exit(0); break;
	default:cout << "the number is wrong enter between 1----->7\n";
	}
}
void Outher()//this the last option in background and it has information about the university
{
	int e;
	cout << "\n\n\t\t==============================================\n\t\t";
	cout << "  1-what is the new in our university \n\t\t  2-About our university \n\t\t  3-Our seen\n\t\t  4-come back to background\n\t\t  5-exit\n";
	cout << "\t\t==============================================\n\t\t";
	cout << "Enter thr opreation : \n\t\t---------------------";
	cin >> e;
	system("cls");
	switch (e)
	{
	case 1:cout << "\n\t\t      what is the new in our university\n\t\t=============================================\n\t\t  The important things in our university is\n\t\t  we have a new specialty this year and\n\t\t  this specialty is the future of the earth \n\t\t  and when you will finsh you will get job\n\t\t\t very fast\n\t\t==============================================\n"; break;
	case 2:cout << "\n\t\t\tAbout our university\n\t\t=================================================\n\t\tour university is the best university in yemen \n\t\tthe first thing is we have the best docters in yemen \n\t\tour building is the best from the location and distance\n\t\twe give the student every thing that he want  \n\t\t=================================================\n"; break;
	case 3:cout << "\n\t\t\t   our seen\n\t\t=====================================\n\t\tto be the best university in yemen  \n\t\t===================================\n"; break;
	case 4:background();
	case 5:exit(0); break;
	default:cout << "the number that you enter is wrong\n";
		break;
	}
	system("pause");
	Outher();
	system("cls");
}
void add()//this is the first option in student function and it add new student nd save it in fail
{
	system("cls");
	ofstream stu;
	stu.open("student.txt", ios::app);
	cout << "\n\n\t--------------------------------\n";
	cout << "\t\tID : "; cin >> v.ID; cin.ignore();
	cout << "\t\tname : "; cin.getline(v.name, 250); h:
x :
	cout << "\t\tage : "; cin >> v.age;	cin.ignore();	if (v.age > 100){ cout << "the age is so high enter less than 100\n"; goto x; }
  char num[12];
  int size;
re:	cout << "\t\tphone : ";
  cin.getline(num, 12);
  size = strlen(num);
  for (int i = 0; i < size; i++)
  {
	  if (int(num[i])<48 || int(num[i])>57)
	  {
		  cout << "error\n";
		  goto re;
	  }
  }
  if (size != 9)
  {
	  cout << "error\nmost be 9 number";
	  goto re;
  }
  else if (num[0] != '7')
  {
	  cout << "must begin with '7'\n";
	  goto re;
  }
  else if (num[1] != '7'&&num[1] != '3'&&num[1] != '1'&&num[1] != '0')
  {
	  cout << "must begin with '77', '73' ,'70','71'\n";
	  goto re;
  }
o:
  cout << "\t\tyear of graduation : "; cin >> v.year; if (v.year > 2020 || v.year < 2015){ cout << "the year of graduation is wrong \n"; goto o; }
  cout << "\n1-Artificial intelligence\n2- cyber security\n3- IT \n4- Accounting\n5- pharmacy\n6- dentistry\n7- metacronics\n8- education\n9- engineering\n10- law \nenter the number of your specialty :  ";
  cin >> v.specialty;
  stu << v.ID << "|" << v.name << "|" << num << "|";
  stu << v.age << "|" << v.year << "|";
  switch (v.specialty)
  {
  case 1: stu << "Artificial intelligence"; if (v.specialty == 1){ v.Account = 10000; v.Reduction = (v.Account * 0.40); v.total = v.Account - v.Reduction; }	break;
  case 2: stu << "cyber security"; if (v.specialty == 2){ v.Account = 9000; v.Reduction = (v.Account * 0.40); v.total = v.Account - v.Reduction; }	break;
  case 3: stu << " IT"; if (v.specialty == 3){ v.Account = 8000; v.Reduction = (v.Account * 0.40); v.total = v.Account - v.Reduction; }	break;
  case 4: stu << "Accounting"; if (v.specialty == 4){ v.Account = 7000; v.Reduction = (v.Account * 0.40); v.total = v.Account - v.Reduction; }	break;
  case 5: stu << " pharmacy"; if (v.specialty == 5){ v.Account = 6000; v.Reduction = (v.Account * 0.40); v.total = v.Account - v.Reduction; }	break;
  case 6: stu << "dentistry"; if (v.specialty == 6){ v.Account = 5000; v.Reduction = (v.Account * 0.40); v.total = v.Account - v.Reduction; }	break;
  case 7: stu << "metacronics"; if (v.specialty == 7){ v.Account = 4000; v.Reduction = (v.Account * 0.40); v.total = v.Account - v.Reduction; }	break;
  case 8: stu << "education";	if (v.specialty == 8){ v.Account = 3000; v.Reduction = (v.Account * 0.40); v.total = v.Account - v.Reduction; } break;
  case 9: stu << "engineering"; if (v.specialty == 9){ v.Account = 2000; v.Reduction = (v.Account * 0.40); v.total = v.Account - v.Reduction; }	break;
  case 10: stu << "law";	if (v.specialty == 10){ v.Account = 1000; v.Reduction = (v.Account * 0.40); v.total = v.Account - v.Reduction; } break;
  default:stu << "the number is not found please enter between 1------->10/n";
  }
  if ((v.specialty) >10)
  {
	  stu << "the number is not found please enter between 1------->10/n";
	  add();
  }
  stu << "|" << v.Account << "|" << v.Reduction << "|" << v.total << "|\n";
  cout << "seccessful add!!!!!!!!!!!!!!!!!";
  system("cls");
}
void add_t()//this is the first option in teacher function and it add new teacher and save it in fail
{
	system("cls");
	ofstream stu;
	stu.open("TTT.txt", ios::app);
	cout << "\n\n\t--------------------------------\n";
	cout << "\t\tID : "; cin >> v.ID; cin.ignore();
	cout << "\t\tname : "; cin.getline(v.name, 250); h:
x :
	cout << "\t\tage : "; cin >> v.age;	cin.ignore();	if (v.age > 100){ cout << "the age is so high enter less than 100\n"; goto x; }
  char num[12];
  int size;
re:	cout << "\t\tphone : ";
  cin.getline(num, 12);
  size = strlen(num);
  for (int i = 0; i < size; i++)
  {
	  if (int(num[i])<48 || int(num[i])>57)
	  {
		  cout << "error\n";
		  goto re;
	  }
  }
  if (size != 9)
  {
	  cout << "error\nmost be 9 number";
	  goto re;
  }
  else if (num[0] != '7')
  {
	  cout << "must begin with '7'\n";
	  goto re;
  }
  else if (num[1] != '7'&&num[1] != '3'&&num[1] != '1'&&num[1] != '0')
  {
	  cout << "must begin with '77', '73' ,'70','71'\n";
	  goto re;
  }
o:
  cout << "\t\tyear of graduation : "; cin >> v.year; if (v.year > 2020 || v.year < 2015){ cout << "the year of graduation is wrong \n"; goto o; }

  cout << "\n1-Artificial intelligence\n2- cyber security\n3- IT \n4- Accounting\n5- pharmacy\n6- dentistry\n7- metacronics\n8- education\n9- engineering\n10- law \nenter the number of your specialty :  ";
  cin >> v.specialty;
  stu << v.ID << "|" << v.name << "|" << num << "|";
  stu << v.age << "|" << v.year << "|";
  switch (v.specialty)
  {
  case 1: stu << "Artificial intelligence"; if (v.specialty == 1){ v.Account = 10000; }	break;
  case 2: stu << "cyber security"; if (v.specialty == 2){ v.Account = 9000; }	break;
  case 3: stu << " IT"; if (v.specialty == 3){ v.Account = 8000; }	break;
  case 4: stu << "Accounting"; if (v.specialty == 4){ v.Account = 7000; }	break;
  case 5: stu << " pharmacy"; if (v.specialty == 5){ v.Account = 6000; }	break;
  case 6: stu << "dentistry"; if (v.specialty == 6){ v.Account = 5000; }	break;
  case 7: stu << "metacronics"; if (v.specialty == 7){ v.Account = 4000; }	break;
  case 8: stu << "education";	if (v.specialty == 8){ v.Account = 3000; } break;
  case 9: stu << "engineering"; if (v.specialty == 9){ v.Account = 2000; }	break;
  case 10: stu << "law";	if (v.specialty == 10){ v.Account = 1000; } break;
  default:cout << "the number is not found please enter between 1------->10/n";
  }
  if ((v.specialty) >10)
  {
	  stu << "the number is not found please enter between 1------->10/n";
	  add_t();
  }
  stu << "|" << v.Account << "|\n";
  cout << "seccessful add!!!!!!!!!!!!!!!!!";
  stu.close();
  system("cls");
  Teacher();
}
void displayall()//this is the second option in student function and it display all student in fail
{
	char data[50000];
	fstream file("student.txt", ios::in);
	system("cls");
	while (!file.eof())
	{
		file.getline(data, 5000);
		cout << endl << data << endl;
	}
	file.close();
}
void displayall_t()//this is the second option in teacher function and it display all teacher in fail
{
	char data[500000];
	fstream file("TTT.txt", ios::in);
	system("cls");
	while (!file.eof())
	{
		file.getline(data, 5000);
		cout << endl << data << endl;
	}
	file.close();
	Teacher();
}
void search()//this the third option in student function and it search about any student you want in fail by phone 
{
	system("cls");
	ifstream stud;
	stud.open("student.txt", ios::in);
	char nu[25];
	char n[25];
	char ge[25];
	char yy[25];
	char nn[25];
	char xx[25];
	char aa[25];
	char a[25];
	char yea[25];
	char id[25];
	cin.ignore();
	cout << "\n======================================\n";
	cout << "enter the phone number  for search : \n------------------------------------";
	cin.getline(a, 25);
	bool x = false;
	cout << "\nID  name   phone    age  year   specialty            Account   Reduction  total" << endl;
	cout << "\n==============================================================================\n";
	while (!stud.eof())
	{
		stud.getline(nu, 25, '|');
		stud.getline(n, 25, '|');
		stud.getline(id, 25, '|');
		stud.getline(ge, 25, '|');
		stud.getline(yea, 25, '|');
		stud.getline(xx, 25, '|');
		stud.getline(yy, 25, '|');
		stud.getline(nn, 25, '|');
		stud.getline(aa, 25, '|');
		if (strcmp(id, a) == 0)
		{
			cout << "\n" << nu << "  " << n << "   " << id << "  " << ge << "  " << yea << "  " << xx << "   " << yy << "    " << nn << "  " << aa << endl;
			cout << "\n=============================================================================\n";
			x = true;
			break;
		}
	}
	if (x == false)
		cout << "not found!!!!!!!!!!!!!\n";
	stud.close();
}
void search_t()//this the third option in teacher function and it search about any teacher you want in fail by phone
{
	system("cls");
	ifstream stud;
	stud.open("TTT.txt", ios::in);
	char nu[25];
	char n[25];
	char ge[25];
	char yy[25];
	char nn[25];
	char xx[25];
	char aa[25];
	char a[25];
	char yea[25];
	char id[25];
	cin.ignore();
	cout << "\n======================================\n";
	cout << "\nenter the phone number  for search : \n------------------------------------";
	cin.getline(a, 25);
	bool x = false;
	cout << "\nID  name   phone    age  year   specialty     salary   " << endl;
	while (!stud.eof())
	{
		stud.getline(nu, 25, '|');
		stud.getline(n, 25, '|');
		stud.getline(id, 25, '|');
		stud.getline(ge, 25, '|');
		stud.getline(yea, 25, '|');
		stud.getline(xx, 25, '|');
		stud.getline(yy, 25, '|');
		if (strcmp(id, a) == 0)
		{
			cout << "================================================================\n";
			cout << "\n" << nu << "  " << n << "   " << id << "  " << ge << "  " << yea << "  " << xx << "   " << yy << endl;
			cout << "================================================================\n";
			x = true;
			break;
		}
	}
	if (x == false)
		cout << "not found!!!!!!!!!!!!!\n";
	stud.close();
	Teacher();
}
void update()//this the fourth option in student function and it update about any information student you want in fail by phone
{
	fstream stud;
	fstream temp;
	stud.open("student.txt", ios::in);
	temp.open("temp.txt", ios::out);
	char ID[25];
	char name[25];
	char age[25];
	char phone[25];
	char year[25];
	char specialty[25];
	char Account[25];
	char  Reduction[25];
	char total[25];
	char a[25];
	cin.ignore();
	cout << "\n\tenter the phone number to delete recored : ";
	cin.getline(a, 25);
	while (!stud.eof())
	{
		stud.getline(ID, 25, '|');
		stud.getline(name, 25, '|');
		stud.getline(phone, 25, '|');
		stud.getline(age, 25, '|');
		stud.getline(year, 25, '|');
		stud.getline(specialty, 25, '|');
		stud.getline(Account, 25, '|');
		stud.getline(Reduction, 25, '|');
		stud.getline(total, 25);
		if (strcmp(phone, a) == 0)
		{
			cout << "\n\tEnter new value of recored \n";
			cout << "\n ID : ";
			cin.getline(ID, 25);
			cout << "\n name : ";
			cin.getline(name, 25);
			cout << "\n phone : ";
			cin.getline(phone, 25);
			cout << "\n age : ";
			cin.getline(age, 25);
			cout << "\n year : ";
			cin.getline(year, 25);
			cout << "\n specialty : ";
			cin.getline(specialty, 25);
			cout << "\n Account : ";
			cin.getline(Account, 25);
			cout << "\n Reduction : ";
			cin.getline(Reduction, 25);
			cout << "\n total : ";
			cin.getline(total, 25);
			temp << ID << '|' << name << '|' << phone << '|' << age << '|' << year << '|' << specialty << '|' << Account << '|' << Reduction << '|' << total << '\n';
		}
		else
		{
			temp << ID << '|' << name << '|' << phone << '|' << age << '|' << year << '|' << specialty << '|' << Account << '|' << Reduction << '|' << total << '\n';
		}
	}
	temp.close();
	stud.close();
	stud.open("student.txt", ios::out);
	temp.open("temp.txt", ios::in);
	while (!temp.eof())
	{
		temp.getline(ID, 25, '|');
		temp.getline(name, 25, '|');
		temp.getline(phone, 25, '|');
		temp.getline(age, 25, '|');
		temp.getline(year, 25, '|');
		temp.getline(specialty, 25, '|');
		temp.getline(Account, 25, '|');
		temp.getline(Reduction, 25, '|');
		temp.getline(total, 25);
		stud << ID << '|' << name << '|' << phone << '|' << age << '|' << year << '|' << specialty << '|' << Account << '|' << Reduction << '|' << total << '\n';
	}
	temp.close();
	stud.close();
	remove("temp.txt");
	cout << "\n \t\tdone !!!!!!!!!!!!!!!!!\n";
	system("cls");
	studen();
}
void update_t()//this the fourth option in teacher function and it update about any information teacher you want in fail by phone
{
	fstream stud;
	fstream temp;
	stud.open("TTT.txt", ios::in);
	temp.open("temp.txt", ios::out);
	char ID[25];
	char name[25];
	char age[25];
	char phone[25];
	char year[25];
	char specialty[25];
	char Account[25];
	char a[25];
	cin.ignore();
	cout << "\n\tenter the phone number to update recored : ";
	cin.getline(a, 25);
	while (!stud.eof())
	{
		stud.getline(ID, 25, '|');
		stud.getline(name, 25, '|');
		stud.getline(phone, 25, '|');
		stud.getline(age, 25, '|');
		stud.getline(year, 25, '|');
		stud.getline(specialty, 25, '|');
		stud.getline(Account, 25);
		if (strcmp(phone, a) == 0)
		{
			cout << "\n\tEnter new value of recored \n";
			cout << "\n ID : ";
			cin.getline(ID, 25);
			cout << "\n name : ";
			cin.getline(name, 25);
			cout << "\n phone : ";
			cin.getline(phone, 25);
			cout << "\n age : ";
			cin.getline(age, 25);
			cout << "\n year : ";
			cin.getline(year, 25);
			cout << "\n specialty : ";
			cin.getline(specialty, 25);
			cout << "\n salary : ";
			cin.getline(Account, 25);
			temp << ID << '|' << name << '|' << phone << '|' << age << '|' << year << '|' << specialty << '|' << Account << '\n';
		}
		else
		{
			temp << ID << '|' << name << '|' << phone << '|' << age << '|' << year << '|' << specialty << '|' << Account << '\n';
		}
	}
	temp.close();
	stud.close();
	stud.open("TTT.txt", ios::out);
	temp.open("temp.txt", ios::in);
	while (!temp.eof())
	{
		temp.getline(ID, 25, '|');
		temp.getline(name, 25, '|');
		temp.getline(phone, 25, '|');
		temp.getline(age, 25, '|');
		temp.getline(year, 25, '|');
		temp.getline(specialty, 25, '|');
		temp.getline(Account, 25);
		stud << ID << '|' << name << '|' << phone << '|' << age << '|' << year << '|' << specialty << '|' << Account << '\n';
	}
	temp.close();
	stud.close();
	remove("temp.txt");
	system("cls");
	cout << "\n done the Update !!!!!!!!!!!!!!!!!\n";
	Teacher();
}
void delet()//this the 5th option in student function and it delete  any information student you want in fail by phone
{
	fstream stud;
	fstream temp;
	stud.open("student.txt", ios::in);
	temp.open("temp.txt", ios::out);
	char ID[25];
	char name[25];
	char age[25];
	char phone[25];
	char year[25];
	char specialty[25];
	char Account[25];
	char  Reduction[25];
	char total[25];
	char a[25];
	cin.ignore();
	cout << "\n\tenter the phone number to delete recored : ";
	cin.getline(a, 25);
	while (!stud.eof())
	{
		stud.getline(ID, 25, '|');
		stud.getline(name, 25, '|');
		stud.getline(phone, 25, '|');
		stud.getline(age, 25, '|');
		stud.getline(year, 25, '|');
		stud.getline(specialty, 25, '|');
		stud.getline(Account, 25, '|');
		stud.getline(Reduction, 25, '|');
		stud.getline(total, 25);
		if (strcmp(phone, a) == 0)
		{
			continue;
		}
		else
		{
			temp << ID << '|' << name << '|' << phone << '|' << age << '|' << year << '|' << specialty << '|' << Account << '|' << Reduction << '|' << total << '\n';
		}
	}
	temp.close();
	stud.close();
	stud.open("student.txt", ios::out);
	temp.open("temp.txt", ios::in);
	while (!temp.eof())
	{
		temp.getline(ID, 25, '|');
		temp.getline(name, 25, '|');
		temp.getline(phone, 25, '|');
		temp.getline(age, 25, '|');
		temp.getline(year, 25, '|');
		temp.getline(specialty, 25, '|');
		temp.getline(Account, 25, '|');
		temp.getline(Reduction, 25, '|');
		temp.getline(total, 25);
		stud << ID << '|' << name << '|' << phone << '|' << age << '|' << year << '|' << specialty << '|' << Account << '|' << Reduction << '|' << total << '\n';
	}
	temp.close();
	stud.close();
	remove("temp.txt");
	system("cls");
	cout << "\n donete dele !!!!!!!!!!!!!!!!!\n";
	studen();
}
void delet_t()//this the 5th option in teacher function and it delete  any information teacher you want in fail by phone
{
	fstream stud;
	fstream temp;
	stud.open("TTT.txt", ios::in);
	temp.open("temp.txt", ios::out);
	char ID[25];
	char name[25];
	char age[25];
	char phone[25];
	char year[25];
	char specialty[25];
	char Account[25];
	char a[25];
	cin.ignore();
	cout << "\n\tenter the phone number to update recored : ";
	cin.getline(a, 25);
	while (!stud.eof())
	{
		stud.getline(ID, 25, '|');
		stud.getline(name, 25, '|');
		stud.getline(phone, 25, '|');
		stud.getline(age, 25, '|');
		stud.getline(year, 25, '|');
		stud.getline(specialty, 25, '|');
		stud.getline(Account, 25);
		if (strcmp(phone, a) == 0)
		{
			continue;
		}
		else
		{
			temp << ID << '|' << name << '|' << phone << '|' << age << '|' << year << '|' << specialty << '|' << Account << '\n';
		}
	}
	temp.close();
	stud.close();
	stud.open("TTT.txt", ios::out);
	temp.open("temp.txt", ios::in);
	while (!temp.eof())
	{
		temp.getline(ID, 25, '|');
		temp.getline(name, 25, '|');
		temp.getline(phone, 25, '|');
		temp.getline(age, 25, '|');
		temp.getline(year, 25, '|');
		temp.getline(specialty, 25, '|');
		temp.getline(Account, 25);
		stud << ID << '|' << name << '|' << phone << '|' << age << '|' << year << '|' << specialty << '|' << Account << '\n';
	}
	temp.close();
	stud.close();
	remove("temp.txt");
	system("cls");
	cout << "\n done the Update !!!!!!!!!!!!!!!!!\n";
	Teacher();
}
