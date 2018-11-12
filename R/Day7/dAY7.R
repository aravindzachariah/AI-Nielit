a1=sample(1:6,3000,replace=TRUE)
a2=sample(30:70,27,replace=TRUE)
a3=sample(c('T','H'),1000,replace=TRUE)

n=rnorm(100,0,30)
pn=dnorm(n,0,30)
plot(n,pn)
cn=pnorm(n,0,30)
plot(n,cn)
pi=0.2
qi=qnorm(pi,0,30)
qi
q2=qnorm(0.5,0,30)
q2


n1=rnorm(100,0,15)
p1=dnorm(n1,0,15)
plot(n1,p1,xlim=c(0,100))

n2=rnorm(100,0,45)
p2=dnorm(n2,0,45)
plot(n2,p2,xlim=c(0,100))

n3=rnorm(100,50,30)
p3=dnorm(n3,50,30)
plot(n3,p3,xlim=c(0,100))

n4=rnorm(100,-50,30)
p4=dnorm(n4,-50,30)
plot(n4,p4,xlim=c(-100,100))

n5=rnorm(5000,20,5)
p5=dnorm(n5,20,5)
hist(p5)

vr=25
sd=vr^0.5
t1=1-pnorm(29,22,5)
t1
t2=pnorm(17,22,5)
t2
t3=pnorm(15,22,5)+(1-pnorm(25,22,5))
t3

mu=30
sigma=2
1/(sqrt(2*pi)*sigma)*exp(-((31 - mu)^2/(2*sigma^2)))
