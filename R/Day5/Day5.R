demo(graphics)

#Question 1
movie_vec <- c(sample(1:20,4))
genres <- c("Com","Act","Rom","SciFi")
colors1 <- c("Red","Green","Blue","Purple")
pie(movie_vec,genres,col=colors1,main = "Tonight's Premier",clockwise = T)

#Question 1_b


#Question 1_c
leg = legend("topleft",genres,fill=colors1)

#Question 2
barplot(movie_vec,xlab="Genres",ylab="People",names.arg = genres,col=colors1,main= "Tonight's Premier")


#Question 3
Products <- c("A","B","C")
sales <- matrix(sample(50:100,12,replace =T),nrow = 4)
barplot(sales,xlab="Products",ylab="sales",names.arg = Products,col=colors1,main= "Quarterly Sales")

#Question 4
mpg <- mtcars[1]
hist(mtcars$mpg,xlab="Cars",col=colors1)

#Question 5
plot.new()
plot.window(xlim=c(0,10),ylim=c(0,10))
axis(1)
axis(2)
declared_pointx <- c(3,6,5,7,8)
declared_pointy <- c(3,4,8,5,9)
final_points <- points(declared_pointx,declared_pointy,"b")
abline(h=max(declared_pointy))
abline(v=max(declared_pointx))

#Question 6
plot.new()
plot.window(xlim=c(10,60),ylim=c(10,60))
axis(1)
axis(2)
drugA <- c(16, 20, 27, 40, 60)
drugB <- c(15, 18, 25, 31, 40)
final_points <- points(drugA,drugB,"b")

#Question 7
boxplot(Temp~Month,data=airquality)
#?boxplot

#Question 8
iris
plot.new()
plot.window(xlim=c(10,60),ylim=c(10,60))
axis(1)
axis(2)

pairs(~Sepal.Length+Sepal.Width,data=iris)
