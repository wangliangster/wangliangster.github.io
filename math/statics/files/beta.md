## Beta 分布
Beta 分布是关于连续变量$x\in[0,1]$的概率分布，它由两个参数$p>0,q>0$确定。

其概率密度函数定义如下：
$$
P(x|p,q)=Beta(x|p,q)=\frac{1}{B(p,q)}x^{p-1}(1-x)^{q-1}=\frac{\Gamma(p+q)}{\Gamma(p)\Gamma(q)}x^{p-1}(1-x)^{q-1}
$$
参考[Beta函数](math/analys/beta.md)，可知$\frac{1}{B(p,q)}$是为了概率求和(积分)等于$1$而构设。

不同的参数，有不同形状的概率密度曲线图， 如下:

![beta图](beta.jpg ':size=500*309')

#### 期望
$$
E(x)=\frac{p}{p+q}
$$
#### 方差
$$
\sigma(x)=\frac{pq}{(p+q)^2(p+q+1)}
$$ 

#### 具体应用参考
[Understanding the beta distribution (using baseball statistics)](http://varianceexplained.org/statistics/beta_distribution_and_baseball/)

[LDA数学八卦2-认识Beta/Dirichlet分布](http://www.flickering.cn/%E6%95%B0%E5%AD%A6%E4%B9%8B%E7%BE%8E/2014/06/lda%E6%95%B0%E5%AD%A6%E5%85%AB%E5%8D%A6%E8%AE%A4%E8%AF%86betadirichlet%E5%88%86%E5%B8%83/)

[带你理解Beta分布](https://blog.csdn.net/a358463121/article/details/52562940)

#### Tips
把它理解为**概率**的***概率分布***，低头想想
