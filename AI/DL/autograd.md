# 详解Pytorch 自动微分

autograd 是Pytorch的重型武器之一，理解它的核心关键在于理解**vector-Jacobian product**

以三维向量值函数为例：

$X = [x_1,x_2,x_3] \\ Y = X^2$

按$Tensor, Element-Wise$机制运算，但实际上表示的是:

$Y=[y_1=x_1^2, y_2=x_2^2,y_3=x_3^2]$

$Y$对$X$的导数不是$2X$, 而是一个$Jacobian$矩阵（因为$X,Y$是向量，不是一维实数）:
$$
J =
\left ( \begin{array}{c}
\frac{\partial y_1}{\partial x_1} &\frac{\partial y_1}{\partial x_2} &\frac{\partial y_1}{\partial x_3} \\
\frac{\partial y_2}{\partial x_1} &\frac{\partial y_2}{\partial x_2} &\frac{\partial y_2}{\partial x_3} \\
\frac{\partial y_3}{\partial x_1} &\frac{\partial y_3}{\partial x_2} &\frac{\partial y_3}{\partial x_3} \\
 \end{array} \right ) =
\left ( \begin{array}{c}
2x_1 & 0 & 0 \\
0 & 2x_2 & 0 \\
0 & 0 & 2x_3 \\
 \end{array} \right )
$$

其中$y_1=f_1(x_1,x_2,x_3)=x_1^2$，它是关于$(x_1,x_2,x_3)$的函数, 而不仅仅是只关于$x_1$，这儿的特殊性是由$element-wise$运算机制引起的， 同理$y_2,y_3$。 


而$d(Y)$对每一个分量$x_i$的导数（变化率）是， 各个分量函数$y_j, j = 1, 2,3$对$x_i$的偏导数沿某一方向$v$的累积， 一般的，$v$的默认方向是$v = (1, 1, 1)$

当然，您也可以传入不同的方向进去，就是官方文档声称的可easy feed external gradient, 我们可以理解为关于$x_i$的偏导数*向量*在$v$方向上的投影，也可以理解为各个分量函数关于$x_i$偏导的权重。 $v$一旦确定，关于每个$x_i$的权重就定了，且都是一样的。

实验一下:

### 一 ---简单的隐式Jacobian
```python
>>> x = torch.randn(3, requires_grad = True)
>>> x
tensor([-0.9238,  0.4353, -1.3626], requires_grad=True)
>>> y = x**2
>>> y.backward(torch.ones(3))
>>> x.grad
tensor([-1.8476,  0.8706, -2.7252])
>>> x
tensor([-0.9238,  0.4353, -1.3626], requires_grad=True)
>>>
```

### 二 ---简单的显示Jacobian验证
```Python
>>> x1=torch.tensor(1, requires_grad=True, dtype = torch.float)
>>> x2=torch.tensor(2, requires_grad=True, dtype = torch.float)
>>> x3=torch.tensor(3, requires_grad=True, dtype = torch.float)
>>> y=torch.randn(3) # produce a random vector for vector function define
>>> y[0]=x1**2+2*x2+x3 # define each vector function
>>> y[1]=x1+x2**3+x3**2
>>> y[2]=2*x1+x2**2+x3**3
>>> y.backward(torch.ones(3))
>>> x1.grad
tensor(5.)
>>> x2.grad
tensor(18.)
>>> x3.grad
tensor(34.)

```
上面代码中**Jacobian**矩阵为:
$$
J =
\left ( \begin{array}{c}
2x_1 & 2 & 1\\
1 & 3x_2^2 & 2x_3\\
2 & 2x_2 & 3x_3^2
\end{array} \right )
$$

各分量函数为分别为:
$$
y_1=x_1^2+2x_2+x_3\\
y_2=x_1+x_2^3+x_3^2\\
y_3=2x_1+x_2^2+x_3^3
$$

投影方向： $v=(1,1,1)$
$$
v \circ J=[2x_1+1+2, 2+3x_2^2+2x_2,1+2x_3+3x_3^2]=[5,18,34]
$$

代码结果与分析相互印证

### 三---代入不同的$v=(3,2,1)$

先分析:
$$
v \circ J=[3*2x_1+2*1+1*2, 3*2+2*3x_2^2+1*2x_2,3*1+2*2x_3+1*3x_3^2]=[10,34,42]
$$

再代码验证:

```Python
>>> x1=torch.tensor(1, requires_grad=True, dtype = torch.float)
>>> x2=torch.tensor(2, requires_grad=True, dtype = torch.float)
>>> x3=torch.tensor(3, requires_grad=True, dtype = torch.float)
>>> y=torch.randn(3)
>>> y[0]=x1**2+2*x2+x3
>>> y[1]=x1+x2**3+x3**2
>>> y[2]=2*x1+x2**2+x3**3
>>> v=torch.tensor([3,2,1],dtype=torch.float)
>>> y.backward(v)
>>> x1.grad
tensor(10.)
>>> x2.grad
tensor(34.)
>>> x3.grad
tensor(42.)
```

吻合！

## 总结
- 既然$v$是权重或向量函数的投影方向，它的大小就必须与**向量函数**的**个数**对应
- 如果最后的函数值是标量，则说明“向量函数”只有一个，$.backward()$可以不传值，默认为$1$


## 参考
- [Understanding the heart of PyTorch’s magic](https://towardsdatascience.com/pytorch-autograd-understanding-the-heart-of-pytorchs-magic-2686cd94ec95)
- [CSC321 Lecture 10: Automatic Differentiation](https://www.cs.toronto.edu/~rgrosse/courses/csc321_2018/slides/lec10.pdf)
- [AUTOGRAD: AUTOMATIC DIFFERENTIATION](https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html#sphx-glr-beginner-blitz-autograd-tutorial-py)
- [PyTorch 的 backward 为什么有一个 grad_variables 参数？
](https://zhuanlan.zhihu.com/p/29923090)
