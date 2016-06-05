using PyPlot

n = 50
srand(1)
x = rand(n)
y = rand(n)
area pi .* (15 .* rand(n)).^2 
scatter(x,y,s=area,alpha=0.5)