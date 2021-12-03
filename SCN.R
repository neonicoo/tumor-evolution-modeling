library(deSolve)
rm(list = ls())

SCN <- function(t, state, parameters)
{
  with(as.list(c(state, parameters)), {
    dS <- S * (beta1 * N/(N+K) - mu - gamma)
    dC <- C * (beta2 * N/(N+K) - delta - tau) + mu * S
    dN <- - N/(N+K) * (beta1 * S + beta2 * C)
    list(c(dS, dC, dN))
  })
}
  
####### Model SCN ####### 
params = c(mu = 0.01, beta1 = 0.05, beta2 = 0.07, gamma = 0.02, delta = 0.025, tau = 0.01, K = 1e2)
init = c(S = 100, C = 25 , N = 1e3)
times <- seq(0, 200, by=0.1)

out <- as.data.frame(ode(y = init, time = times, func = SCN, parms = params))

t = out$time
S = out$S
C = out$C
N = out$N

plot(t,S, type = "l", las=1, col = "blue", ylim = c(0, max(S, C)))
lines(t, C, type = "l", col="red")
lines(t, N, type = "l", col="forestgreen")

legend("topright", legend=c("S cells", "C cells", "Nutrients"),
       col=c("blue", "red", "forestgreen"), lty = 1)

