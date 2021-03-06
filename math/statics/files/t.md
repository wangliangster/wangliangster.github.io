# t-分布
威廉·希利·戈斯特（1876－1937）以**"The Student"**笔名发表的假设检验方法，
通过抽样，用来衡量假设的真实程度t所服从的分布，称为t-分布。

关系式表示如下：
$$
t=\frac{\overline{x}-\mu_0}{s/\sqrt{n}}
$$

其中$\overline{x}$是样本均值，$\mu_{0}$是比较分布的期望（假设比较分布$X\sim N(X|\mu,\sigma^2)$，已知期望为$\mu_0$，方差未知，故用样本标差$s$代替，$n$为样本数。重复多次抽样，就得到关于t的分布。

由关系式，通俗讲就是**通过样本均值与原分布的期望差值，结合标准差，来衡量新的大数据样本期望是否真实提高了。**

## 概率密度函数

$$
P(t)=\frac{\Gamma(\frac{n}{2})}{\sqrt{(n-1)\pi}\Gamma(\frac{n-1}{2})}(1+\frac{t^2}{n-1})^{-\frac{n}{2}}
$$

## 应用
某一次具体的抽样，会得到一具体$t$值。$\int_{t}^{+\infty}P(X=t|\mu_0,s^2,n)dx$称为$P$值，它越大说明假设越成立，越小说明假设越不成立，通用域值为$0.05$，若小于该值，则称显著推翻假设。


#### 参考：
- [马同学](https://www.zhihu.com/question/30753175/answer/296723303)
