a=sample(1:20,4,replace=TRUE)
nm=c('Comedy', 'Action', 'Romance','Science/Fiction')
col=c("red","blue","green","violet")
pie(a,nm,col=rainbow(4),main='Movie Preference',clockwise=TRUE)

legend("topleft",nm,fill=col,cex=0.7)
box()

barplot(a,xlab="Movies",ylab="Preference",main="Movie Preference",names.arg=nm,col=col,border="blue")

p=c("A","B","C")
m=matrix(sample(1:20,12,replace=TRUE),nrow=4,ncol=3)
m
barplot(m,xlab="Product",ylab="Sales",main="ABC Company Sale",names.arg=p,col=col,border="blue")
hist(mtcars$mpg)

plot.new()
plot.window()
plot.window(xlim=c(0,10),ylim=c(0,10))
axis(1)
axis(2)
abline(h=0)
abline(v=0)
px=c(2,4,7,9)
py=c(1,3,8,9)
points(px,py,"b")
abline(h=max(py))
abline(v=min(px))