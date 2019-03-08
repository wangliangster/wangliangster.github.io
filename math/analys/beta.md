## Beta 函数

$$
B(p,q)=\int_{0}^{1}x^{p-1}(1-x)^{q-1}dx \quad (p,q)\in(0,+\infty)\times(0,+\infty)
$$ 
被称为**Beta 函数**, 或**第一类Euler积分**(含参变量积分)

它有如下性质
- $B(p,q)$在$(0,+\infty)\times(0,+\infty)$上**连续**。
- $B(p,q)=B(q,p)$ **对称**
	+ **证** 作变换$x=1-t$就得到$$B(p,q)=\int_{0}^{1}x^{p-1}(1-x)^{q-1}dx=\int_{0}^{1}(1-t)^{p-1}t^{q-1}dt=B(q,p)$$
- **递推公式**
	+ $$B(p,q)=\frac{q-1}{p+q-1}B(p,q-1),\quad p>0,q>1$$
	+ $$B(p,q)=\frac{(p-1)(q-1)}{(p+q-1)(p+q-2)}B(p-1,q-1),\quad p>1,q>1$$
- $B(\frac{1}{2},\frac{1}{2})=\pi， \quad B(1,1)=1$(即**均匀分布**)
