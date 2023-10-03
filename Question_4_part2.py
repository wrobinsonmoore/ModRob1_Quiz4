import numpy as np
from scipy.optimize import fsolve, root

# Define your r11...r33 from your desired matrix
r11 = 1/np.sqrt(2)
r12 = 0
r13 = -1/np.sqrt(2)
r21 = 0
r22 = 1
r23 = 0
r31 = 1/np.sqrt(2)
r32 = 0
r33 = 1/np.sqrt(2)

# Define your omegas (w's)
w11 = 0
w12 = 0
w13 = 1
w21 = 0
w22 = 1/np.sqrt(2)
w23 = -1/np.sqrt(2)

# Define your system of equations as functions
def equations(guess):
    # Extract x and y from the input array initial_guess
    t1 = guess[0]
    t2 = guess[1]

    # Define your system of equations
    eq1 = np.cos(t1)*np.cos(t2) + (-w13*np.sin(t1))*(w23*np.sin(t2)) - r11
    eq2 = np.cos(t1)*(-w23*np.sin(t2)) + (-w13*np.sin(t1))*(np.cos(t2)+np.power(w22, 2)*(1-np.cos(t2))) - r12
    eq3 = np.cos(t1)*(w22*np.sin(t2)) + (-w13*np.sin(t1))*(w22*w23*(1-np.cos(t2))) - r13
    eq4 = w13*np.sin(t1)*np.cos(t2) + np.cos(t1)*w23*np.sin(t2) - r21
    eq5 = w13*np.sin(t1)*(-w23*np.sin(t2)) + np.cos(t1)*(np.cos(t2) + np.power(w22, 2)*(1-np.cos(t2))) - r22
    eq6 = w13*np.sin(t1)*w22*np.sin(t2) + np.cos(t1)*(w22*w23*(1-np.cos(t2))) - r23
    eq7 = (np.cos(t1) + np.power(w13, 2)*(1-np.cos(t1)))*(-w22*np.sin(t2)) - r31
    eq8 = (np.cos(t1) + np.power(w13, 2)*(1-np.cos(t1)))*(w22*w23*(1-np.cos(t2))) - r32
    eq9 = (np.cos(t1) + np.power(w13, 2)*(1-np.cos(t1)))*(np.cos(t2)+np.power(w23, 2)*(1-np.cos(t2))) - r33

    
    # Return an array of your equations
    return [eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9]

# Initial guesses for (t1, t2)
initial_guess = np.array([0.0, 0.0])

# Use fsolve to find the solution
result = root(equations, initial_guess, method='lm')

print(f"\nYour angles in RADIANS are (t1, t2) are =\n{result.x}\n")
print(f"\nYour angles in DEGREES are (t1, t2) are =\n{(result.x)*180/np.pi}\n")
