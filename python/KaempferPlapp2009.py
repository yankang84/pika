#!/usr/bin/python
'''
***************************************
* Calculator for Phase Field Modeling *
* of Dry Snow Metamorphosis           *
* (Kaempfer 2009)                     *
*                                     *
* Execute:                            *
* ./KaempferPlapp2009.py              *
*                                     *
***************************************

NOMENCLATURE:

R_da = gas constant for dry air [J/(kg K)]
R_v = gas constant for water vapor [J/(kg K)]

P_a = atmospheric pressure [Pa]
P_vs = saturated vapor pressure over ice [Pa]

K_fit = fitting coefficients
T = Temperature [K]
X_s = humidity ratio [kg/kg]

'''

# Load SymPy and enable latex printing
from sympy import *
init_printing()

# Define symbolic variables
T = symbols('T')

# Define constants
R_da = 286.9
R_v = 461.5
P_a = 1.01325e5
rho_a = 1.341
rho_i = 918.9
K_fit = [-0.58653696e4, 0.2224103300e2, 0.13749042e-1, -0.34031775e-4, 0.26967687e-7, 0.6918651]
gamma = 1.09e-1
a = 3.19e-10
k = 1.38e-23
a_1 = (5./8.)*sqrt(2.)
W = 1.e-6
alpha = 10.e-2
m = 2.99e-26

# Eq. (2)
P_vs = exp(K_fit[0]*T**(-1) + K_fit[1]*T**0 + K_fit[2]*T**1 + K_fit[3]*T**2 + K_fit[4]*T**3 + K_fit[5]*log(T))

# Eq. (1)
x_s = (R_da / R_v) * P_vs / (P_a - P_vs)

# Eq. (3)
rho_vs = rho_a * x_s

# d0, d0' Eq. (25)
d_0 = gamma * a**3 / (k * T)
d_0_prime = (rho_vs/rho_i) * d_0

# Make fixed version for testing user prescribed d0
d_0_fixed = 1.3e-9
d_0_prime_fixed = (rho_vs/rho_i) * d_0_fixed

# Lambda Eq. (37)
lbda = a_1 * W / d_0_prime
lbda_fixed = a_1 * W / d_0_prime_fixed

# beta0, beta0' Eq. (26)
beta_0 = 1/alpha * sqrt(2*pi*m /(k * T))
beta_0_prime = (rho_vs/rho_i) * beta_0

# Make fixed version for testing user prescribed d0
beta_0_fixed = 5.5e5
beta_0_prime_fixed = (rho_vs/rho_i) * beta_0_fixed

# Tau Eq. (38)
tau = beta_0_prime * W * lbda / a_1
tau_fixed = beta_0_prime_fixed * W * lbda / a_1

# Concentration equilibrium
u_eq = (rho_vs - rho_vs.subs(T, 263.15)) / rho_i


print "P_vs(263.15) = ", P_vs.evalf(subs={T: 263.15})
print "P_vs(268.15) = ", P_vs.evalf(subs={T: 268.15})
print ""
print "x_s(263.15) = ", x_s.evalf(subs={T: 263.15})
print "x_s(268.15) = ", x_s.evalf(subs={T: 268.15})
print ""
print "rho_vs(263.15) = ", rho_vs.evalf(subs={T: 263.15})
print "rho_vs(268.15) = ", rho_vs.evalf(subs={T: 268.15})
print ""
print "u_eq(263.15) = ", u_eq.evalf(subs={T: 263.15})
print "u_eq(268.15) = ", u_eq.evalf(subs={T: 268.15})
print ""
print "d0(263.15) = ", d_0.evalf(subs={T: 263.15})
print "d0(268.15) = ", d_0.evalf(subs={T: 268.15})
print ""
print "d0'(263.15) = ", d_0_prime.evalf(subs={T: 263.15})
print "d0'(268.15) = ", d_0_prime.evalf(subs={T: 268.15})
print ""
print "lambda(263.15) = ", lbda.evalf(subs={T: 263.15})
print "lambda(268.15) = ", lbda.evalf(subs={T: 268.15})
print ""
print "d0_fixed(263.15) = ", d_0_fixed
print "d0_fixed(268.15) = ", d_0_fixed
print ""
print "d0_fixed'(263.15) = ", d_0_prime_fixed.evalf(subs={T: 263.15})
print "d0_fixed'(268.15) = ", d_0_prime_fixed.evalf(subs={T: 268.15})
print ""
print "lambda_fixed(263.15) = ", lbda_fixed.evalf(subs={T: 263.15})
print "lambda_fixed(268.15) = ", lbda_fixed.evalf(subs={T: 268.15})
print ""
print "beta0(263.15) = ", beta_0.evalf(subs={T: 263.15})
print "beta0(268.15) = ", beta_0.evalf(subs={T: 268.15})
print ""
print "beta0'(263.15) = ", beta_0_prime.evalf(subs={T: 263.15})
print "beta0'(268.15) = ", beta_0_prime.evalf(subs={T: 268.15})
print ""
print "tau(263.15) = ", tau.evalf(subs={T: 263.15})
print "tau(268.15) = ", tau.evalf(subs={T: 268.15})
print ""
print "beta0_fixed(263.15) = ", beta_0_fixed
print "beta0_fixed(268.15) = ", beta_0_fixed
print ""
print "beta0_fixed'(263.15) = ", beta_0_prime_fixed.evalf(subs={T: 263.15})
print "beta0_fixed'(268.15) = ", beta_0_prime_fixed.evalf(subs={T: 268.15})
print ""
print "tau_fixed(263.15) = ", tau_fixed.evalf(subs={T: 263.15})
print "tau_fixed(268.15) = ", tau_fixed.evalf(subs={T: 268.15})
print ""
