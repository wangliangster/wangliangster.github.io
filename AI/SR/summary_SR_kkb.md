# 语音识别

# 历史

## 20世纪
### 50 年代

贝尔实验室开始进行语音识别研究。主要是基于简单孤立词的语音识别系统。
例如，采用模拟电子器件实现针对特定说话人的十个英文数字的孤立词语音识别系统, 
59年，伦敦大学的科学家第一次使用**统计学**原理构建了四元音和九辅音的音素识别器。

### 60 年代

三个关键技术的出现对于语音识别的发展奠定了基础。
- 针对语音时长不一致的问题，来自RCA实验室的Martin提出了一种时间规整的机制。
- 前苏联的Vintsyuk提出采用动态规划算法实现动态时间规整(Dynamic Time Warping，DTW)
DTW可以有效的解决两个不同长度的语音片段的相似度度量，一度成为语音识别的主流技术。
- 卡耐基梅隆大学Reddy利用音素动态跟踪的方法进行**连续**语音识别。

### 70 年代
三个关键的技术被引入
- 模式识别思想
- 动态规划算法
- 线性预测编码
这些技术的成功使用使得孤立词语音识别系统从理论上得以完善，并且可以达到实用化的要求。

### 80 年代
两项关键技术
- 基于隐马尔科夫模型(Hidden Markov Model，HMM)的声学建模
- 基于n-gram的语言模型
HMM使得语音识别获得了突破，开始从基于简单的模板匹配方法转向基于**概率统计**建模的方法．此后统计建模的框架一直沿用到今天。
神经网络也在80年代后期被引入语音识别，但当时相比于GMM-HMM系统并未没有展现出优势。

### 90 年代
GMM-HMM框架得到广泛使用和研究，两种思想的引入解决了HMM模型参数自适应的问题
- 最大后验概率估计(Maximum APosteriori，MAP)
- 最大似然线性回归(Maximum Likelihood Linear Regression，MLLR)


## 21世纪 
###  00-06
GMM-HMM的语音识别系统框架已经趋于完善，进展缓慢。

###  10-至今
DNN—HMM在大词汇量连续语音识别任务上相比于传统的GMM—HMM系统获得了显著的性能提升， 深度学习结合GMM-HMM成为突破的主流期待




# 关键技术







## 参考
- [语音识别的发展过程](https://blog.csdn.net/baidu_31437863/article/details/82682163)
- [语音识别技术简述（概念->原理）](https://zhuanlan.zhihu.com/p/62171354)
- [语音识别的技术原理是什么？](https://www.zhihu.com/question/20398418/answer/18080841)
- [GMM算法](https://blog.csdn.net/bvngh3247/article/details/80778348) 
- [HMM算法](https://blog.csdn.net/bvngh3247/article/details/80778467) 
- [Viterbi算法（解码）](https://blog.csdn.net/bvngh3247/article/details/80786724) 
- [语音识别算法原理文档整理（一）](https://blog.csdn.net/bvngh3247/article/details/80778165) 





