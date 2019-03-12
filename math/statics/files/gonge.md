# 共轭分布
共轭分布是指先验与后验拥有相同的形式，只是参数值不同，先验分布被称为后验分布的共轭先验。

## 先验分布
根据经验，假设待估计的参数$\theta$，符合某种形式且参数（经验值）已知的分布。
**例如:**
$$
	\theta \sim P_1(\theta|p=1,q=2)=Beta(\theta∣p=1,q=2)
$$
服从$p=1,q=2$的[Beta分布](math/statics/files/beta.md)

## 后验分布
假设某一随机变量$X$服从参数为$\theta$的[二项分布](math/statics/files/bin.md)，$\theta$未知，正是我们考虑的对象，但对$X$的观测数据有三${\{1,2,3\}}$，根据每一个不同的观测事实，结合经验假设$(p=1,q=2)$，参数$\theta$有不同的最大可能取值，这些**最大可能**所服从的分布被称为后验分布。
记为$P_2(\theta|X)$，如果其与$P_1(\theta|p=1,q=2)$有相同的形式，则称$P_1(\theta)$为它关于$X$分布的共轭先验。

## Bayes 分析
由Bayes公式
$$
P(\theta|X)=\frac{P(X|\theta)P(\theta)}{P(X)}=\frac{P(X|\theta)P(\theta)}{\int{P(X|\theta')P(\theta')}d\theta'}
$$
若记$X$服从的分布为$P_0(X)$，则有如下形式。
$$
P_2(\theta|X)=\frac{P_0(X|\theta)P_1(\theta)}{\int{P_0(X|\theta')P_1(\theta')}d\theta'}
$$
代入$X={\{1,2,3\}}$，可得关于$\theta$的三个具体值:
$$
P_2(\theta|X=1)=\frac{\left(\begin{array}{c} N \\ 1 \end{array} \right)\theta(1-\theta)^{N-1}\frac{(1-\theta)}{B(p=1,q=2)}}{\int{\left(\begin{array}{c} N \\ 1 \end{array} \right)\theta'(1-\theta')^{N-1}}\frac{(1-\theta')}{B(p=1,q=2)}d\theta'}
$$
$$
P_2(\theta|X=2)=\frac{\left(\begin{array}{c} N \\ 2 \end{array} \right)\theta^2(1-\theta)^{N-2}\frac{(1-\theta)}{B(p=1,q=2)}}{\int{\left(\begin{array}{c} N \\ 2 \end{array} \right)\theta'^2(1-\theta')^{N-2}}\frac{(1-\theta')}{B(p=1,q=2)}d\theta'}
$$
$$
P_2(\theta|X=3)=\frac{\left(\begin{array}{c} N \\ 3 \end{array} \right)\theta^3(1-\theta)^{N-3}\frac{(1-\theta)}{B(p=1,q=2)}}{\int{\left(\begin{array}{c} N \\ 3 \end{array} \right)\theta'^3(1-\theta')^{N-3}}\frac{(1-\theta')}{B(p=1,q=2)}d\theta'}
$$
其中，分母是一个**定值**(定积分，$N$是常量)，分子是$X$确定后关于$\theta$的具体形式，若有更多的数据画成图，它必然也会展开成某一分布形式，就是我们记作的$P_2(\theta|X)$，理论上，针对已知分布$P_0(X|\theta)$，可以选任何分布作为它的参数先验，因为胡猜和经验在概率本质上其实没有区别，但是与$P_0(X|\theta)P_1(\theta)$结合起来求积分（$P_0(X)$）多数情况下都很困难，然而有一种选择恰恰会使积分易求且化简后的形式与所选择的分布形式相同，只参数异， 这就是[Howard Raiffa等](https://en.wikipedia.org/wiki/Howard_Raiffa)发现的共轭先验。

经过多年发展总结起来有一张对应表，见wiki里[Conjugate prior](https://en.wikipedia.org/wiki/Conjugate_prior)
