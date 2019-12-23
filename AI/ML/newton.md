## 牛顿法 Newton's method
基于Hessian矩阵来指导搜索，这种最简单的方法就是**牛顿法**

- 对于一元函数如下图

![pl](newton.gif ':size=400*247')

$x_{i+1}=x_i-\Delta x$

$x_{i+1}=x_i-\frac{f(x_i)}{f(x_i)'}$

分析：

$f(x_i)'=\lim\limits_{\Delta x \to 0}\frac{\Delta y}{\Delta x}$

把$f(x)'$看成是斜率$k$

就可以得到:
$
k=\tan\theta=\frac{f(x_i)}{\Delta x}
$
所以
$\Delta x = \frac{f(x_i)}{f(x_i)'}$ 按此方式更新一定是趋近于零点的

找到了零点，也就找到了原函数的可能极值点（鞍点除外）

- 对于多元函数（$f: \Reals^n \mapsto \Reals$）

它的一阶导数是*梯度*（$m=1$的特殊Jacobi矩阵）， 二阶导数是$Hessian$矩阵

更新方式

$X_{i+1}=X_i-H^{-1}\nabla f(X_i)$

其中$X_i$是$n$维列向量, $\nabla f(X_i)$是其Jacobi矩阵的转置
