from scipy.optimize import newton

from mach_area import area_ratio

def residual(MN, ar_target): 
    return ar_target - area_ratio(MN)

# return the supersonic solution
def super_mn_from_ar(ar_target): 
    return newton(residual, 2.0, args=(ar_target,), maxiter=150)

# return the subsonic solution
def sub_mn_from_ar(ar_target): 
    return newton(residual, 0.01, args=(ar_target,), maxiter=150)

if __name__ == "__main__": 
    print('supersonic: ', super_mn_from_ar(3.))
    print('subsonic: ', sub_mn_from_ar(3.))







