clc
clear
format rational
X=input('Enter list of  abscissas :');
Y=input('Enter list of  ordinates :');
p0=input('Enter point of aproximation : ');
n=length(X);
h=X(2)-X(1);
F=zeros(n,n);
F(:,1)=Y;
for j=2:n
    for i=1:n-j+1
    F(i,j)=F(i+1,j-1)-F(i,j-1);    
    end
end
C=F(1,n);
for k=n-1:-1:1
   p=poly(X(n))/h;
   p(2)=p(2)+(k-1);
   C=conv(C,p)/k;
   m=length(C);
   C(m)=C(m)+F(n-k+1,k);
    
end
C
A=polyval(C,p0);
A

B=fliplr(C);
x=linspace(X(1),X(n),100);
y=polyval(C,x);
plot(x,y,'r')
hold on
plot(X,Y,'o')

for C=n:-1:2
    fprintf('+(%.2fx^%d)',B(C),C-1)
end
fprintf('+(%.2f)',B(1))