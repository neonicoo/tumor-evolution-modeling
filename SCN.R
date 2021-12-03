library(deSolve)
rm(list = ls())

SCN <- function(t, state, parameters)
{
  with(as.list(c(state, parameters)), {
    dS <- -mu*S - gamma*S + beta1*(N/(N+K))*S
    dC <- mu*S - delta*C + beta2*(N/(N+K))*C - tau*C
    dN <- - beta1* (N/(N+K))*S - beta2*(N/(N+K))*C
    list(c(dS, dC, dN))
  })
}
  
####### Model SCN ####### 
params = c(mu = 0.002, beta1 = 0.001, beta2 = 0.002, gamma = 0.0005, delta = 0.001, tau = 0.001, K = 1e2)
init = c(S = 2000,C = 200 ,N = 1e4)
times <- seq(0, 2000, by=0.01)

out <- as.data.frame(ode(y = init, time = times, func = SCN, parms = params))

t = out$time
S = out$S
C = out$C
N = out$N

plot(t,S, type = "l", las=1, col = "blue", ylim = c(0, max(S, C)))
lines(t, C, type = "l", col="red")

legend("topright", legend=c("S cells", "C cells"),
       col=c("blue", "red"), lty = 1)

