clear
clc
n=input('Enter how many Equation you want : ');
output=input(' enter the output of all equation : ');
o=det(n);
y=n;
[m,c]=size(n);
for i=1:m
    y(:,i)=output;
    de=det(y);
    X(:,i)=[de/o];
    y=n;
end
disp('X =');
disp(X);