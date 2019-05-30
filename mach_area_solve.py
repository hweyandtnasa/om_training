from scipy.optimize import newton

from mach_area import area_ratio

def residual(MN, ar_target): 
    return ar_target - area_ratio(MN)

# solve for the MN that gives an area ratio of 3, with an initial guess of MN=0.1
solution = newton(residual, 0.1, args=(3.,), maxiter=150)
print('subsonic solution: ', solution)

# solve for the MN that gives an area ratio of 3, with an initial guess of MN=2.0

solution = newton(residual, 2.0, args=(3.,), maxiter=150)
print('supersonic solution: ', solution)




