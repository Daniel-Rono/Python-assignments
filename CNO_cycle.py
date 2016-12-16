# Daniel Rono.
# Astrophysics II.
# CNO Coding.

import math

print ("Welcome to the CNO cycle!")

c = 3*(10**8) # the speed of light in vacuo, in metres per second.

L_sol = 3.839*10**26 # solar luminosity in Watts

M_sol = 1.9891*10**30 # solar mass in kg

He4 = 4.00260325413 # mass of Helium-4 in AMU

H = 1.00782503223 # mass of Hydrogen-1 in AMU

C12 = 12 # the following twelve lines are isotope masses in AMU and lifetimes in seconds.

t_C12 = 1 # this is a stable isotope

N13 = 13.005738609

t_N13 = (5.98*10**2)/math.log1p(2) # mean lifetime in seconds, calculated as the halflife divided by ln(2)

C13 = 13.00335483507

t_C13 = 1

N14 = 14.00307400443

t_N14 = 1

O15 = 15.003065618

t_O15 = (1.22*10**2)/math.log1p(2)

N15 = 15.00010889888

t_N15 = 1

def cno():

    E = 0 # setting initial energy generated at zero.

    X = float (input("Please enter the mass fraction of hydrogen in the sun as a number between 0 and 1 : ")) # Allows the user to enter the mass fraction of hydrogen in the sun.

    dC12 = (N15/t_N15) + H - (N13/t_N13) # the following six lines calculate the rate at which various isotopes in the CNO cycle are generated.

    dN13 = (C12/t_C12) + H - (C13/t_C13)

    dC13 = (N13/t_N13) - (N14/t_N14)

    dN14 = (C13/t_C13) + H - (O15/t_O15)

    dO15 = (N14/t_N14) + H - (N15/t_N15)

    dN15 = (O15/t_O15) - (C12/t_C12) - He4

    E = (X*(((4*H)-He4)*(1.6605*(10**-27)))*M_sol)*(c**2) # calculates the energy generated in the CNO cycle.

    print ("The total energy in Joules generated by the CNO cycle in the sun is ",E)

    print ("The rate of generation of Carbon-12 in the CNO cycle is ",dC12)

    print ("The rate of generation of Nitrogen-13 in the CNO cycle is ",dN13)

    print ("The rate of generation of Carbon-13 in the CNO cycle is ",dC13)

    print ("The rate of generation of Nitrogen-14 in the CNO cycle is ",dN14)

    print ("The rate of generation of Oxygen-15 in the CNO cycle is ",dO15)

    print ("The rate of generation of Nitrogen-15 in the CNO cycle is ",dN15)

cno()

#References:

# https://www-nds.iaea.org/
