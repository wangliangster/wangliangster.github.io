# 马尔可夫链
马尔可夫链(markov link)是一种特殊的**随机过程**,　它的随机性只与当前状态有关，与过往已发生的状态和将来可能发生的状态都无关。

![HMM](HMM.png ':size=400*247')

## 隐马尔可夫链(HMM hiden markov methold)
用来描述一种变化状态是隐藏的，且是离散的马尔可夫过程(**特殊随机过程**)。


- **隐状态序列**: $S=s_1s_2...s_T$　（参数表示）
- **隐状态集合**: $H=\{h_1,h_2,...h_N\},  s_i \in H$ (Hiden)

- **观测序列**: $O=o_1o_2...o_T$ （参数表示）
- **观测值集合**: $R=\{r_1,r_2,...r_M \}, o_i \in R$ （Reality ,已成事实）


### 一组参数 $\lambda = (\pi, A, B)$
- $\pi$ :
	- 初始状态概率分布，即第一个隐状态$s_1$为各状态$H=\{h_1,h_2,...h_N\}$的概率分别是多少。
- $A中的元素a_{ij}$ :
	- 当前时间点它的状态是$h_i$，下一个时间点变成$h_j$的概率，因为$H$有$N$个元素，所以它是个$N\times N$方阵，每一个时间点的转移矩阵都是相同的，此为**时间**无关性。
- $B中元素b_{ij}=P(o_t=r_j|s_t=h_i)=b_{s_t \to o_t}$ :
	- 它是一个$N\times M$矩阵，隐状态$h_i$到观测值$r_j$的概率，也是与时间先后无关的。



### 二个假设 
- $P(s_{t+1}|s_1s_2...s_t;o_1o_2...o_t)=P(s_{t+1}|s_t)$　齐次markov性假设
- $P(o_t|s_1s_2...s_t;o_1o_2...o_{t-1})=P(o_t|s_t)$ 
观测独立性假设

### 三种问法

- **Evaulation**, Given $\lambda$, 求$P(O|\lambda)$, 已知转移参数$\lambda$，评估一个已经发生的观测序列$O$的概率，用以判断我们的模型参数是不是准
- **Learning**,  $\lambda$, $\lambda_{MLE} = arg maxP(O|\lambda)$ 已知一个观测序列事实$O$，找出一组参数$\lambda$使得其概率最大, 用[$EM$算法](AI/ML/EM.md)
- **Decoding**,  $\hat{H}= arg maxP(H|O;\lambda)$, 已知观察序列和参数，求（反编）哪一串隐序列使得这个事实发生的概率最大，Viterbi算法（动态规划）穷举法（舍弃） 

## 公式推导
#### Evaulation **前向**, 给定$\lambda=(\pi,A,B)$　求$P(O|\lambda)$
$$
P(O|\lambda) = \sum_{S}^H P(O,S|\lambda) \newline
=\sum_{S}^H P(O|S;\lambda)P(S|\lambda)
\tag{1}
$$

又因为
$$
P(O|S;\lambda)=\prod_{t=1}^T b_{s_t \to o_t}, \; \; s_t \in H , o_t \in R \tag{2}
$$
$$
P(S|\lambda)=P(s_1s_2...s_T|\lambda)=P(s_T|s_1s_2...s_{T-1};\lambda)P(s_1s_2...s_{T-1};\lambda) \newline
递归下去
=\pi(s_1)\prod_{i=1}^{T-1} a_{s_{T-i}s_{T-i+1}}, \;\; s_i \in H\newline 
整理得
=\pi(s_1)\prod_{t=1}^{T-1} a_{s_ts_{t+1}}, \;\; s_t \in H
\tag{3}$$
所以
$$
P(O|\lambda)=\underbrace{\sum_{s_1}^H\sum_{s_2}^H...\sum_{s_T}^H}_{\text{O=N的T次方}} \pi(s_1) \prod_{t=1}^{T－1} a_{s_ts_{t+1}}\prod_{t=1}^T b_{s_t \to o_t}
\tag{4}
$$

