close all   % close all open such as : figures, fuctions, etc
clc         % clear the command prompt
clear all   % clear all variables


% Loading Real Data 
load ('Data_Condor_BioLinux')
M = length(Data_Condor_BioLinux(:,1));       

for j = 1 : 3   U(:,j) =  Data_Condor_BioLinux(:,j); end

figure(1)
subplot(2,1,1)
plot(U(:,1), U(:,2),'-*r')   
axis equal tight
grid on
xlabel('Data size')
ylabel('Time')
title('Condor performance')   

subplot(2,1,2)
plot(U(:,1), U(:,3),'-*b')  
grid on
xlabel('Data size')
ylabel('Time')
title('Condor performance')

pause() 
% SAVE PLOTS:  saveas (1,"test.eps")  or print (1,"test.eps") or print -deps test.eps
%saveas (2,"test1.eps")
%print (2,"test2.eps")
%print('figure.eps','-deps')
print -deps -color OUTPU.eps
