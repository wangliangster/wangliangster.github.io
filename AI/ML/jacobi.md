## Jacobian 矩阵
向量值函数：

$$
\begin{cases} y_1=f_1(x_1,x_2,...,x_n),\\
y_2=f_2(x_1,x_2,...,x_n),\\
........................\\
y_m=f_m(x_1,x_2,...,x_n), \end{cases} \quad (x_1,x_2,...,x_n)^T \in D
$$

若**$f$**的每一个分量函数$f_i(x_1,x_2,...x_n)$ 在**$x^0 \in D$**点都可**偏导**，就称**$f$**在$x^0$点**可导**，并称矩阵
$$
(\frac{\partial f_i}{\partial x_j}(x^0))_{m\times n}=\begin{pmatrix} \frac{\partial f_1}{\partial x_1}(x^0) & \frac{\partial f_1}{\partial x_2}(x^0) & ...&\frac{\partial f_1}{\partial x_n}(x^0)\\
\frac{\partial f_2}{\partial x_1}(x^0) & \frac{\partial f_2}{\partial x_2}(x^0) & ...&\frac{\partial f_2}{\partial x_n}(x^0)\\
...&...&...&...\\
\frac{\partial f_m}{\partial x_1}(x^0) & \frac{\partial f_m}{\partial x_2}(x^0) & ...&\frac{\partial f_m}{\partial x_n}(x^0) \end{pmatrix}
$$
为向量值函数$f$在$x^0$处的**导数**或者**Jacobian矩阵**


#### 若 $m=n$

Jacobi矩阵是个方阵，若其行列式不为零，则说明$f$在$x^0$附近存在反函数。

反函数是否存在是隐函数（**隐函数定理**）是否存在的前提，在分析中它是拉格朗日乘数法的理论基础。

可把Jacobi矩阵理解为一种特殊的**方向导数**，也可以理解为在$x^0$处的**梯度**

## 参考
- [wiki](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant)