若记
$$
\alpha_{t}(i)=P(o_1...o_t,s_t=h_i|\lambda) 
\tag{5}
$$
则有：
$$
\tag{6}
\alpha_{1}(i)=P(o_1,s_1=h_i|\lambda)=P(o_1|s_1=h_i)P(s_1=h_i)\newline 
=b_{i\to o_1}\pi(s_1=h_i) \newline
\alpha_{T}(i)=P(O,s_T=h_i|\lambda) 
$$
$$
\tag{7}
P(O|\lambda) = \sum_{i=1}^N P(O,S_T=h_i|\lambda)\newline
=\sum_{i=1}^N \alpha_{T}(i)
$$

展开
$$
\tag{8}
\alpha_{t+1}(j)=P(o_1...o_to_{t+1},s_{t+1}=h_j|\lambda) \newline
=\sum_{i=1}^N P(o_1...o_to_{t+1},s_t=h_i s_{t+1}=h_j|\lambda) \newline
=\sum_{i=1}^N P(o_{t+1}|o_1...o_t,s_t=h_i s_{t+1}=h_j;\lambda) P(o_1...o_t,s_t=h_i s_{t+1}=h_j;\lambda) \newline
=\sum_{i=1}^N P(o_{t+1}|s_{t+1}=h_j) P(o_1...o_t,s_t=h_i s_{t+1}=h_j;\lambda) \newline
=\sum_{i=1}^N P(o_{t+1}|s_{t+1}=h_j) P(s_{t+1}=h_j|s_t=h_i;\lambda) P(o_1...o_t,s_t=h_i;\lambda) \newline

=\sum_{i=1}^N b_{j \to o_{t+1}} a_{ij} \alpha_{t}(i)

$$

##### 计算过程：
	
- **step1:** 计算$\alpha_{1}(i) \; \;  from \;\; i=1 \to N$ 依据公式$(6)$
- **step2:** 计算$\alpha_{2}(j) \; \;  from \;\; j=1 \to N$ 依据**step1** 和公式$(8)$
- ......依据上一步和公式$(8)$
- **stepT:** 计算$\alpha_{T}(k) \; \;  from \;\; k=1 \to N$ 依据上一步和公式$(8)$
- **finally** 依公式$(7)$得 $P(O∣\lambda)$




#### Evaulation **后向**, 给定$\lambda=(\pi,A,B)$　求$P(O|\lambda)$

若记
$$
\tag{9}
\beta_{t}(i) = P(o_{t+1}...o_T|s_t=h_i;\lambda)
$$
则有
$$
\tag{10}
\beta_{1}(i) = P(o_2...o_T|s_1=h_i;\lambda)
$$
同时
$$
\tag{11}
\beta_{T-1}(i)=P(o_T|s_{T-1}=h_i;\lambda) \newline
=\sum_{j=1}^N P(o_T,s_T=h_j|s_{T-1}=h_i;\lambda) \newline
=\sum_{j=1}^N P(o_T|s_T=h_j|s_{T-1}=h_i;\lambda) P(s_T=h_j|s_{T-1}=h_i;\lambda) \newline
=\sum_{j=1}^N P(o_T|s_T=h_j,s_{T-1}=h_i;\lambda) a_{ij} \newline
=\sum_{j=1}^N b_{j\to o_T} a_{ij}
$$
现在我们列出递推式 $\beta_t$ 与$\beta_{t+1}$的关系

$$
\tag{12}
\beta_{t}(i)=P(o_{t+1}...o_T|s_t=h_i;\lambda) \newline
=\sum_{j=1}^N P(o_{t+1}...o_T,s_{t+1}=h_j|s_t=h_i;\lambda) \newline
=\sum_{j=1}^N P(o_{t+1}|o_{t+2}...o_T,s_{t+1}=h_j|s_t=h_i;\lambda) P(o_{t+2}...o_T,s_{t+1}=h_j|s_t=h_i;\lambda) \newline
=\sum_{j=1}^N b_{j \to o_{t+1}} P(o_{t+2}...o_T|s_{t+1}=h_j,s_t=h_i) P(s_t=h_i,s_{t+1}=h_j) \newline
=\sum_{j=1}^N b_{j \to o_{t+1}} \beta_{t+1}(j) a_{ij}
$$

