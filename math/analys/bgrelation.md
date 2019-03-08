## Beta 函数与Gamma 函数的关系

$$
B(p,q)=\frac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}， \quad p>0，q>0
$$

## Stirling 公式
Gamma 函数有如下渐近估计：
$$
\Gamma(x+1)=\sqrt{2\pi x}(\frac{x}{e})^xe^{\frac{\theta}{12x}}，\quad x>0，0<\theta<1
$$
特别地，当$x=n$为**正整数**时
$$
n!=\sqrt{2\pi n}(\frac{n}{e})^ne^{\frac{\theta}{12n}}
$$
常被用来作$n!$估计

## Legendre 公式
$$
\Gamma(x)\Gamma(x+\frac{1}{2})=\frac{\sqrt{\pi}}{2^{2x-1}}\Gamma(2x)，\quad x>0
$$

## 余元公式
$$
\Gamma(x)\Gamma(1-x)=\frac{\pi}{\sin(\pi x)}，\quad 0<x<1
$$
由上可知，令$x=\frac{1}{2}\quad$易得，$\Gamma(\frac{1}{2})=\sqrt{\pi}$

**更进一步**，可得:
$$
\Gamma(\frac{3}{2})=\frac{\sqrt{\pi}}{2}，\quad \Gamma(\frac{5}{2})=\frac{3\sqrt{\pi}}{4}，\quad \Gamma(\frac{7}{2})=\frac{15\sqrt{\pi}}{8}，\quad \Gamma(\frac{9}{2})=\frac{105\sqrt{\pi}}{16}...
$$
