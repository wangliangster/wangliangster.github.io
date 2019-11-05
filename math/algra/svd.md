## 奇异值分解

#### 预热知识

- 任何一个$n \times n$ 阶方阵$A$，如果它有$n$个线性无关的特征向量，则它可以对角化
	* 根据特征向量的定义
$$
AV=A[v_{1},v_{2},...v_{n}]=[v_{1},v_{2},...v_{n}]\left[\begin{array}{c} \lambda_{1} &\quad&\quad&\quad\\ \quad &\lambda_{2} &\quad\\ \quad &\quad &...&\quad \\ \quad &\quad &\quad &\lambda_{n} \end{array}\right ]=VD
$$
又因为，$V$是$n$个线性无关的特征向量组成的矩阵，所以$V^{-1}$存在
$$
A=VDV^{-1}
$$

- 不是所有$n$阶方阵都可对角化，但都可以化[Jordan标准形](math/algra/jordan.md)

- **任何一个矩阵乘以自身的转置都是一个对称矩阵**
- **任何一个矩阵的转置乘以自身也是一个对称矩阵**

**证：**
设$A$是任意$m \times n$矩阵，显然有$(A')'=A$。

$(AA')'=(A')'A'=AA'\Rightarrow m \times m$

$(A'A)'=A'(A')'=A'A \Rightarrow n \times n$


#### 任意实对称矩阵不同特征值所对应的特征向量必定正交
#### 单一特征值对应的多个特征向量组组成的基础解系必定线性无关
#### 任一线性无关的向量组都可通过[Schimidt正交化](math/algra/schimidt.md) 转为一组等价的正交向量组

**定理：** 任意一个实对称矩阵$A$，都存在一个$n$级正交矩阵$V$，使得$V'AV=V^{-1}AV$成对角形。

任何一个实对称矩阵，都等价于一个二次型，任何一个二次型都合同于一个标准型。
即可对角化了（不同只是正负惯性指数差异）

### 综上所述

任一实对称矩阵$A$， 都可以分解为三个简单矩阵的联乘，称之为**特征分解EVD**
$$
A=VDV'=VDV^{-1}
$$
其中$V$是正交阵，它由$A$的归一化特征向量按列排成，其中$D$为特征向量对应的特征值对角排成的对角阵。

### SVD
而对于普通的任意$m \times n$矩阵，它都可以分解成如下三个矩阵联乘
$$
A=UDV'
$$

其中$U$由$AA'$的特征向量组成，$V'$由$A'A$的特征向量组转置而成，而$D$由它们共同的特征值的正平方根构成。

之所有可以这样分解，都是通过对称阵构造而来。

**注意** SVD分解，$U$和$V'$并不是唯一的，但$D$上的值除排列顺序外是唯一的。

另外，据参考，把$A$的分解写成
$$
A=\sigma_{1}u_{1}v_{1}'+\sigma_{2}u_{2}v_{2}'+...\sigma_{r}u_{r}v_{r}', \quad r\leq min(m,n)
$$
可以理解为它是秩1的矩阵的和，每个秩一矩阵的权重由$\sigma_{i}$决定
若对$\sigma$按大小排序，取前$k$个，则把$U$由$m--to--k$称为"数据压缩"(**去除无效重复样本**)，$V$由$n--to--k$称为特征阵维(**PCA降维**)
### 参考
- [geometric explanation of singular value decompositions](http://www.ams.org/publicoutreach/feature-column/fcarc-svd)
- [奇异值的物理意义是什么](https://www.zhihu.com/question/22237507/answer/53804902)
