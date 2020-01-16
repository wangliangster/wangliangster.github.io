# EM 算法　
- In statistics， an expectation–maximization (EM) algorithm is an iterative method to find maximum likelihood or maximum a posteriori (MAP) estimates of parameters in statistical models， where the model depends on unobserved latent variables.


## 公式推导

### 目标函数
$$
\tag{1}
L(\theta)=L(x_1， x_2， x_3，...x_n;\theta)=\prod_{k=1}^n P(x_k;\theta)， \theta \in \varTheta
$$

样本$x_k$之间相互独立，所以用乘法

- 取对数把连乘变为连加
$$
\tag{2}
\ell(L(\theta))=\sum_{k=1}^n logP(x_k;\theta)
$$

- 加入隐变量$z$考虑
$$
\tag{3}
\sum_{k=1}^n log \sum_{z}P(x_k， z;\theta)
$$

- 把隐变量看成分布$Q(z)$
$$
\tag{4}
\ell(L(\theta))=\sum_{k=1}^n log [ \sum_{z_i}P(x_k， z_i;\theta)] \newline 
=\sum_{k=1}^n log [ \sum_{z_i}Q(z_i)\frac{P(x_k， z_i;\theta)}{Q(z_i)}]
\newline
\geq \sum_{k=1}^n \sum_{z_i}Q(z_i) log\frac{P(x_k， z_i;\theta)}{Q(z_i)}
$$

- 最后一步利用$Jensen$不等式把**$log和函数$** 变为**$和log函数$**。
因为，$f(y)=log y$是**凹函数**，所以Jensen不等式反号，令$y_i=\frac{P(x_k,z_i;\theta)}{Q(z_i)}$
上式即$f(E(y)) \geq E(f(y))$，通过交替更新$z$和$\theta$， 通过寻找$Jensen$函数下界的极大值，从而达到找到原函数(*凹*)的极大值的目的，直至收敛（在端点）。
- 退一步讲，即使找到的不是极值，满足$Jensen$函数下界递增的参数也是使原函数向极值点奔去的参数。

更进一步拆分上式:
$$
\tag{5}
\sum_{k=1}^n \sum_{z_i}Q(z_i)[log P(x_k， z_i;\theta)-log Q(z_i)]
$$

分析：
- 我们的目标是公式$1$中的最大参数$\theta$, $x_k$是已知的样本数据; $Q(z_i)$是$Jensen$不等式中的一组$\lambda_i$, 它只在计算过程中起辅助作用，不是我们要的。
- 随机初始化一个$\theta^0$, 然后要找到一组$\lambda_i=Q(z_i)$使得$5$式最大, 此时$5$式的后半部分$log Q(z_i)$是会影响$Q(z_i)$的选择的（为了使整个$5$达到最大）。而一旦$Q(z_i)$选定了之后
- 目标函数就变成了以$\theta$为参数的函数，而此极大化过程与$5$式的后半部分无关，为了简化计算，一般都把后半部分略去了，从而目标函数变成了：
$$
\tag{6}
\theta^{t+1} =\underset{\theta^t}{\operatorname{argmax}}\sum_{k=1}^n \sum_{z_i}Q(z_i)log P(x_k， z_i;\theta^t)
$$ 

- 从整体来看，都是在提升$\theta$, 而$Q(z_i)=\lambda_i$只是辅助，中间虽然省掉了一部分，但整体上还是$\theta$还是提升了，虽然没有极值理论最大化提升，所以可以说是路径弯曲了一点，（节省了大量计算）。但大目标没有变，最终还是能收敛。算法的效果是可以达到的，而针对此处**破绽**的分析很少有人提，习惯都是一笔带过，故此补上这个遗憾。

### Jensen不等式
设$f$是定义域为$R$的函数

- 如果对于任意的$x，f(x)$的二次导数$f''(x) \geq 0$，那么$f$是凸函数。
- 当$X$是向量时，若其[$Hessian$](AI/ML/hessian.md)矩阵$H$是半正定的，那么$f$是凸函数。

