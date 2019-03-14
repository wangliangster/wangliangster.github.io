import numpy as np
from scipy.stats import f
import matplotlib.pyplot as plt

x=np.arange(0,10,.001)
plt.plot(x,f.pdf(x,1,1), x,f.pdf(x,3,8), x,f.pdf(x,8,3), x,f.pdf(x, 40,40))

plt.xlim(0,10)
plt.ylim(0,1.5)

plt.xlabel('$x$',fontsize=20)
plt.ylabel('$P(X=x | K_1,K_2)$',fontsize=18)

plt.title('Fisher-Distribution',fontsize=20)
plt.legend(['$K_1=1, K_2=1$','$K_1=3, K_2=8$', '$K_1=8 ,K_2=3$', '$K_1=40, K_2=40$'])
plt.show()
