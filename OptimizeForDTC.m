clc,clear all,close('all');

busroute1 = 1:10;
busroute2 = [11:14 5 15 16:20];
busroute3 = [21:24 4 25 16 26:28 8 29 30];

adjacencymatrix = zeros(30,30);

for i = 1:length(busroute1)
    for j = i:length(busroute1)
        if i ~= j
            if abs(find(busroute1 == busroute1(i)) - find(busroute1 == busroute1(j))) == 1
                adjacencymatrix(busroute1(i),busroute1(j)) = 10*rand(1);
                adjacencymatrix(busroute1(j),busroute1(i)) = 10*rand(1);
            end
        end
    end
end

for i = 1:length(busroute2)
    for j = i:length(busroute2)
        if i ~= j
            if abs(find(busroute2 == busroute2(i)) - find(busroute2 == busroute2(j))) == 1
                adjacencymatrix(busroute2(i),busroute2(j)) = 10*rand(1);
                adjacencymatrix(busroute2(j),busroute2(i)) = 10*rand(1);
            end
        end
    end
end


for i = 1:length(busroute3)
    for j = i:length(busroute3)
        if i ~= j
            if abs(find(busroute3 == busroute3(i)) - find(busroute3 == busroute3(j))) == 1
                adjacencymatrix(busroute3(i),busroute3(j)) = 10*rand(1);
                adjacencymatrix(busroute3(j),busroute3(i)) = 10*rand(1);
            end
        end
    end
end

SUM1 = sum(adjacencymatrix(:))
Efficency_init = sum(adjacencymatrix(:))/(29*30)

%% Now make this 13 delete
adjacencymatrix(12,14) = adjacencymatrix(12,13) + adjacencymatrix(13,14); % min(adjacencymatrix(12,13),adjacencymatrix(13,14));
adjacencymatrix(14,12) = adjacencymatrix(12,13) + adjacencymatrix(13,14); % min(adjacencymatrix(12,13),adjacencymatrix(13,14));
adjacencymatrix(12,13) = 0;
adjacencymatrix(13,12) = 0;
adjacencymatrix(13,14) = 0;
adjacencymatrix(14,13) = 0;
SUM2 = sum(adjacencymatrix(:))
Efficency13node = sum(adjacencymatrix(:))/(29*28)

%% Lets delete node 18
adjacencymatrix(17,19) = adjacencymatrix(19,18) + adjacencymatrix(18,17);
adjacencymatrix(19,17) = adjacencymatrix(19,18) + adjacencymatrix(18,17);
adjacencymatrix(19,18) = 0;
adjacencymatrix(18,19) = 0;
adjacencymatrix(18,17) = 0;
adjacencymatrix(17,18) = 0;
SUM3 = sum(adjacencymatrix(:))
Efficency18node = sum(adjacencymatrix(:))/(27*28)
