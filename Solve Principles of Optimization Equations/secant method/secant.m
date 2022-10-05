fun=input('Enter The Function : ','s');
re=inline(fun);
rang=input('Enter the rang : ');
error=input(' Enter the error : ');
n=input('Enter the end of looping : ');
a=rang(1);
b=rang(2);
i=0;

while (i<=n)
    a0=re(a);
    b0=re(b);
    r=((a*b0)-(b*a0))/(b0-a0);
    
    disp(r);
    disp(r0);
    r0=re(r);
    
       if r0<0
           a=r;
       
       else
           b=r;
        end
       if ((abs(r0)<error)||(r0==0))
           d=r;
           disp(' the root is :');
           disp(d);
           break;
       end
       if(i==n)
           disp(i);
          disp('no root'); 
          break;
       end
   i=i+1;
    
end

