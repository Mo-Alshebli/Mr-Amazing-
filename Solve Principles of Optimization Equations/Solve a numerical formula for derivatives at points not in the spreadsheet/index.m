clc
clear
format rational
X=input('Enter list of  abscissas :');
Y=input('Enter list of  ordinates :');
p0=input('Enter point of aproximation : ');
n=length(X);
h=X(2)-X(1);
alph=(p0-X(1))/h
alph
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
drif_num=input('Enter Which derivative you want  1 or 2 or 3');
if drif_num==1
drif_1=1/h*((F(1,2)*(alph-1/2)*F(1,3))+(1/6*(((3*alph^2)-(6*alph))+2)*F(1,4)));
drif_1
elseif drif_num==2
    drif_2=1/h^2*(F(1,3)+(alph-1)*F(1,4));
    drif_2
else
    drif_3=1/h^3*F(1,4);
    drif_3
    
end

