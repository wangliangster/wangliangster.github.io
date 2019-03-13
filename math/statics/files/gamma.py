import numpy as np
from scipy.stats import gamma
from matplotlib import pyplot as plt

alpha_values = [1, 2, 3, 3, 3]
beta_values = [0.5, 0.5, 0.5, 1, 2]
color = ['b','r','g','y','m']
x = np.linspace(1E-6, 10, 1000)

fig, ax = plt.subplots(figsize=(12, 8))

for k, t, c in zip(alpha_values, beta_values, color):
    dist = gamma(k, 0, t)
    plt.plot(x, dist.pdf(x), c=c, label=r'$\alpha=%.1f,\ \beta=%.1f$' % (k, t))

plt.xlim(0, 10)
plt.ylim(0, 2)

plt.xlabel('$X$',fontsize=20)
plt.ylabel(r'$\Gamma(x|\alpha,\beta)$',fontsize=20)
plt.title('Gamma Distribution',fontsize=22)

plt.legend(loc=0)
plt.show()
