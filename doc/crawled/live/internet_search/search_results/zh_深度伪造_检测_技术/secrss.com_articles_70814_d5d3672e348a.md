# secrss.com/articles/70814

### 来源信息
- **URL**: https://www.secrss.com/articles/70814
- **域名**: www.secrss.com
- **检索关键词**: 深度伪造 检测 技术
- **页面抓取**: 成功

### 搜索摘要
随着大数据时代的到来，Deepfake深度伪造技术依靠深度生成算法，能够对人脸图像实施高质量篡改与伪造，并受到广泛的社会关注。

### 页面正文
随着大数据时代的到来，Deepfake深度伪造技术依靠深度生成算法，能够对人脸图像实施高质量篡改与伪造，并受到广泛的社会关注。尽管该技术可以为人们的生活带来很多便利，但是恶意的使用Deepfake已经对社会造成了隐私安全方面的隐患，也对当今社会产生了诸多实际的受害者案例。
由于生成模型的迭代，现有算法在被动地检测高质量伪造图像时陷入瓶颈，并在跨域实验的泛化性方面存在不稳定性。考虑到不同的深度伪造算法的最终目的都旨在对图像实施篡改以达到相同的结果，我们从主动防御的角度出发，提出人脸关键点感知水印（landmark perceptual watermark）这一概念，构建具备人脸关键点（facial landmark）语义的鲁棒感知水印，并根据经过Deepfake篡改后的图片与重新还原回来的鲁棒水印的匹配度，判断图片的真伪。我们将这一算法命名为LampMark.
本文首先使用人脸关键点分析了人脸图像的结构轮廓信息对Deepfake篡改的敏感特性（structure-sensitive characteristic）。由图1可知，遭遇过Deepfake篡改的图片与原图之间的人脸关键点错位程度普遍远高于普通的图像处理（如高斯噪声或Jpeg压缩）。因此，我们对人脸图像提取对应的人脸关键点坐标信息，并通过主成分分析（PCA）、特征归一化等机器学习方法，在免训练（training-free）的模式下完成了将人脸关键点转化成固定长度的二进制水印的操作，并最大限度地维持了原数据集内人脸关键点的分布规律。该操作确保了水印之间的独特性（discrimination）。
图1 人脸关键点对Deepfake篡改的敏感特性分析
上图中左图展示了人脸关键点在经历常见图像处理和Deepfake篡改前后之间的偏移欧氏距离；右图展示了人脸关键点的偏移程度受常见图像处理和Deepfake篡改后的分布情况。
与此同时，为了保证水印的保密性（confidentiality），确保非授权人员无法根据水印追溯回初始的人脸关键点从而达成恶意替换的目的，我们设计了一种元胞自动机加密系统，对人脸关键点感知水印进行加密，使其在加密后具备不可预测和不可逆向追溯的特性。最后，为了使水印可以维持鲁棒地针对图片进行嵌入和提取，我们搭建了一个自编码器结构（图2），与判别器进行联合训练，借助Deepfake篡改模型和常见图像处理的对抗攻击，使水印具备了良好的鲁棒性（robustness）。
图 2 LampMark算法流程图。
由图2的decoder部分可知，在图像经过未知的操作之后，通过还原初始嵌入的鲁棒水印，并与根据经过未知操作后的图片所制作的人脸关键点感知水印进行比较，便可知经过操作后的图片的真伪。
在实验中，本方法在库内（in-dataset）、跨库（cross-dataset）、跨算法（cross-manipulation）的设定下皆取得了优于对比工作的效果。并且，通过赋予水印语义含义这一设计，使得该主动Deepfake检测流程无需借助ground-truth水印便可以判断真伪。详细方法流程以及实验结果请参考原文。
论文信息
相关论文已被Proceedings of the 32nd ACM International Conference on Multimedia (MM "24) 录用，作者是南洋理工大学的王天一、Zhiqi Shen，齐鲁工业大学的黄梦筱、张笑，和山东大学的Harry Cheng。
Tianyi Wang, Mengxiao Huang, Harry Cheng, Xiao Zhang, Zhiqi Shen. LampMark: Proactive Deepfake Detection via Training-Free Landmark Perceptual Watermarks. In Proceedings of the 32nd ACM International Conference on Multimedia, 2024.（点击下方阅读原文查看论文全文）
供稿：王天一、黄梦筱
声明：本文来自隐者联盟，版权归作者所有。文章内容仅代表作者独立观点，不代表安全内参立场，转载目的在于传递更多信息。如有侵权，请联系 anquanneican@163.com。

---
*检索时间: 2026-07-24 14:38:05*
*搜索来源: DuckDuckGo*
