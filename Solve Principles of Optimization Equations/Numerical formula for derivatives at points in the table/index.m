g = input('Enter your function e.g @(x) sin(x): ','s');
f = str2func(g) ;
h = input('Enter step size: ');
d = input('Which derivative you want to compute: ');
x = input('At which point you want to approximate derivative: ');
if d==1
    Fd2 = (f(x+h)-f(x))/h; %forward 2-point
    Bd2 = (f(x)-f(x-h))/h; %backward 2-point
    Cd2 = (f(x+h)-f(x-h))/(2*h); %central 2-point
    Fd3 = (4*f(x+h)-f(x+2*h) -3*f(x))/(2*h); %forward 3-point
    Bd3 = (-4*f(x-h)+f(x-2*h)+3*f(x))/(2*h); %Backward 3-point
    disp('Results using 2-point formulas\n')
    fprintf('Forward: %.4f\n',Fd2)
    fprintf('Backward: %.4f\n',Bd2)
    fprintf('Central: %.4f\n',Cd2)
    disp('Results using 3-point formulas\n')
    fprintf('Forward: %.4f\n',Fd3 )
    fprintf (' Backward: %.4f\n',Bd3)
elseif d ==2
    Fd3 = (f(x+2*h) -2*f(x+h) +f(x))/(h*2); %forward 3-point
    Bd3 = (f(x-2*h) -2*f(x-h) +f(x))/(h*2); %Backward 3-point
    Ca3 = (f(x+h) - 2*f(x) + f(x-h))/(h*2);% Scentral 3-point
    disp('Results using 3-point formulas')
    fprintf(' Forward: %.4f\n',Fd3)
    fprintf('Backward: %.4f\n',Bd3)
    fprintf('Central: %.4f\n',Ca3)
else
    disp('**Formula not available**');

end