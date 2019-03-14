# F-分布
**F-distribution** 又名Snedecor's F distribution，以**(Fisher and W. Snedecor)**名字命名，中文直译**F-分布**，它是指：

若$U_1$和$U_2$是相互独立的两个随机变量，且它们分别服从自由度为$K_1$和$K_2$的[$\Large{\chi^2}$分布](math/statics/files/xx.md)，则:
$$
X=\frac{U_1/K_1}{U_2/K_2} \sim F(K_1,K_2)
$$

## 概率密度函数
$$
P(X=x;K_1,K_2)=\frac{\sqrt{\frac{(xK_1)^{K_1} K_2^{K_2}}{(xK_1+K_2)^{K_1+K_2}}}}{xB(\frac{K_1}{2},\frac{K_2}{2})},\quad for \quad x\in(0,+\infty)
$$

其中$B$是[Beta函数](math/analys/beta.md)

## 图像
<div align=center><img src="math/statics/files/f.jpg", width=500, height=310></div>

## 期望 
$$
E(x)=\frac{K_2}{K_2-2},\quad for \quad K_2>2
$$

## 方差
$$
\sigma^2(X)=\frac{2K_2^2(K_1+K_2-2}{K_1(K_2-2)^2(K_2-4)},\quad for \quad K_2>4
$$

## 应用
[F 检验](https://blog.csdn.net/lanchunhui/article/details/52185808)

## 参考
- [wiki](https://en.wikipedia.org/wiki/F-distribution)
- [百度百科](https://baike.baidu.com/item/F%E5%88%86%E5%B8%83)
