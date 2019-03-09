### PMF（probability mass function)
国际上，对**离散**形随机变量$X$的概率分布一般记为:
$$
X\sim P(X=x_i)
$$
简称**PMF**，国内很多书经常翻译为概率**"质量"**函数，简直就是误人子弟！ 它有如下性质
- $\forall x_i,\quad 0\leqq P(x_i)\leqq 1$
- $\sum_{x_i\in X}P(x_i)=1$

### PDF （probability desity function）
对于**连续**形随机变量$X$的概率分布一般用:
$$
p(x)
或者
f(x)
$$
表示,简称**PDF**, 它有如下性质
- $p(x)\geqq 0$ 
- $\int p(x)dx=1$

**注意**: 连续形随机变量并不要求$p(x)\leqq 1$，即意味$p(X=x)$并不是指$x$处的概率。

一般$\int_{a}^{b}p(x)dx$才是指随机变量$X$处于区间$[a,b]$的概率表示

## 期望
设$f(x)$为随机变量$X=x$处的一种表征值，$p(x)$为$X=x$的概率分布，则称它的**平均**表征值为**期望**,有如下表示:
$$
E(X)=\int p(x)f(x)dx
$$
## 方差
$$\sigma^2(X)=E[(X-E(X))^2]=\int p(x) [x-{\int p(t)f(t)dt}]^2dx$$
一般**标准差**用$\sigma$表示，**方差**用$\sigma^2$表示
## 协方差
它是两个随机变量$X$和$Y$的线性相关性的度量
$$
Cov(X,Y)=Cov(Y,X)=E((X-E(X))(Y-E(Y)))=\int p(x,y)(x-\int p(x)f(x)dx)(y-\int p(y)f(y)dy)dxdy
$$
**注意:** 两个相互独立的随机变量协方差一定为$0$，协方差为$0$的两个随机变量并不一定相互独立，协方差不为零的两个随机变量一定相关