![Jensen](Jensen.png ':size=300*200')

如果$f$是凸函数(有**极小值**,**凹函数**有极大值)，$X$是随机变量，那么：$E[f(X)] \geq f(E[X])$，通俗的说法是函数值的期望大于等于期望的函数值。[算术平均大于等于几何平均](http://mathworld.wolfram.com/JensensInequality.html)

## pLSA 如何用EM算法
Probabilistic latent semantic analysis (PLSA)， also known as probabilistic latent semantic indexing (PLSI)


$w_j$ :单词word，可统计的量，总共有$N$个不同的单词

$z_k$ :主题，可假设($K$个不同的主题)，可通过训练得到的隐变量

$d_i$ :文档，总共有$M$篇文档，样本总数


$$P(w_j|z_k)$$ 隐变量$z_k$假设固定条件下， 每一个单词的分布， 当$k$取一系列值$(1，2，3...)$时，就成了一个矩阵$A$， 矩阵中的元素$a_{kj}$表示第$k$个主题中第$j$个词的出现的概率，同理

$$P(z_k|d_i)$$　
表示文档确定下隐性主题的分布，把$k，i$展开也会得到矩阵$B$， $b_{ik}$表示第$i$篇文档中各主题的分布


$$
P(d_i，w_j)=P(d_i)P(w_j|d_i)=P(d_i)\sum_{k=1}^K P(w_j|z_k)P(z_k|d_i) \newline =P(d_i)\sum_{k=1}^K a_{kj}b_{ik}
$$

整个语料库生成的对数似然函数为：

$$\ell(L(\theta))=\ell(L(A，B))=\sum_{i=1}^M\sum_{j=1}^N n(d_i，w_j)log P(d_i，w_j) \newline
=\sum_{i=1}^M\sum_{j=1}^N n(d_i，w_j)[log P(d_i)+log\sum_{k=1}^K a_{kj}b_{ik}]
\newline
=\sum_{i=1}^M n(d_i)[log P(d_i)+\sum_{j=1}^N \frac{n(d_i，w_j)}{n(d_i)} log\sum_{k=1}^K a_{kj}b_{ik}]
$$

其中　$n(d_i)$ 表示第$i$篇文档词的总数，$n(d_i，w_j)$表示文档$i$中第$j$个词的个数, $\frac{n(d_i,w_j)}{n(d_i)}$表示第$i$篇文档中第$j$个词的词频。


上式中只有$a_{kj}$(表示第$k$个主题中第$j$个词的出现的概率)， $b_{ik}$(表示第$i$篇文档中各主题的分布)是变量，其它都是常数，目标是最大化似然函数$\ell(L(\theta))$。

仔细观察，因为考虑的是概率，所以有：
$$
\sum_{j=1}^N a_{kj}=1 \newline
\sum_{k=1}^K b_{ik}=1 \newline
a_{kj}\geq 0 \newline b_{ik} \geq 0
$$

于是问题转化为约束条件下的极值问题，可用[Lagrange乘子法](AI/ML/Lagrange.md) 解得:

$$
a_{kj}=\frac{\sum_{i=1}^M n(d_i,w_j)P(z_k|d_i,w_j)}{\sum_{o=1}^N\sum_{i=1}^M n(d_i,w_o)P(z_k|d_i,w_o)} \newline 

b_{ik}=\frac{\sum_{j=1}^N n(d_i,w_j)P(z_k|d_i,w_j)}{n(d_i)}
$$

利用$EM$算法，得出矩阵$A,B$ 也就得到了**“主题-词”**和**“文档-主题”**的分布。

## 参考
- [pLSA Wiki](https://en.wikipedia.org/wiki/Probabilistic_latent_semantic_analysis)
- [EM Wiki](https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm)
- [如何通俗理解EM算法](https://blog.csdn.net/v_july_v/article/details/81708386)
