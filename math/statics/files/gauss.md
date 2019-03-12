# 正态分布（高斯分布）
正态分布又名高斯分布， 是自然界中最常用的分布， 因为据大数中心定理，任何分布的任意组合，其均值，在数据足够大的假设下，都服从正态分布！这是自然的规律！

### 概率密度函数
$$
P(x|\mu,\sigma^2)={N}(x|\mu,\sigma^2)=\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$
### 期望
$$
E(x)=\mu=\int_{-\infty}^{+\infty}\frac{x}{\sqrt{2\pi \sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}dx
$$
### 方差
$$
\sigma^2(x)=\sigma^2=\int_{-\infty}^{+\infty}\frac{(x-\mu)^2}{\sqrt{2\pi \sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}dx
$$
