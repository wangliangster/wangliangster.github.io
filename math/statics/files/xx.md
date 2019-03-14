# $\chi^2$ 分布
若$X_1,X_2,X_3...X_K$是$K$个相互独立的标准[正态分布](math/statics/files/gauss.md)随机变量（$N(X_i|0,1$），令$Q=\sum_{i=1}^{K}X_i^2$，则称随机变量$Q$服从自由度为$K$的**卡方分布**, 记为：
$$
Q \sim \Large{\chi^2}\small{ (K)}
$$

## 概率密度函数
$$
P(Q=x|K)=\frac{x^{\frac{K}{2}-1}e^{-\frac{x}{2}}}{2^{\frac{K}{2}}\Gamma({\frac{K}{2}})},\quad for\quad x>0
$$


## 图像
<div align=center><img src="math/statics/files/chi.svg" width=500, height=310></div>

## 期望
$$
E(Q)=K
$$

## 方差
$$
\sigma^2(Q)=2K
$$

## 应用
- [卡方检验](https://blog.csdn.net/ludan_xia/article/details/81737669)
- [卡方分布分析与应用](https://blog.csdn.net/jinxiaonian11/article/details/78617936)
