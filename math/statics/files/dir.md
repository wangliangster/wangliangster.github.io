# $Dirichlet$分布
**狄利克雷分布**是关于一组包含$n$个**连续变量**$x_i\in[0,1]$的概率分布，它受制于条件$\sum_{i=1}^{n}x_i=1$。

令$\mathbf{x}={(x_1;x_2;...x_n)}$, 参数$\mathbf{\alpha}=(a_1;a_2;...a_n),\quad a_i>0,\quad \sum_{i=1}^{n}{a_i}=A$

### 概率密度函数
$$
P(\mathbf{x}|\mathbf{\alpha})=Dir(\mathbf{x}|\mathbf{\alpha})=\frac{\Gamma(A)}{\Gamma(a_1)\Gamma(a_2)...\Gamma(a_n)}\prod_{i=1}^{n}x_i^{a_i-1}
$$
### 期望
$$
E(x_i)=\frac{a_i}{A}
$$
### 方差
$$
\sigma^2(x_i)=\frac{a_i(A-a_i)}{A^2(A+1)}
$$
### 协方差
$$
cov(x_i,x_j)=\frac{a_ia_j}{A^2(A+1)}
$$

当$n=2$时，**Dirichlet分布**退化为[Beta分布](math/statics/files/beta.md)。

**注意**, 应该把此处的$x_2$理解为Beta分布中随机变量$x$发生的对立事件---**不发生事件**

