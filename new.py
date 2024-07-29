import matplotlib.pyplot as plt
import numpy as np

# Event Characteristics
Energy = 3.5
e_str = f"{Energy:.1f} GeV"

proj = "p"
targ = "p"

# Column descriptions
t2 = "GiBUU total"
t3 = "{/Symbol r \256 }e^+e^-"
t4 = "{/Symbol w \256 }e^+e^-"
t5 = "{/Symbol f \256 }e^+e^-"
t6 = "{/Symbol w \256 p^0}e^+e^-"
t7 = "{/Symbol p^0 \256 }e^+e^-{/Symbol g}"
t8 = "{/Symbol h \256 }e^+e^-{/Symbol g}"
t9 = "{/Symbol D \256 }Ne^+e^-"
t10 = "{/Symbol h \256 }e^+e^-"
t14 = "pp Brems"

# Set default line styles
w = 4
ww = 6

# Function to sum over columns i to j
def colsum(data, i, j):
    return np.sum(data[:, i:j+1], axis=1)

# Load data from DileptonMass.dat (replace with actual data file)
data = np.loadtxt("DileptonMass.dat")

# Plot mass spectrum
plt.figure(figsize=(8, 6))
plt.title(f"{proj} + {targ} @ {e_str}")
plt.xlabel("dilepton mass $m_{{ee}}$ [GeV]")
plt.ylabel("d{/Symbol s}/dm_{ee} [{/Symbol m}b/GeV]")
plt.yscale("log")
plt.xlim(0, 1.1)
plt.ylim(5e-4, 5e1)

# Plot individual components
plt.plot(data[:, 0], data[:, 3] + data[:, 4] + data[:, 5] + data[:, 6] + data[:, 7] + data[:, 12] + colsum(data, 20, 38), label=t2)
plt.plot(data[:, 0], data[:, 3], label=t4)
plt.plot(data[:, 0], data[:, 4], label=t5)
plt.plot(data[:, 0], data[:, 5], label=t6)
plt.plot(data[:, 0], data[:, 6], label=t7)
plt.plot(data[:, 0], data[:, 7], label=t8)
plt.plot(data[:, 0], data[:, 8], label="{/Symbol D} QED")
plt.plot(data[:, 0], colsum(data, 20, 32), label="N* VMD")
plt.plot(data[:, 0], colsum(data, 33, 38), label="{/Symbol D}* VMD")
plt.plot(data[:, 0], data[:, 13], label=t14)

plt.legend()
#plt.savefig("pp35_mass.png")
plt.show()
