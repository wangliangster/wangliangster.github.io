# 逻辑回归（logistics regression）

### 线性回归
$$ f(X) = W^TX+b , \quad X =[x_1,x_2,...x_n]^T, \quad x_i \in \Reals $$

$x_i$ 可对应于每一个样本的属性取值

### 非线性回归

$$ f(X) = \theta^TX , \quad X =[x_1^2,x_2,\sin(x_3), e^x_4...ln(x_n)]^T, \quad x_i \in \Reals $$

也可以把$x_i$ 理解为每一个样本的属性取值

### $sigmod$ 函数

<div align=center><img src="AI/ML/Logistic.svg", width=400, height=327></div>

$$ \sigma(x) = \frac{1}{1+e^{-x}}$$

它有以下特点：
- 定义域$(-\infty, +\infty)$
- $\sigma(-x)=1-\sigma(x)$
- $\sigma'(x)=\sigma(x)(1-\sigma(x))=\sigma(x)\sigma(-x)$
- 值域$(0,1)$， $\sigma(0)=0.5$， 当$x>0$时，$\sigma(x)>0.5$； 当$x<0$时， $\sigma(x)<0.5$

正是由于以上特性，它可以把线性（非线性）回归的问题转化为$0-1$分类问题，并且借助概率概念，其可解释性强。

### 逻辑(logisitic)回归 
令:
$$
z=f(X)=W^TX \\
P(y=1|z>0,W)=\sigma(z)\\
P(y=0|z<0,W)=\sigma(z)\\
$$

$f(X)$既可以是线性函数，也可以是非线性函数，$f(x)=0$为**决策边界**

这样就把线性回归转化为了二分类问题，进一步扩展可以解决多分类问题。



 

# 参考
- [逻辑回归 logistics regression 公式推导](https://zhuanlan.zhihu.com/p/44591359)
