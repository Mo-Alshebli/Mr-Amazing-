fun=input('Enter The Function : ','s');
f=inline(fun);
rang=input('Enter the rang : ');
error=input(' Enter the error : ');
n=input('Enter the end of looping');
a=rang(1);
b=rang(2);
i=0;
format long;
while (i<=n)
    a0=f(a);
    b0=f(b);
    r=(a+b)/2;
    r0=f(r);
    disp(r0);
       if sign(a0)==-1 && sign(r0)==-1
           a=r;
       end
        if (sign(a0)==1 && sign(r0)==-1)||(sign(a0)==-1 && sign(r0)==1)
           b=r;
        end
       if (abs(r0)<error)
           d=r;
           disp(' the root is :');
           disp(d);
           break;
       end
       if(i==n)
          disp('no root'); 
          break;
       end
   i=i+1;
    
end

