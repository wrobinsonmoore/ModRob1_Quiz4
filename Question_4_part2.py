import sympy as sp
import numpy as np

# Define symbolic variables
w11, w12, w13, w21, w22, w23, t1, t2 = sp.symbols('w11 w12 w13 w21 w22 w23 t1 t2')

# Matrices
t1_matrix = sp.Matrix([[sp.cos(t1) + sp.Pow(w11, 2)*(1-sp.cos(t1)), w11*w12*(1-sp.cos(t1))-w13*sp.sin(t1), w11*w13*(1-sp.cos(t1)) + w12*sp.sin(t1)], 
                       [w11*w12*(1-sp.cos(t1)) + w13*sp.sin(t1), sp.cos(t1) + sp.Pow(w12, 2)*(1-sp.cos(t1)), w12*w13*(1-sp.cos(t1)) - w11*sp.sin(t1)], 
                       [w11*w13*(1-sp.cos(t1)) - w12*sp.sin(t1), w12*w13*(1-sp.cos(t1)) + w11*sp.sin(t1), sp.cos(t1) + sp.Pow(w13, 2)*(1-sp.cos(t1))]])

t2_matrix = sp.Matrix([[sp.cos(t2) + sp.Pow(w21, 2)*(1-sp.cos(t2)), w21*w22*(1-sp.cos(t2))-w23*sp.sin(t2), w21*w23*(1-sp.cos(t2)) + w22*sp.sin(t2)], 
                       [w21*w22*(1-sp.cos(t2)) + w23*sp.sin(t2), sp.cos(t2) + sp.Pow(w22, 2)*(1-sp.cos(t2)), w22*w23*(1-sp.cos(t2)) - w21*sp.sin(t2)], 
                       [w21*w23*(1-sp.cos(t2)) - w22*sp.sin(t2), w22*w23*(1-sp.cos(t2)) + w21*sp.sin(t2), sp.cos(t2) + sp.Pow(w23, 2)*(1-sp.cos(t2))]])

# Symbolic representation of final matrix. It's gigantic
symb_multi = t1_matrix @ t2_matrix @ sp.eye(3)

# Define your omegas (w's)
w11_value = 0
w12_value = 0
w13_value = 1
w21_value = 0
w22_value = 1/np.sqrt(2)
w23_value = -1/np.sqrt(2)

# Let's simplify this matrix by substituting these known values in it
symb_multi_sub = symb_multi.subs([(w11, w11_value), (w12, w12_value), (w13, w13_value), (w21, w21_value), (w22, w22_value), (w23, w23_value)])
symb_multi_simp = sp.simplify(symb_multi_sub)

# Print it out
print(f"The final result is:\n")
sp.pprint(symb_multi_simp)