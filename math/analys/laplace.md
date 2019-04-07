## Laplace 变换

将[Fourier变换](math/analys/fourier.md)的频率$w$的数域由实数域$\Reals$扩展到复数域$\Complex$
， 就是**Laplace 变换**

在 Fourier变换的基础上
$$
\hat{f}(w)=F(w)=\int_{-\infty}^{+\infty}f(t)e^{-iwt}dt, \quad w \in (-\infty,+\infty)
$$

乘一个衰减函数
$$
L(w)=\int_{-\infty}^{+\infty}f(t)e^{-\delta t}e^{-iwt}dt \\ =\int_{-\infty}^{+\infty}f(t)e^{-(\delta+iw)t}dt\\= \int_{-\infty}^{+\infty}f(t)e^{-i(-\delta i+w)t}dt, \quad w \in (-\infty,+\infty),\quad \delta >0
$$

令
$$s=w-\delta i=a+bi$$

则有:
$$
L(s)=F(w,\delta)=\int_{-\infty}^{+\infty}f(t)e^{-ist}dt, \quad s \in \Complex
$$

注意此时$s$的**实部**对应于原实数域的频率$w$，虚部对应于衰减指数$-\delta$,如果搞反了多半是对$s$的定义不一致。

现在把$s$看成是广义上的“频率”，若把其虚部$\delta$当成一个连续量来看，它相当于表示组成基频的辐度随$\delta$也是变化的，应将带$\delta$的整体看成是一个基，不像原来$\sin x,\cos x$都是$1$，因为这样的基可以处理一些不可积的发散函数，所以它更厉害一点，当$b=0$时，也就是$\delta=0$不进行衰减，即复频$s$（没有旋转量）等于实频，就是**[Fourier变换](math/analys/fourier.md)**
