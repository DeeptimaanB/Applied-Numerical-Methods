clc;
clear;
close all;

syms f(x);
f(x)=input('Enter Integration function : '); 
u=input('Enter Upper Limit : ');
l=input('Enter Lower Limit : ');
n=input('Enter n : ');
xx=[];
yy=[];
h=(u-l)/n;

while l <= u
    xx=[xx,l];
    yy=[yy,f(l)];
    l=l+h;
end
fprintf("X");
disp(xx);
fprintf("Y");
disp(yy);
i=1;
sol=0;
while i<=length(yy)
    if ((i==1) || (i==length(yy)))
        sol=sol+yy(i);
        i=i+1;
        continue;
    end
    sol=sol+(2*yy(i));
    i=i+1;
end
sol=(h/2)*sol;
fprintf("Solution : ");
disp(sol);