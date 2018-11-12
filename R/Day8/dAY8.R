p1=dbinom(5,50,0.8)
p1
p2=dbinom(5,50,0.05)
p2
p3=pbinom(6,50,0.8)
p3
p4=(1-pbinom(24,50,0.8))
p4
p5=pbinom(6,50,0.05)
p5

q1=dbinom(40,60,0.65)
q1
q2=pbinom(40,60,0.65)
q2

x=seq(0,30,1)
x

y=dbinom(x,31,0.15)
plot(x,y,type='b')
     
y1=dbinom(x,31,0.4)
plot(x,y1,type='b')

y2=dbinom(x,31,0.8)
plot(x,y2,type='b')

r1=dbinom(20,60,0.5)+dbinom(25,60,0.5)+dbinom(30,60,0.5)
r1
r2=pbinom(20,60,0.5)
r2
r3=pbinom(30,60,0.5)-pbinom(20,60,0.5)
r3

dpois(100,5)
dpois(100,25)
dpois(100,75)

s1=rpois(2608,10097)
hist(s1)

t1=ppois(5,7)
t1
t2=1-ppois(10,7)
t2
t3=ppois(16,7)-ppois(4,7)
t3

u1=punif(6,0,25)
u1