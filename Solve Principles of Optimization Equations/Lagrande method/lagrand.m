clc
clear
X=input('Enter list of  abscissas');
Y=input('Enter list of  ordinates');
n=length(X);
L=zeros(n,n);
for i=1:n
   V=1;
   for j=1:n
       if i~=j
           V= conv(V,poly(X(j)))/(X(i)-X(j));
       end
   end
   L(i,:)=V*Y(i);
end
P=sum(L);
F=fliplr(P);
for K=n:-1:2
    fprintf('+(%.2fx^%d)',F(K),K-1)
end
fprintf('+(%.2f)',F(1))

x=linspace(X(1),X(n),100);
y=polyval(P,x);
plot(x,y,'r')
hold on
plot(X,Y,'o')