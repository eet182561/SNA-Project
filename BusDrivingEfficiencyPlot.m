x = 0:0.001:1;
W = 0:1/100:10;
plot(x,W,'ro');
title('Relation between Bus Driving Efficiency and Passenger Flow')
xlabel('Passenger Flow');
ylabel('Bus Driving Efficiency');

for i = 1:length(x)
    W1(i) = 10*x(i)/(1+(x(i)/1)^10);
end
hold on, plot(x,W1,'bo'); legend('Bus Driving Efficiency','Improved Bus Driving Efficiency','Location','northwest');
