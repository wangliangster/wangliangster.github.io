# Gamma 分布

对[Gamma函数](math/analys/gamma.md)作个变形，可得:
$$
\int_{0}^{+\infty}\frac{t^{\alpha-1}e^{-t}}{\Gamma(\alpha)}dt=1
$$

若某随机变量$X$的概率密度函数为$\frac{x^{\alpha-1}e^{-x}}{\Gamma(\alpha)}$， 则该随机变量服从参数为$\alpha$的伽玛分布:
$$
X \sim \Gamma(x|\alpha)
$$

## 更一般形式
令$x=\beta t$，积分可变形为:

$$
\int_{0}^{+\infty}\frac{\beta^{\alpha}t^{\alpha-1}e^{-\beta t}}{\Gamma(\alpha)}dt=1
$$

可得随机变量$t$的密度函数：

$$
\frac{\beta^{\alpha}t^{\alpha-1}e^{-\beta t}}{\Gamma(\alpha)}
$$
称为更一般形式:
$$
t \sim \Gamma(t|\alpha,\beta)
$$
联系相应物理意义，其中$\alpha$称为**形状**参数，$\beta$称为**陡率**参数。具体参看下图

### 图像
![gamma图](gamma.jpg ':size=500*309')

### 期望
$$
E(x)=\frac{\alpha}{\beta}
$$
### 方差
$$
\sigma^2(x)=\frac{\alpha}{\beta^2}
$$

### 应用
随机变量$X$为等到第$\alpha$件事发生所需的等候时间。

例如，水文学中的年最大洪水及最大径流量问题，气象预报中的月最大风速及最大风压问题，可靠性中产品失效前的工作时间问题，海洋学中年海浪最大波高问题，化学实验中的反应时间问题，生态学中多个群体的总增长速度问题，经济统计中单位时间内个人的最大收入问题，等等。
