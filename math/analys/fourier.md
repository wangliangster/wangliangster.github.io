## Fourier 级数与变换

### 正交函数列
函数族$\{1,\sin x,\cos x,\sin 2x,\cos 2x,...,\sin nx,\cos nx,...\}$ 是任一长度为$2\pi$区间上的正交函数列， 用矩阵描述，等价于：

$$
A= \left [ \begin{array}{c} 1 \\
\quad & \sin x \\
\quad & \quad & \cos x \\
\quad & \quad & \quad & \sin 2x \\
\quad & \quad & \quad & \quad &\cos 2x \\
\quad & \quad & \quad & \quad & \quad & ... \\
\quad & \quad & \quad & \quad & \quad & \quad & \sin nx \\
\quad & \quad & \quad & \quad & \quad & \quad & \quad & \cos nx \\

\end{array} \right ]
$$
是一个非标准的正交坐标系，其各轴上的**单位刻度**不用二范式定义，而用积分定义如下:

若$X$是一列向量
$$
X= \left [ \begin{array}{c} 1 
 \\ \sin x 
 \\ \cos x 
 \\ \sin 2x 
 \\ \cos 2x 
 \\ ... 
 \\ \sin nx 
 \\ \cos nx 

\end{array} \right ]
$$
则有
$$
\int_{-\pi}^{\pi} XX^{T} dx=
\int_{-\pi}^{\pi} AAdx

= \left [ \begin{array}{c} 2\pi \\
\quad & \pi  \\
\quad & \quad & \pi  \\
\quad & \quad & \quad & \pi  \\
\quad & \quad & \quad & \quad &\pi  \\
\quad & \quad & \quad & \quad & \quad & ... \\
\quad & \quad & \quad & \quad & \quad & \quad & \pi  \\
\quad & \quad & \quad & \quad & \quad & \quad & \quad & \pi  \\

\end{array} \right ]
$$

### 级数

$$
f(x) \backsimeq \frac{a_0}{2} + \sum_{n=1}^{+\infty}(a_n \cos nx + b_n \sin nx)
$$

其各个系数可以由如下方法得到:
$$
a_n= \frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos nx dx, \quad n=0,1,2,...\\
b_n= \frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin nx dx, \quad n=1,2,...\\
$$

**知道了系数$a_n,b_n$，从频率的角度看，把各个基看成是不同的频率，就知道了原函数由哪些频率组成，它们各是多少。** 用很装逼的说法讲就是**时频变换**

## $a_n,b_n$的求法可以理解为用积分的形式量一量，$f(x)$在各个轴(基）上长度到底有多$\textcolor{blue}长$


## 收敛条件

- $f(x)$在点$x$的某个邻域$O(x,\delta)$上是分段单调有界函数， 粗俗的说就是绝对可积
- $f(x)$在点$x$处满足指数为$\alpha \in (0,1]$的[Hölder条件](https://en.wikipedia.org/wiki/H%C3%B6lder_condition)


## Fourier 变换

经过Euler公式的几翻折腾整合，级数展开可以写成如下形式:

$$
f(x) \backsimeq \frac{1}{2\pi}\int_{-\infty}^{+\infty}[\int_{-\infty}^{+\infty}f(t)e^{-iwt}dt]e^{iwx}dw
$$

其中方括号内的表达式就称为$f(x)$的**Fourier变换**
$$
\hat{f}(w)=F(w)=\int_{-\infty}^{+\infty}f(t)e^{-iwt}dt, \quad w \in (-\infty,+\infty)
$$

如何理解频率$w$会小于零？，默认级数展开都是加号（不经数学运算等价转换），而把基镜面对称扩展了。

而套用工程师不严谨的常用手段，把约等号换成等号(默认成立)

$$
f(x) \backsimeq F^{-1}[\hat{f}](x)=\frac{1}{2\pi}\int_{-\infty}^{+\infty}F(w)e^{iwx}dw
$$

就称这种操作为**逆变换**

## [卷积](http://mathworld.wolfram.com/Convolution.html)

设函数$f$和$g$在$x \in (-\infty,+\infty)$上有定义，且积分
$$
Fjuan[f(x),g(x)]=(f*g)(x)=\int_{-\infty}^{+\infty}f(t)g(x-t)dt=\int_{-\infty}^{+\infty}f(x-t)g(t)dt
$$ 
存在，则称其为$f$和$g$的卷积。

## Fourier 变换卷积定理

设函数$f$和$g$在$x \in (-\infty,+\infty)$上绝对可积，则有:
$$
F[f*g]=F[f]F[g]
$$
其中$F$是Fourier变换。

**翻译一下**：两个函数的卷积的傅利叶变换等于各自傅利叶变换的乘积，结合线性变换的条件$f(ab)=f(a)f(b)$来理解，很像在说傅利叶变换对于**卷积**的操作等价于**乘法**操作。

**横看成岭侧成峰，其实都是一堆土！**


## Parsevel 等式

设函数$f(x)$在$x \in (-\infty,+\infty)$上绝对可积，且$\int_{-\infty}^{+\infty}[f(x)]^2dx$收敛。则有

$$
\int_{-\infty}^{+\infty}[f(x)]^2dx=\frac{1}{2\pi}\int_{-\infty}^{+\infty}|F(w)|^2dw
$$


## 离散Fourier变换

计算机都只可能处理离散的Fourier变换！所以这才是真正的**应用**

对于数据序列$\{x(0),x(1),...x(N-1)\}$ 作如下变换
$$
W(j)=\sum_{n=0}^{N-1}x(n)e^{-2\pi i\frac{nj}{N}},\quad (j=0,1,2,...N-1)
$$
称为**离散Fourier变换**

### 离散正交关系式
$$
\frac{1}{N}\sum_{n=0}^{N-1}e^{-2\pi i \frac{nj}{N}}e^{2\pi i \frac{nk}{N}}=\delta_{j,k}=\{ \begin{array}{c} 1, & j=k \\ 0, &j\neq k \end{array}  
$$

### 离散逆变换

$$
x(k)=\frac{1}{N}\sum_{j=0}^{N-1}W(j)e^{2\pi i\frac{jk}{N}},\quad (k=0,1,2,...N-1)
$$


## FFT 快速Fourier变换

思想是将事先计算好的存起来，从而可以减少后续计算复数加法与乘法次数。

以$2$为底的FFT能将时间复杂度由原来的$N^2$降到$\frac{1}{N}\log_{2}{N}$， 由于$2$可以扩展，结合现在的多CPU和TensorFlow计算FFT就太easy了


## 参考
- [Fourier Notes](papers/fourier.md)
- [卷积Wolfrm Convolution](http://mathworld.wolfram.com/Convolution.html)

