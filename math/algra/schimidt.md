## 施密特(Schimidt)正交化
**定理：** $n$维殴氏空间中，任意一组基（线性无关）都可以通过线性变换转为等价的一组标准正交基。

**例子**
把
$$
a_{1}=(1,1,0,0), \quad a_{3}=(-1,0,0,1),\\
a_{2}=(1,0,1,0), \quad a_{4}=(1,-1,-1,1),\\
$$
变成单位正交向量组。

先**正交化**，得:

$\beta_{1}=a_{1}=(1,1,0,0)$

$\beta_{2}=a_{2}-\frac{(a_{2}\bullet\beta_{1})}{(\beta_{1}\bullet \beta_{1})}\beta_{1}=(\frac{1}{2},-\frac{1}{2},1,0)$

$\beta_{3}=a_{3}-\frac{(a_{3}\bullet\beta_{1})}{(\beta_{1}\bullet \beta_{1})}\beta_{1}-\frac{(a_{3}\bullet\beta_{2})}{(\beta_{2}\bullet \beta_{2})}\beta_{2}=(-\frac{1}{3},\frac{1}{3},\frac{1}{3},1)$

$\beta_{4}=a_{4}-\frac{(a_{4}\bullet\beta_{1})}{(\beta_{1}\bullet \beta_{1})}\beta_{1}-\frac{(a_{4}\bullet\beta_{2})}{(\beta_{2}\bullet \beta_{2})}\beta_{2}-\frac{(a_{4}\bullet\beta_{3})}{(\beta_{3}\bullet \beta_{3})}\beta_{3}=(1,-1,-1,1)$

再**单位化** 得

$\varepsilon_{1}=(\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2},0,0)$

$\varepsilon_{2}=(\frac{\sqrt{6}}{6},-\frac{\sqrt{6}}{6},\frac{\sqrt{6}}{3},0)$

$\varepsilon_{3}=(-\frac{\sqrt{12}}{12},\frac{\sqrt{12}}{12},\frac{\sqrt{12}}{12},\frac{\sqrt{12}}{4})$

$\varepsilon_{4}=(\frac{1}{2},-\frac{1}{2},-\frac{1}{2},\frac{1}{2})$
