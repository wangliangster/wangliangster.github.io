#!/usr/bin/env python
import numpy as np
from scipy.stats import beta
from matplotlib import pyplot as plt

alpha_values = [1/3,2/3,1,1,2,2,4,10,20]
beta_values = [1,2/3,3,1,1,6,4,30,20]
colors =  ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 
           'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive']
x = np.linspace(0, 1, 1002)[1:-1]

fig, ax = plt.subplots(figsize=(14,9))

for a, b, c in zip(alpha_values, beta_values, colors):
    dist = beta(a, b)
    plt.plot(x, dist.pdf(x), c=c,label=r'$p=%.1f,\ q=%.1f$' % (a, b))

plt.xlim(0, 1)
plt.ylim(0, 6)

plt.xlabel(r'$\chi$', fontsize=20)
plt.ylabel(r'$P(\chi|p,q)$',fontsize=20)
plt.title('Beta distribution', fontsize=22)

ax.annotate('Beta(1/3,1)', xy=(0.014, 5), xytext=(0.04, 5.2),
            arrowprops=dict(facecolor='black', arrowstyle='-'))
ax.annotate('Beta(10,30)', xy=(0.276, 5), xytext=(0.3, 5.4),
            arrowprops=dict(facecolor='black', arrowstyle='-'))
ax.annotate('Beta(20,20)', xy=(0.5, 5), xytext=(0.52, 5.4),
            arrowprops=dict(facecolor='black', arrowstyle='-'))
ax.annotate('Beta(1,3)', xy=(0.06, 2.6), xytext=(0.07, 3.1),
            arrowprops=dict(facecolor='black', arrowstyle='-'))
ax.annotate('Beta(2,6)', xy=(0.256, 2.41), xytext=(0.2, 3.1),
            arrowprops=dict(facecolor='black', arrowstyle='-'))
ax.annotate('Beta(4,4)', xy=(0.53, 2.15), xytext=(0.45, 2.6),
            arrowprops=dict(facecolor='black', arrowstyle='-'))
ax.annotate('Beta(1,1)', xy=(0.8, 1), xytext=(0.7, 2),
            arrowprops=dict(facecolor='black', arrowstyle='-'))
ax.annotate('Beta(2,1)', xy=(0.9, 1.8), xytext=(0.75, 2.6),
            arrowprops=dict(facecolor='black', arrowstyle='-'))
ax.annotate('Beta(2/3,2/3)', xy=(0.99, 2.4), xytext=(0.86, 2.8),
            arrowprops=dict(facecolor='black', arrowstyle='-'))

plt.legend(loc=0)
plt.show()
