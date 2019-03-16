## 矩阵
### 转置
$$
(A')'=A \\
(A+B)'=A'+B'\\
(AB)'=B'A'\\
(kA)'=kA'
$$

### 逆
设$A_{ij}$是矩阵
$$
A=\left [ \begin{array}{c} a_{11} & a_{12} & ...& a_{1n} \\
a_{21} & a_{22} & ...& a_{2n} \\
... & ... & ...& ... \\
a_{n1} & a_{n2} & ...& a_{nn} \\
\end{array} \right]
$$
中元数$a_{ij}$的代数余子式，令
$$
A^{\bullet}=
\left [ \begin{array}{c} A_{11} & A_{12} & ...& A_{1n} \\
A_{21} & A_{22} & ...& A_{2n} \\
... & ... & ...& ... \\
A_{n1} & A_{n2} & ...& A_{nn} \\
\end{array} \right]
$$
$$
A^{\bigstar}=(A^{\bullet})'=
\left [ \begin{array}{c} A_{11} & A_{21} & ...& A_{n1} \\
A_{12} & A_{22} & ...& A_{n2} \\
... & ... & ...& ... \\
A_{1n} & A_{2n} & ...& A_{nn} \\
\end{array} \right]
$$
为矩阵$A$的**伴随矩阵**，若$d=|A| \neq 0$
