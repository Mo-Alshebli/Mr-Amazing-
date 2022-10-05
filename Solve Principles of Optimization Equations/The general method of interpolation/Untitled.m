clear
clc
syms x ;
fun=input('Enter The Function : ','s');
X=input('Enter the value of X : ');
Y=input('Enter the value of Y : ');
[s,w]=size(X);
x=0;
for i =1:w
   x=X(:,i);
   subs(fun)
   x=input('Enter the varibal of equation : ');
   c(i,:)=x;
end
o=det(c);
y=c;
[m,b]=size(c);
for i=1:m
    y(:,i)=Y;
    de=det(y);
    XX(:,i)=[de/o];
    y=c;
end
disp('X =');
disp(XX);