%  clear
%  close all 
% % t = -3:0.00001:3;
% % % f = (6 - t.^2)./(2 + t.^2);
% % % plot(t,f)
% % % f2 = (6 - (0.5*t).^2)./(2 + (0.5*t).^2);
% % % plot(t,f,t,f2)
% % f = sin(1*t);
% % plot(t,f)
% % f2 = sin(2*t);
% % f3 = sin(0.5*t);
% % 
% % f4 = 5.* sin(t);
% % plot(t,f,t,f2,t,f3,t,f4)
% n = -3:1:3;
% x= abs(n);
% x2= abs(2*n);
% x3= abs(0.3*n);
% stem(n,x2,'LineWidth',3)
% hold on
% stem(n, x,'LineWidth',3)
% hold on
% stem(n, x3,'LineWidth',3)
close all
clear all
t = -3:0.0001:3;
y1 = sin(t);
y2 = sin(t + 1);
y3 = sin(t - 1);
plot(t,y1,t,y2,t,y3,'LineWidth',3)
legend('original', ' tau = -1 (Lead)', 'tau = +1 (Lag)')