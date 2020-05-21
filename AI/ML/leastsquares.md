# 最小二乘法 (Least Squares)

误差方程为:

$$Error(w|X,y)=(Xw-y)^T(Xw-y)$$
其最优解为:

<font color=blue size=3>$$w=(X^TX)^{-1}X^Ty$$</font>

其中$X$为$m \times n$ 的样本输入矩阵：
$$
\left[ \begin{array}{c}
     x_{11} & x_{12} & ...& x_{1n} \\
     x_{21} & x_{22} & ...& x_{2n} \\
     \vdots & \vdots &  \vdots & \vdots \\
     x_{m1} & x_{m2} & ...& x_{mn} \end{array} \right]
$$

$y$为$m \times 1$ 列向量，一般称为$labels$
$$
\left [ \begin{array}{c} y_1 \\ y_2 \\ \vdots \\y_m \end{array} \right ]
$$

$w$为$n \times 1$ 列向量，就是待求的拟和权重参数。
$$
\left [ \begin{array}{c} w_1 \\ w_2 \\\vdots\\w_n \end{array} \right ]
$$

## 最优解的详细推导过程

误差方程展开

$(Xw-y)^T(Xw-y)=((Xw)^T-y^T)(Xw-y)=\\ w^TX^TXw-(Xw)^Ty-y^TXw+y^Ty=$

因为，对于两个任意两个列向量$\alpha^T\beta=\beta ^T\alpha$，所以上式继续等于

$w^TX^TXw-2(Xw)^Ty+y^Ty$，它的极值（小）在对$w$求导为零处，所以有

$2X^TXw-2X^Ty=0$

整理得：
<font color=blue size=3>$$w=(X^TX)^{-1}X^Ty$$</font>

为什么对列向量求导可以得到上面的等式？

假设有以向量为参数的函数$f(v)=k^Tv$，对向量求导等价于以对向量的每个分量求偏导而形成新的向量:
$$
\frac{\partial f}{\partial v}=
\left [ \begin{array}{c} \frac{\partial f}{\partial v_1} \\ \frac{\partial f}{\partial v_2} \\\vdots\\\frac{\partial f}{\partial v_n} \end{array} \right ]
$$

把向量表达式展开:
$$f(v)=k^Tv=k_1v_1+k_2v_2+...k_nv_n$$
对每一分量求偏导有：
$$\frac{\partial f}{\partial v_1}=k_1$$
$$\frac{\partial f}{\partial v_2}=k_2$$
$$\vdots$$
$$\frac{\partial f}{\partial v_n}=k_n$$

所以有$\frac{\partial (k^Tv)}{\partial v}=k$

按同样的方法，我们把$w^TX^TXw-2(Xw)^Ty+y^Ty$展开分别对$w$的每个分量求偏导（先看**第二**部分，第三部分为零忽略）

$$P(w)=2* \left (\left[ \begin{array}{c}
     x_{11} & x_{12} & ...& x_{1n} \\
     x_{21} & x_{22} & ...& x_{2n} \\
     \vdots & \vdots & \vdots & \vdots \\
     x_{m1} & x_{m2} & ...& x_{mn} \end{array} \right] 
	\left[ \begin{array}{c} w_1 \\w_2\\\vdots\\w_n \end{array} \right ]\right)^T
\left[ \begin{array}{c} y_1 \\y_2\\\vdots\\y_m \end{array} \right ] \\ =
2* \left (\left[ \begin{array}{c}
     x_{11}w_1 + x_{12}w_2 +... x_{1n}w_n \\
     x_{21}w_1 + x_{22}w_2 + ... x_{2n}w_n \\
     \vdots  \\
     x_{m1}w_1 +x_{m2}w_2 + ... x_{mn}w_n \end{array} \right]
        \right)^T
\left[ \begin{array}{c} y_1 \\y_2\\\vdots\\y_m \end{array} \right ]\\ =
2(x_{11}w_1 + x_{12}w_2 +... + x_{1n}w_n)y_1+ \\ \quad 2(x_{21}w_1 + x_{22}w_2 + ... + x_{2n}w_n)y_2+ \\ \qquad\qquad\quad \vdots \qquad\qquad\qquad\qquad\qquad + \\ \quad 2(x_{m1}w_1 +x_{m2}w_2 + ...+ x_{mn}w_n)y_m
$$

由上可得

$$
\frac{\partial P(w)}{\partial w_1}=2(x_{11}y_1+x_{21}y_2+...x_{m1}y_m) \\
\frac{\partial P(w)}{\partial w_2}=2(x_{12}y_1+x_{22}y_2+...x_{m2}y_m) \\
\vdots \\
\frac{\partial P(w)}{\partial w_n}=2(x_{1n}y_1+x_{2n}y_2+...x_{mn}y_m) \\
$$

合并整理后可得
$$
\frac{\partial P(w)}{\partial w}=\frac{\partial [ 2(Xw)^Ty ]}{\partial w}=2X^Ty
$$

同理展开**第一**部分有(利用到$X^TX$是对称阵的信息）

$$
\frac{\partial Q(w)}{\partial w}=\frac{\partial [ w^TX^TXw ]}{\partial w}=2X^TXw
$$

所以可得
<font color=blue size=3>$$w=(X^TX)^{-1}X^Ty$$</font>

## 参考
- [The Normal Equation and matrix calculus](https://eli.thegreenplace.net/2015/the-normal-equation-and-matrix-calculus/)
