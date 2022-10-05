clear all
clc
syms x;
fun=input('Enter The Function : ','s');
f=inline(fun);
rang=input('Enter the rang : ');
error=input(' Enter the error : ');
n=input('Enter the end of looping : ');
a=rang(1);
b=rang(2);
x0=(a+b)/2;
f_diff=diff(f(x));
ff=inline(f_diff);
disp(f_diff);
i =0;
while(i<n)
    R=f(x0);
    R_diff=ff(x0);
  x1=x0-R/R_diff;
  i
  y=f(x1);
   y
   if (abs(y<=error))
       disp("THe root is : ")
       x1
       break
   else
       x0=x1;
   end
       
 
    i=i+1;
    
end