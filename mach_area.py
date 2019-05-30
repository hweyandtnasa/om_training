import numpy as np
import matplotlib.pylab as plt

gamma = 1.4

gp1 = gamma+1 
gm1 = gamma-1

def area_ratio(MN): 
    return (gp1/2)**(gp1/(2*gm1)) * (1 + gm1/2*MN**2)**(gp1/(2*gm1)) / MN 


if __name__ == "__main__":
    Machs = np.linspace(0.1, 3, 50)
    area_ratios = area_ratio(Machs)

    fig, ax = plt.subplots()
    ax.plot(Machs, area_ratios)
    ax.set_xlabel("Mach")
    ax.set_ylabel(r"$\frac{A}{A^*}$", rotation="horizontal", fontsize=15)
    fig.savefig("mach_area.pdf")

    plt.show()
