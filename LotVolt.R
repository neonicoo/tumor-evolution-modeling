library(deSolve)
rm(list = ls())

Lotka.Volterra <- function(t, state, parameters)
{
  with(as.list(c(state, parameters)), {
    dX <- X * (alpha - beta * Y)
    dY <- Y * (delta * beta * X - gamma)
    list(c(dX, dY))
  })
}
  
### Lotka-volterra Model ##

alpha <- 1.1
beta <- 0.2
gamma <- 0.2
delta <- 0.6

params = c(alpha, beta, gamma, delta)

init = c(X = 10, Y = 2)
time <- seq(0, 100, by=0.1)

out <- as.data.frame(ode(y = init, times = time, func = Lotka.Volterra, parms = params))

S <- out$X
C <- out$Y

plot(time, S, type = "l", las=1, col = "blue", ylim = c(0, max(S, C)))
lines(time, C, type = "l", col="red")

legend("topright", legend=c("Normal cells", "Cancerous cells"),
       col=c("blue", "red"), lty = 1)

