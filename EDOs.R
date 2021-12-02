library(deSolve) # importation de la librarie diferential equation Solve 
#library(phaseR)

rm(list = ls()) # Ré-initialisation de toutes les variables

SCN <- function(t, x, parameters)
{
  mu <- parameters[1]  # mutation rate for a normal cell to become cancerous
  beta1 <- parameters[2] # reproduction for normal cells
  beta2 <- parameters[3] # reproduction for cancer cells
  gamma <- parameters[4] # apoptosis for normal cells
  delta <- parameters[5] # apoptosis for cancer cells
  tau <- parameters[6] # treatment effect
  K <- parameters[7] # nutriment threshold
  
  S <- x[1] # susceptible cells
  C <- x[2] # cancerous cells
  N <- x[3] # nutriment resources
  
  dSdt <- -mu*S - gamma*S + beta1*(N/(N+K))*S
  dCdt <- mu*S - delta*C + beta2*(N/(N+K))*C - tau*C
  dNdt <- - beta1* (N/(N+K))*S - beta2*(N/(N+K))*C
    
  list(c(dSdt, dCdt, dNdt))
}

mu <- 0.001
beta1 <- 0.001
beta2 <- 0.002
gamma <- 0.001
delta <- 0.0015
tau <- 0.0001
K<- 1e3/2

S0 <- 2000
C0 <- 200
N0 <- 1e3

param = c(mu, beta1, beta2, gamma, delta, tau, K)
init = c(S0,C0,N0)
times <- seq(0, 1000, by=0.001)

out <- ode(y = init, times = times, func = SCN, parms = param)

S = out[,"1"]
C = out[,"2"]
N = out[,"3"]
t = out[,"time"]

par(mfrow=c(1,1))
plot(t,S, type = "l", las=1, col = "blue", ylim = c(0, S0))
lines(t, C, type = "l", col="red")
lines(t, N, type = "l", col="green")

legend("topright", legend=c("S cells", "C cells", "nutrients"),
       col=c("blue", "red", "green"), lty = 1)
