import glob
import matplotlib.pyplot as plt
import numpy as np
import string


filenames = ["logs/p_0", "logs/p_1", "logs/Ux_0", "logs/Uy_0", "logs/Uz_0", "logs/k_0", "logs/epsilon_0"]

for f in filenames:
    #print(f)
    data = np.loadtxt(f)

    plt.plot(data[:,0],data[:,1])

plt.axhline(y=1.0e-05, color="black", linestyle='--')

#Array for legend names
leg_n = []

#Iterate through filenames, changing strings.
for string in filenames:
    new_string = string.replace("logs/", "")
    leg_n.append(new_string)

plt.title("Residual vs. Iteration")
plt.xlabel("Iteration")
plt.ylabel("Log Residual")
plt.yscale("log")
plt.xlim(0, len(data))

plt.legend(leg_n)
plt.savefig('figure.png')
plt.show()