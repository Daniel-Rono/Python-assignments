# Daniel Rono.
# Astrophysics II.
#HW 5: Jupiter Coding Project.

import math

M0 = 2*10**30      # final mass in kg

r1 = float (input("Please enter the smallest radius in metres at which you wish to begin the mass iteration: ")) # Allows the user to enter the radius at which iterations of r begin

dr = 1000          # incremental radius in m

P0 = 3*10**12      # central pressure in Pa

T0 = 92000         # central temperature in K

mH = 1.67*10**-27  # mass of hydrogen in kg

mu = 1             # because we are assuming that the gas is comprised of hydrogen atoms

gamma = 0.6

G = 6.67*10**-11   # gravitational constant in N*m**2/kg**2

k = 1.38*10**-23   # Boltzmann's constant in J/K

rho = (P0*mu*mH)/(T0*k) # density at the centre of the planet, calculated from the ideal gas law

def mass():
    
    dM = 0    # setting initial shell mass in kg to zero
    
    dP = P0   # setting initial pressure to be the central pressure in the planet's core
    
    dT = T0   # setting initial temperature to be the central temperature in the planet's core
    
    r=r1      # setting the initial radius to be the one entered globally by the user

    rho1 = rho # setting the initial density equal to that at the centre of the planet.
    
    while dM<=M0:                            # while-loop iterates until the mass is >= M0
        
        print ("r equals ",r)
        
        dM += 4*math.pi*(r**2)*rho1*dr       # calculates the mass of the planet as shells of mass dM are added
        
        print ("Mass M equals ",dM)

        rho1 = dM/((4/3)*math.pi*(r+dr)**3)  # calculates the density as the mass and volume of the planet increase with increasing radius

        print ("rho equals ",rho1)
        
        dP += (-1*G*dM*rho1*dr)/(r**2)       # calculates the pressure as r increases       
        
        print ("Pressure P equals ",dP)
        
        dT += -((mu*mH)/k)*((G*dM)/r**2)*(1-(1/gamma))     # calculates the temperature given dP at a given radius r

        print ("Temperature T equals ",dT)
        
        r += dr                              # incrementally increases the radius by dr so that the loop iterates over radius r

mass()
