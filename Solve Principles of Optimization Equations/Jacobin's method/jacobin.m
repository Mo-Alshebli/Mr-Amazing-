clear all; clc;
syms x y   
f=x^2+y^2-1;
g=x*y;
%f=input('Enter the Function F(x,y) : ');
%g=input('Enter the Function g(x,y) : ');
arrfun=[f;g];
%x0=input('Enter the  X0 : ');
%y0=input('Enter the  Y0 : ');

x0=0.5;
y0=-0.1;
arrv=[x;y];
jac=jacobian(arrfun,arrv);
de=det(jac);
dee=inline(de);

for i=1:2
    disp('=================');
J=dee(x0,y0);
J
ff=inline(f);
gg=inline(g);
fx1=inline(jac(1,1));
fy1=inline(jac(1,2));
gx2=inline(jac(2,1));
gy2=inline(jac(2,2));
F=ff(x0,y0);
F
G=gg(x0,y0);
G
arrx=[F,fy1(y0);G,gy2(x0)];
arrx
arry=[fx1(x0),F;gx2(y0),G];
x1=x0-((1/J)*det(arrx));
y1=y0-((1/J)*det(arry));
x1
y1
x0=x1;
y0=y1;
end