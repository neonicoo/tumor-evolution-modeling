library(deSolve) # importation de la librarie diferential equation Solve 
#library(phaseR)

rm(list = ls()) # Ré-initialisation de toutes les variables

SCN <- function(t, x, parameters1)
{
  mu <- parameters1[1]  # mutation rate for a normal cell to become cancerous
  beta1 <- parameters1[2] # reproduction for normal cells
  beta2 <- parameters1[3] # reproduction for cancer cells
  gamma <- parameters1[4] # apoptosis for normal cells
  delta <- parameters1[5] # apoptosis for cancer cells
  tau <- parameters1[6] # treatment effect
  K <- parameters1[7] # nutriment threshold
  
  S <- x[1] # susceptible cells
  C <- x[2] # cancerous cells
  N <- x[3] # nutriment resources
  
  dSdt <- -mu*S - gamma*S + beta1*(N/(N+K))*S
  dCdt <- mu*S - delta*C + beta2*(N/(N+K))*C - tau*C
  dNdt <- - beta1* (N/(N+K))*S - beta2*(N/(N+K))*C
    
  return(list(c(dSdt, dCdt, dNdt)))
}

Lotka.Volterra <- function(t, x, parameters2)
{
  alpha <- parameters2[1]
  beta <- parameters2[2]
  gamma <- parameters2[3]
  delta <- parameters2[4]
  
  S <- x[1]
  C <- x[2]
  
  dSdt <- S*(alpha - beta*S)
  dCdt <- C*(delta*S - gamma)
  
  return(list(c(dSdt, dCdt)))
}
  
####### Model SCN #######

mu <- 0.005
beta1 <- 0.001
beta2 <- 0.002
gamma <- 0.0005
delta <- 0.001
tau <- 0.001
K<- 1e2

S0 <- 2000
C0 <- 200
N0 <- S0

param1 = c(mu, beta1, beta2, gamma, delta, tau, K)
init = c(S0,C0,N0)
times <- seq(0, 1000, by=0.001)

out <- ode(y = init, times = times, func = SCN, parms = param1)

S = out[,"1"]
C = out[,"2"]
N = out[,"3"]
t = out[,"time"]

plot(t,S, type = "l", las=1, col = "blue", ylim = c(0, max(S, C)))
lines(t, C, type = "l", col="red")

legend("topright", legend=c("S cells", "C cells"),
       col=c("blue", "red"), lty = 1)

###########################
### Lotka-volterra Model ##

alpha <- 2
beta <- 0.5
gamma <- 0.2
delta <- 0.6

S0 <- 10
C0 <- 10

param2 = c(alpha, beta, gamma, delta)
init2 = c(S0, C0)
times2 <- seq(0, 100, by=1)


out2 <- ode(y = init2, times = times2, func = Lotka.Volterra, parms = param2)

S <- out2[,"1"]
C <- out2[,"2"]
t2 <- out2[,"time"]

plot(t2,S, type = "l", las=1, col = "blue")
lines(t2,C, type = "l", col="red")

legend("topright", legend=c("Normal cells", "Cancerous cells"),
       col=c("blue", "red"), lty = 1)