而所求为
$$
\tag{13}
P(O|\lambda)=P(o_1...o_T|\lambda) \newline
=\sum_{i=1}^N P(o_1...o_T,s_1=h_i;\lambda) \newline
=\sum_{i=1}^N P(o_1...o_T|s_1=h_i;\lambda)P(s_1=h_i) \newline
=\sum_{i=1}^N P(o_1...o_T|s_1=h_i;\lambda)\pi(s_1) \newline

反向考虑：
=\sum_{i=1}^N P(o_1|o_2...o_T,s_1=h_i;\lambda)P(o_2...o_T,s_1=h_i;\lambda)\pi(s_1) \newline
=\sum_{i=1}^N P(o_1 | s_1=h_i)\beta_1(i) \pi(s_1=h_i) \newline
=\sum_{i=1}^N b_{s_1=h_i \to o_1} \beta_1(i)\pi(s_1=h_i)
$$

##### 计算过程：

- **step1:** 计算$\beta_{T-1}(i) \; \;  from \;\; i=1 \to N$ 依据公式$(11)$
- **step2:** 计算$\beta_{T-2}(j) \; \;  from \;\; j=1 \to N$ 依据**step1** 和公式$(12)$
- ......依据上一步和公式$(12)$
- **stepT-1:** 计算$\beta_{1}(k) \; \;  from \;\; k=1 \to N$ 依据上一步和公式$(12)$
- **finally** 依公式$(13)$得 $P(O∣\lambda)$

## Learning 问题

[EM算法](AI/ML/EM.md)

$$
\tag{14}
\theta^{t+1}=\underset{\theta}{\operatorname{argmax}} \int_{z} log P(X,Z|\theta) P(Z|X,\theta^t)dz
$$
对应到HMM的参数$\lambda=(\pi, A, B)$

$$
\tag{15}
\lambda^{t+1}=\underset{\lambda}{\operatorname{argmax}} \sum_{S}^H log P(O,S|\lambda) P(S|O,\lambda^t)
$$

又因为
$$
P(S|O,\lambda^t)=\frac{P(S,O|\lambda^t)}{P(O,\lambda^t)}
$$
中分母$P(O,\lambda^t)$是个定值，对$(15)$不影响，所以目标可变为

$$
\tag{16}
\lambda^{t+1}=\underset{\lambda}{\operatorname{argmax}} \sum_{S}^H log P(O,S|\lambda) P(S,O|\lambda^t)
$$

所以我们可以定义目标函数为：
$$
\tag{17}
f(\lambda, \lambda^t)=\sum_{S}^H log P(O,S|\lambda) P(S,O|\lambda^t) \newline
代入(4)式　\newline
=\sum_{S}^H [(log \pi(s_1) + \bcancel{\sum_{t=1}^{T－1} log a_{s_ts_{t+1}}}+ \bcancel{\sum_{t=1}^T log b_{s_t \to o_t}})P(S,O|\lambda^t)]
$$

为了简便计算，我们先只考虑$\pi(s_1)$, 因为后两项是连加性，所以整个函数的最值与第一项的最值也是一致的，　公式$(17)$可进一步简化为：

$$
\tag{18}
\sum_{S}^H [log \pi(s_1)P(S,O|\lambda^t)] \newline
=\sum_{s_1}^H [log \pi(s_1)P(O,s_1|\lambda^t)] \newline
=\sum_{i=1}^N [log \pi(s_1=h_i)P(O,s_1=h_i|\lambda^t)]
$$

问题转化为约束条件下的极值问题：
$$
\begin{cases}
   \sum_{i=1}^N [log \pi(s_1=h_i)P(O,s_1=h_i|\lambda^t)]   \\
   s.t \;\; \sum_{i=1}^N \pi(s_1=h_i)=1 
\end{cases}
$$

利用[Lagrange乘子法](AI/ML/Lagrange.md)

