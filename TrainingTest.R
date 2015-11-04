## Used for presentation on the importance of splitting data
## into a training set, CV set, and test set for machine learning

require(ggplot2)

## generate some fake data
## simple linear relationship between x and y
N <- 50
x <- runif(N, 0, 100)
y <- x + rnorm(N, sd = 10)
ind <- order(x)
x <- x[ind]
y <- y[ind]
plot(x,y)

## now we can fit a few models

## y = beta0 + beta1*x
fit1 <- lm(y ~ x)
## y = beta0 + beta1*x + beta2*(x^2) + ... + beta10*(x^10)
fit10 <- lm(y ~ poly(x, degree = 10))
## y = beta0 + beta1*x + beta2*(x^2) + ... + beta10*(x^10) + ... + beta20*(x^20)
fit20 <- lm(y ~ poly(x, degree = 20))
prd <- data.frame(x = rep(x, 3),
                  y = rep(y, 3),
                  fit = c(fit1$fitted.values, fit10$fitted.values, fit20$fitted.values),
                  degree = factor(rep(c(1,10,20), each = N)))

g <- ggplot(prd, aes(x = x, y = y)) +
    theme_bw() +
    geom_point() +
    geom_line(aes(x = x, y = fit, colour = degree))
plot(g)

## calculate sum squared error
SSE <- function(y, yfit) return(sum((y - yfit)^2))
errs <- c(SSE(y, prd$fit[prd$degree == 1]),
          SSE(y, prd$fit[prd$degree == 10]),
          SSE(y, prd$fit[prd$degree == 20]))
names(errs) <- c('linear', 'degree 10', 'degree 20')

## How does it do with new data?
newx <- runif(N, 0, 100)
newy <- newx + rnorm(N, sd = 10)
ind <- order(newx)
newx <- newx[ind]
newy <- newy[ind]
newxdf <- data.frame(newx = newx)

prd$newx <- rep(newx, 3)
prd$newy <- rep(newy, 3)
prd$newfit <- c(predict(fit1, newxdf),
                predict(fit10, newxdf),
                predict(fit20, newxdf))
newg <- ggplot(prd, aes(x = newx, y = newy)) +
    theme_bw() +
    geom_point() +
    geom_line(aes(x = x, y = newfit, colour = degree))
dev.new()
plot(newg)

errs <- rbind(errs,
              c(SSE(newy, prd$newfit[prd$degree == 1]),
                SSE(newy, prd$newfit[prd$degree == 10]),
                SSE(newy, prd$newfit[prd$degree == 20])))

## but now we've done model fitting with this new data set!
## We're fitting 'd', the degree of the polynomial.
## that's fine! We call this second dataset the cross validation set.
## But to really have a sense of how accurate your model is,
## don't report the CV error. Compare it to a new set of data, your test set.

## Moral of the story: Any time you're fitting a model, test it on new data!
