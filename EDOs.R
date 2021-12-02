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
  N <- x[3] # nutriment resources, dN = -v_S * S - v_T *T ; v_S = N * beta1 ; N/(N+K_N) * beta1 ; v_C = N * beta2
  
  dSdt <- -mu*S - gamma*S + beta1*(1-(N/(N+K)))*S #beta1 * (N/(N+K))
  dCdt <- mu*S - delta*C + beta2*(1-(N/(N+K)))*C - tau*C
  dNdt <- - beta1* (N/(N+K))*S - beta2*(N/(N+K))*C
    
  list(c(dSdt, dCdt, dNdt))
}

mu <- 0.001
beta1 <- 0.001
beta2 <- 0.002
gamma <- 0.001
delta <- 0.0015
tau <- 0.0001
K<- 10e4

S0 <- 1900
C0 <- 100
N0 <- 10e6


param = c(mu, beta1, beta2, gamma, delta, tau, K)
init = c(S0,C0,N0)
times <- seq(0, 1000, by=0.001)

out <- ode(y = init, times = times, func = SCN, parms = param)

S = out[,"1"]
C = out[,"2"]
N = out[,"3"]
t = out[,"time"]

par(mfrow=c(2,2))
plot(t,S, type = "l")
plot(t,C, type = "l")
plot(t,N, type = "l")