$$
\tag{19}
L(\pi, \eta)=\sum_{i=1}^N [log \pi(s_1=h_i)P(O,s_1=h_i|\lambda^t)] + \eta(\sum_{i=1}^N \pi(s_1=h_i)-1)
$$


$$
\tag{20}
\frac{\partial L}{\partial \pi_i}=\frac{1}{\pi_i}P(O,s_1=h_i|\lambda^t) + \eta =0
$$

两边乘以$\pi_i$ 再把所有$\pi_i$进行求和得：

$$

\sum_{i=1}^N P(O,s_1=h_i|\lambda^t) + \eta =0 \newline

\eta = -\sum_{i=1}^N P(O,s_1=h_i|\lambda^t) \newline
代入(20)得 \newline

\pi_i =\frac{P(O,s_1=h_i|\lambda^t)}{\sum_{i=1}^N P(O,s_1=h_i|\lambda^t)}
$$
最终得
$$
\pi_i^{t+1} =\frac{P(O,s_1=h_i|\lambda^t)}{P(O|\lambda^t)}

$$
由连加性同理可得
$$

a_{ij}^{t+1}=\frac{P(O,s_{t+1}=h_j|s_t=h_i)}{P(O|\lambda^t)}=\frac{a_{ij}^{t}}{P(O|\lambda^t)}\newline
b_{s_t=h_j\to o_t=r_k}^{t+1}=\frac{b_{s_t=h_j\to o_t=r_k}^t}{P(O|\lambda^t)}

$$


## Decoding 问题
$$
\tag{21}
P(S|O,\lambda) \newline
S=s_1s_2s_3...s_T \newline
O=o_1o_2o_3...o_T
$$

首先定义

$$
\delta_{t} (i) = \underset{index(s_1s_2...s_{t})}{\operatorname{max}} P(s_1s_2...s_t=h_i|o_1o_2...o_t)
$$
表示$t$时刻，隐状态$s_t=h_i$，为最符合已发生事实的概率标记,

则有
$$

\delta_{t+1} (j) = \underset{index(s_1s_2...s_{t+1})}{\operatorname{max}} P(s_1s_2...s_{t+1}=h_j|o_1o_2...o_{t+1}) \newline
=\underset{1<=i<=N}{\operatorname{max}} \delta_{t}(i) a_{ij} b_{j\to o_{t+1}}

$$

$$
\delta_{1}(i)=\underset{index(s_1)}{\operatorname{max}}P(s_1=h_i|o_1)
$$

令
$$
\varphi(t)=\arg \underset{1<=i<=N}{\operatorname{max}} \delta_t (i)=i
$$

所以有

$$
\varphi(1)\varphi(2)...\varphi(T) = index(S) = \underset{index(S)}{\operatorname{max}}P(S|O,\lambda) 
$$

计算步骤由$1,2,...T$即解码的隐状态序列，这种方法也叫Viterbi算法



## Viterbi算法

Viterbi算法　类似动态规划思想，求出每个子序列的最大值进而逐步得到整个序列发生的最大值。它相比穷举法对时间复杂度有很大的改进。

对于一个已经发生的观察序列$O=o_1o_2...o_T$, 要找到某一隐序列$s_1s_2...s_T, s_i \in H$ 使发生的概率最大
- 穷举法，每一个$s_i$都可以有$N$种可能，共有$N^T$种序列，根据参数，算出每一种序列的发观事实的概率，取最大的。
- Viterbi 算法，$o_1$找出最大概率对应的$s_1$,固定！$s_1 \to s_2=h_i \to o_2$选一条最大的固定, $s_1s_2\to s_3=h_i \to o_3$选一条最大的，这样就有$T*N$的计算复杂度。


### 参考
- [如何用简单易懂的例子解释隐马尔可夫模型?](https://www.zhihu.com/question/20962240/answer/33438846)
- [隐马尔科夫模型（HMM）—— 数学推导](https://blog.csdn.net/qq_27586341/article/details/94602772#%E4%BB%A3%E7%A0%81%E5%AE%9E%E7%8E%B0%EF%BC%9Ahmmlearn)
- [bilibili](https://www.bilibili.com/video/av32471608?p=8)
