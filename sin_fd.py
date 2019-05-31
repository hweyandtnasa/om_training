import numpy as np 

import matplotlib.pylab as plt

def fd_sin(x, epsilon): 

    return (np.sin(x+epsilon) - np.sin(x))/epsilon

steps = np.logspace(-15, -3, base=10, num=50)
fd_derivs = fd_sin(np.pi/4, steps)
true_deriv = np.cos(np.pi/4)
rel_error_derivs = np.abs(fd_derivs-true_deriv)/true_deriv

fig, ax = plt.subplots()
ax.loglog(steps, rel_error_derivs)
ax.set_title('Relative error of the FD approximation')
ax.set_xlabel(r'log($\epsilon$)')
ax.set_ylabel(r'log(rel error)', rotation='horizontal', ha='right')

plt.savefig('sin_fd.pdf', bbox_inches='tight')

