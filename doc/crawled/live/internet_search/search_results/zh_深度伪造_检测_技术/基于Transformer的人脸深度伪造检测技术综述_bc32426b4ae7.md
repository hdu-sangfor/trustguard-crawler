# 基于Transformer的人脸深度伪造检测技术综述

### 来源信息
- **URL**: https://html.rhhz.net/GDGYDXXB/html/1699424549429-1096035086.htm
- **域名**: html.rhhz.net
- **检索关键词**: 深度伪造 检测 技术
- **页面抓取**: 成功

### 搜索摘要
摘要: 人脸深度伪造检测旨在对人脸图像和视频进行真伪鉴别，能为肖像权保护、虚假消息鉴定、网络诈骗防范等提供理论和技术支撑。早期的检测技术主要基于卷积神经网络(Convolutional Neural Networks，CNNs) 实现，并取得了显著的效果，但普遍存在泛化性能不足的问题。为了进一步提高人脸深度伪造检测技术的泛化性，最新的研究工作开始引入一种基于自我注意力机制的深度神经网络Transformer，其具有长距离依赖建模能力和全局感受野，可用于捕捉到图像

### 页面正文
2. ä¸å½äººæ°è¦å¯å¤§å¦ ç§»æ°ç®¡çå¦é¢(å¹¿å·) , å¹¿ä¸ å¹¿å· 510663
2. School of Immigration Administration (Guangzhou) , China Peopleâs Police University, Guangzhou 510663, China
éççæå¼äººå·¥æºè½åæ·±åº¦å¦ä¹ ææ¯çå¿«éåå±ï¼çææå ·çå®æçä¼ªé äººè¸å¾åä¸è§é¢åå¾è¶æ¥è¶å®¹æãç¶èï¼å¤§ä¼ä¾ç¶æ®éææâç¼è§ä¸ºå®âççå¿µï¼ç¸å ³ä¼ªé è§é¢æ çå¯¹å½ä»ç¤¾ä¼çä¿¡ä»»ä½ç³»é æäºæå¤§çå²å»ã2017å¹´ï¼ä¸ä¸ªåä¸ºâDeepfakeâçRedditç¤¾äº¤ç½ç«ç¨æ·ï¼å¨ç¤¾äº¤ç½ç«ä¸åå¸äºçå°Â·å æµçå¥³ææâæ¢è¸âè§é¢ï¼æ å¿çäººè¸æ·±åº¦ä¼ªé ææ¯çå ´èµ·ï¼æ¤åâDeepfakeâåâæ¢è¸âä¹è¢«å¼ç¨æä¸ºäºè¯¥ææ¯çä»£åè¯[1]ãå¨ä¿ä¹å²çªè¿ç¨ä¸ï¼ååä¹å å °æ»ç»æ³½è¿æ¯åºçæéçæ®µåä¼ªé ä¿ç½æ¯æ»ç»æ®äº¬çç´§æ¥è®²è¯è§é¢ï¼å¼åäºæ°ä¼çææ æ ç»ªãæ¤å¤ï¼ä¸äºä¸æ³ååå©ç¨æºè½AIæ¢è¸åæå£°ææ¯å®æ½çµä¿¡è¯éªçæ°éªå±èµ°å ¥äºå ¬å ±è§éï¼å¼èµ·ç¤¾ä¼å¤æ¹éè§ãä¸ºåºå¯¹æ·±åº¦ä¼ªé ææ¯å¸¦æ¥çç¤¾ä¼é£é©åææï¼è¶æ¥è¶å¤çç ç©¶å¢éå¼å±äººè¸æ·±åº¦ä¼ªé æ£æµææ¯ç ç©¶ã
æ©æçæ£æµææ¯ä¸»è¦ä»¥å·ç§¯ç¥ç»ç½ç»(Convolutional Neural Networksï¼CNNs) ä¸ºåºç¡[2-12]ï¼æåäººè¸åºåä½ä¸ºè¾å ¥ï¼åºäºçæè¿ç¨ä¸å¼å ¥çä¼ªé çè¿¹ä¿¡æ¯ï¼ä»ç©ºåãé¢åãæ¶åçå¤ä¸ªç»´åº¦ä¸å¦ä¹ å°æå ³ä¼ªé çè¿¹çç¹å¾è¿è¡äºåç±»(ç/å)å¤å«ï¼è¾¾å°äººè¸å¾ååè§é¢çä¼ªé´å«çç®çãåéäºå·ç§¯ç¥ç»ç½ç»æåéçå¤§å°åç¹å¾äº¤äºå¦ä¹ è½åå¼±ï¼åºäºå·ç§¯ç¥ç»ç½ç»çæ£æµææ¯æåå°çäººè¸ä¼ªé ç¹å¾å¾å¾æ´ä¸ºå±é¨ååä¸ï¼é¾ä»¥èèå°å¾åä¸å ¨å±åç´ ä¹é´çå ³ç³»åè§é¢ä¸çæ¶åºå ³è[13-15]ï¼æ¨¡åæ³åè½åä¸è¶³ã
ä¸ºäºæé«äººè¸æ·±åº¦ä¼ªé æ£æµææ¯çæ³åæ§ï¼ææ°çç ç©¶å·¥ä½å¼å§å¼å ¥ä¸ç§åºäºèªæ³¨æåæºå¶çç¥ç»ç½ç»Transformer[16-19]ãç¸å¯¹äºCNNsæ¨¡åï¼Transformeræ¨¡åå¨äººè¸æ·±åº¦ä¼ªé æ£æµä»»å¡ä¸å ·æä»¥ä¸4ä¸ªç¹ç¹ï¼(1) Transformeræ¨¡åå©ç¨èªæ³¨æåæºå¶æ¥ææè¾å ¥æ°æ®ä¸çé¿è·ç¦»ä¾èµå ³ç³»ãè¿ä½¿å¾å®è½å¤æ´å¥½å°çè§£è¾å ¥æ°æ®ä¹é´çå ³èï¼è¿å¯¹äºæ£æµæ·±åº¦ä¼ªé éå¸¸éè¦ï¼å ä¸ºä¼ªé å¯è½æ¶åå°è¿è·ç¦»çä¸ä¸æä¿¡æ¯ãç¸æ¯ä¹ä¸ï¼CNNsä¸»è¦ç¨äºææå±é¨ç¹å¾ï¼èè¾é¾ææå ¨å±ä¿¡æ¯ã(2) æ·±åº¦ä¼ªé æ£æµå¯ä»¥è¢«çä½æ¯ä¸ä¸ªåºåå°åºåé®é¢ï¼å ¶ä¸è¾å ¥åºåæ¯è§é¢å¸§æå¾åï¼è¾åºåºåæ¯äºå æ ç¾(çå®æä¼ªé ) ãTransformerå¨åºåå»ºæ¨¡ä»»å¡ä¸è¡¨ç°åºè²ï¼å ä¸ºå®éå¸¸éç¨äºå¤çå¯åé¿åº¦çè¾å ¥åºåãCNNséå¸¸éè¦åºå®å¤§å°çè¾å ¥ï¼å æ¤å¨å¤çå¯ååºåæ¶å¯è½éè¦é¢å¤çé¢å¤çæ¥éª¤ã(3) Transformeræ¨¡åå·²ç»å¨å¤§è§æ¨¡çææ¬æ°æ®ä¸è¿è¡äºé¢è®ç»ï¼ç¶åå¯ä»¥è¿ç§»å°è§è§ä»»å¡ä¸ãè¿ç§è¿ç§»å¦ä¹ ä½¿å¾Transformerè½å¤åçäºå¤§è§æ¨¡çå¤æ¨¡ææ°æ®ï¼ä»èæé«æ³åè½åãCNNséå¸¸éè¦å¨ç¹å®çå¾åæ°æ®éä¸è¿è¡è®ç»ï¼æ³åè½åè¾å¼±ã(4) æ·±åº¦ä¼ªé ææ¯å¯è½æ¶åå¯¹ææ§æ»å»ï¼å ¶ä¸ä¼ªé è è¯å¾ä½¿æ£æµå¨äº§çéè¯¯çç»æãTransformeræ¨¡åéå¸¸å¯¹å¯¹ææ§æ»å»æ´å æµæï¼å ä¸ºå®ä»¬å¨è®ç»æ¶å å«äºæ´å¤çæ°æ®å¤æ ·æ§åå¤ææ§ï¼ä»èæ´é¾åå°æ»å»ã
å°ç®åä¸ºæ¢è¿æ²¡ææç®å¯¹åºäºTransformerçäººè¸æ·±åº¦ä¼ªé æ£æµææ¯è¿è¡å ¨é¢çåæåæ»ç»ãé´äºæ¤, æ¬æé¦å ç®è¦ä»ç»äºè¯¥é¢åç ç©¶èæ¯ï¼éè¿°äºäººè¸æ·±åº¦ä¼ªé çæå ¸åææ¯ï¼ç¶åå¯¹ç°æåºäºTransformerçæ£æµææ¯è¿è¡æ»ç»åå½çº³ï¼æåæ¢è®¨äººè¸æ·±åº¦ä¼ªé æ£æµææ¯é¢ä¸´çææåæªæ¥ç ç©¶æ¹åãæ¬æå¯¹å¦ä½è®¾è®¡å ·æè¯å¥½æ³åæ§è½çäººè¸æ·±åº¦ä¼ªé æ£æµææ¯æéè¦åé´æä¹ã
1 äººè¸æ·±åº¦ä¼ªé çæå ¸åææ¯ç°æçäººè¸æ·±åº¦ä¼ªé çæææ¯å¤§è´å¯åä¸ºä»¥ä¸4ç§ç±»åï¼äººè¸çæãäººè¸äº¤æ¢ãå±é¨ä¼ªé åäººè¸éç°ãå ¶ä¸ï¼äººè¸äº¤æ¢åäººè¸éç°æ¯ç®åæ·±åº¦ä¼ªé æ¹åä¸ææµè¡çæ¹æ³ã
1.1 äººè¸äº¤æ¢äººè¸äº¤æ¢å¯ä»¥å®ç°è®©åå§äººç©åºç°å¨ä»/å¥¹ä»æ¥æ²¡æåºç°è¿çåºæ¯ä¸,éè¦æä¾ä¸ç»åå§äººè¸åç®æ äººè¸ä½ä¸ºè®ç»æ°æ®è¿è¡ä¼ªé ãå ¸åææ¯å æ¬ Deepfake[20]ãFaceSwap[21]çãDeepfakeåºæ¬åçå¦å¾1æç¤ºï¼å¾ä¸åå§è§é¢åç®æ è§é¢éèªå ¬å¼æ°æ®éFaceforensics++[2]ãDeepfakeææ¯éè¦å æåæºè§é¢ä¸çäººè¸ä»¥åç®æ è§é¢ä¸çäººè¸ï¼å¹¶å¯¹æåå°çäººè¸è¿è¡è£åªåå¯¹é½ï¼å¦è°æ´ç»ä¸å¤§å°ãå¨è®ç»ç¼è§£ç å¨é¶æ®µï¼ä½¿ç¨åå§äººè¸Aåç®æ äººè¸Bä½ä¸ºè®ç»æ°æ®ï¼è®ç»ä¸ä¸ªæå¼å ±äº«çç¼ç å¨ï¼ç¨äºæåAåBçå ±æé¢é¨å±æ§ï¼éåï¼AåBåèªè®ç»ä¸ä¸ªç¬ç«çè§£ç å¨åå«å¦ä¹ AåBç¹æçé¢é¨ä¿¡æ¯ï¼å®æå¯¹åºäººè¸éæãå¨æµè¯çæé¶æ®µï¼å¾ AåBçç¼è§£ç å¨è®ç»å¥½åï¼ä¸ºäºå®ç°åå§äººè¸Aåç®æ äººè¸Bä¹é´çäººè¸äº¤æ¢ï¼é¦å å©ç¨ç¼ç å¨å¯¹Bè¿è¡é¢é¨å±æ§ç¼ç ï¼æ¥çç¨Açè§£ç å¨å¯¹Bçé¢é¨å±æ§ç¼ç ç¹å¾è¿è¡è§£ç éæäººè¸ï¼çæå ·æäººè¸Aå¤è²ç¹å¾åæ¶ä¿çäººè¸Bé¢é¨è¡¨æ å¨ä½çæ·±åº¦ä¼ªé äººè¸ãå»¶ç»ç±»ä¼¼çæè·¯ï¼ç ç©¶è æåºååå±äºæ´å¤çäººè¸äº¤æ¢æ¹æ³ï¼å¦FaceShifter[22]ãSimSwap[23]çï¼ä½¿å¾çæçä¼ªé äººè¸è´¨éå¤§å¹ æé«ã
äººè¸éç°æ¯å©ç¨ç®æ äººè¸çå§¿æåè¡¨æ æ¥é©±å¨æºäººè¸ï¼ä½¿ä¿®æ¹åçäººè¸ä¿çç®æ äººè¸çé¿ç¸ååå§äººè¸çè¡¨æ ä¸å§¿æãå ¸åææ¯å æ¬Face2Face[24]åFsGAN[25]çãFace2Faceæ¯ç±Thiesçæåºçä¸ç§åºäºç»å ¸è®¡ç®æºå¾å½¢å¦è¿è¡äººè¸éç°çææ¯[24]ãå®è½å¤å¨ä¿æèº«ä»½ä¿¡æ¯ä¸åçæ åµä¸å°æºäººè¸çè¡¨æ è½¬ç§»å°ç®æ äººè¸ï¼å¹¶å¯ä»¥ä½¿ç®æ è§é¢äººè¸å®æ¶æ¨¡ä»¿å£ååè¡¨æ ãé¦å éè¿æåå¤´å®æ¶æè·æºäººè¸è§é¢ä½ä¸ºæºåºåå¸§ï¼å¹¶å©ç¨å¯éçå ç §ä¸è´æ§ç¹å¾æ¥å®æ¶è·è¸ªæºåç®æ è§é¢çé¢é¨è¡¨æ ï¼åå«çæå¯¹åºçé¢é¨è¡¨æ æ©ç ãç¶åï¼éè¿ä¸ç§æ°ä¼ éå½æ°å¨äºç»´ç©ºé´ä¸ææå°ä¼ éå½¢åï¼ä»èå°æºäººè¸è¡¨æ å®æ¶ä¼ éç»ç®æ äººè¸ãæåï¼å©ç¨çæçè¡¨æ è½¬æ¢æ©ç æä»¶éæ°æ¸²æç®æ äººè¸ï¼å¨ç®æ äººè¸åè¡¨æ è½¬æ¢æ©ç èåçåºç¡ä¸å¤çå¹³æ»çè¿¹ï¼å¹¶è¿è¡å ç §å¼ºåº¦çå¹é å¾å°æç»åæçææå¾ãFace2Faceåºæ¬åçå¦å¾2æç¤ºã
Transformer[16]æ¯ä¸ç§åºäºèªæ³¨æåæºå¶çæ·±åº¦ç¥ç»ç½ç»ï¼é¦å åºç¨äºèªç¶è¯è¨å¤ç(Natural Language Processingï¼NLP) ä»»å¡ï¼å¹¶éæ¸å¨è®¡ç®æºè§è§é¢åä¸å¾å°å¹¿æ³åºç¨ãTransformeræ ¸å¿æ¨¡åæ¯åºäºç¼ç å¨åè§£ç å¨æ¶æï¼èç¼ç å¨åè§£ç å¨ç±å¤ä¸ªå±ææãå¨ç¼ç å¨åè§£ç å¨çç»æä¸ï¼ç¼ç å¨è´è´£æåç¹å¾ï¼è§£ç å¨è´è´£å°æåå°çç¹å¾è½¬åä¸ºç»æãå ¶ä¸ï¼ç¼ç å¨ç±æ³¨æåå±åå ¨è¿æ¥å±ç»æãæ³¨æåæºå¶ä¸»è¦è½è®©ç¥ç»ç½ç»æ´èç¦äºè¾å ¥ä¸çç¸å ³ä¿¡æ¯ï¼åå°æ å ³ä¿¡æ¯çå¹²æ°ï¼éè¿æå¼æ¥å³å®èµäºè¾å ¥æ°æ®çæ³¨æåé«ä½ãåæ¶ï¼Transformerå ·æé¿è·ç¦»ä¾èµå»ºæ¨¡è½ååæ´å¹¿éçæåéï¼ä»èæ´åç¡®å°æååå¤çå¾åç¹å¾[26]ãä»æ°å¦è§åº¦æ¥åæï¼è®¡ç®æ³¨æåå¯ä»¥è¢«æè¿°ä¸ºä¸ä¸ªæ¥è¯¢(Query) å°ä¸ç³»åé®å¼å¯¹(Key-Value) çæ å°ãä¸»è¦æä»¥ä¸3ä¸ªæ¥éª¤ï¼
1) å¯¹è¾å
¥åºå
| $ {\rm{[}}{\boldsymbol{Q}}{\rm{,}}{\boldsymbol{K}}{\rm{,}}{\boldsymbol{V}}{\rm{]}} = {\boldsymbol{z}}{{\boldsymbol{U}}_{{\boldsymbol{QKV}}}},{{\boldsymbol{U}}_{{\boldsymbol{QKV}}}} \in {{\boldsymbol{R}}^{d \times 3{d_h}}}$ | (1) | 
2) è®¡ç®æ¥è¯¢åé
| $ f({\boldsymbol{Q,K}}) = \frac{{{{\boldsymbol{Q}}{\boldsymbol{}}^{\rm{T}}}{{\boldsymbol{K}}_i}}}{{\sqrt {{d_k}} }} $ | (2) | 
3) å©ç¨
| $ {\rm{Attention}}({\boldsymbol{Q,K,V}}) = {\rm{softmax}}(\frac{{{\boldsymbol{Q}}{{\boldsymbol{K}}^{\rm{T}}}}}{{\sqrt {{d_k}} }}) {\boldsymbol{V}} $ | (3) | 
èå¤å¤´æ³¨æåå°±æ¯éè¿
| $ \begin{gathered} {\rm{MultiHead}}({\boldsymbol{Q,K,V}}) = {\rm{Concat}}({\rm{hea}}{{\rm{d}}_1}, \cdots ,{\rm{hea}}{{\rm{d}}_h}) {\boldsymbol{W}} \\ {\rm{where}} \,{\rm{hea}}{{\rm{d}}_i} = {\rm{Attention}}({\boldsymbol{QW}}_i^{\boldsymbol{Q}}{{,}}{\boldsymbol{KW}}_i^{\boldsymbol{K}}{{,}}{\boldsymbol{VW}}_i^{\boldsymbol{V}}) \\ \end{gathered} $ | (4) | 
ViT(Vision Transformer) [17]æ¯å¨Transformerçåºç¡ä¸ä¿®æ¹å½¢æï¼ä¸»è¦åºç¨äºè®¡ç®æºè§è§ä¸çå¾ååç±»ï¼æ¯è§è§Transformerçæ åæ¶æãViTé¦å
å°è¾å
¥çå¾å
ä¸ºæ©å¤§è§è§Transformerçéç¨æ§ï¼ç ç©¶è ä»¬ç¸ç»§æåºäºéåä¸åè§è§ä»»å¡çåä½[26]ãæ ¹æ®åä½æ¨¡åçç¹ç¹åè¾¾å°çå¤çææï¼å¤§è´å¯åä¸º4ç±»ï¼
1) å·ç§¯Transformerãä¸ºäºå¢å¼ºæ¨¡åå¯¹äºå±é¨ç¹å¾çæåè½åï¼å¨Transformeræ¨¡åä¸å¼å ¥å·ç§¯æä½ï¼ææç»åå½çº³åå·®ä¸èªæ³¨æåãå ¸åæ¨¡åä»£è¡¨æDeiT[27]ãCvT[28]åConViT[29]ã
2) å±é¨Transformerãä¸ºäºå¢å¼ºæ¨¡åå¯¹äºé¿åºåæ°æ®çå»ºæ¨¡è½åï¼åå°å åå¼éï¼å¹¶æé«æ¨¡åå¨å¤çé¿åºåæ°æ®æ¶çæçï¼å¨Transformeræ¨¡åä¸æ¾å¼å ¨å±ç¹æ§éåå±é¨æ³¨æåï¼çµæ´»å¤çæ¥èªä¸åç©ºé´å°ºåº¦çç¹å¾ï¼æé«ç¹å¾çè¡¨è¾¾åäº¤äºè½åãå ¸åæ¨¡åä»£è¡¨æSwin Transformer[18]ãTwinsS-VT[30]åRegionViT[31]ã
3) åå±Transformerãä¸ºäºææåå°æ¢¯åº¦æ¶å¤±åæ¢¯åº¦çç¸çè®ç»è¿ç¨ä¸çé®é¢ï¼ä½¿å¾æ¨¡åè®ç»æ´å ç¨³å®åé«æï¼å¨Transformeræ¨¡åä¸éç¨åå±çç¥ï¼å¯ä»¥æé«æ¨¡åçè®ç»æ§è½ï¼æ´å¥½å°ææå¾åä¸çä¸åå°ºåº¦åå±æ¬¡ç»æç¹å¾ãå ¸åæ¨¡åä»£è¡¨æPVT[32]åTokens-to-Token ViT[33]ã
4) æ·±åº¦Transformerãä¸ºäºåå°æ¨¡åçè®¡ç®å¤æåº¦ï¼å¯ä»¥è®¾è®¡ä¸åçæ³¨æåæºå¶æ¥ä»£æ¿Transformerä¸çèªæ³¨æåç»æï¼æå»ºåºæ´æ·±å±æ¬¡çTransformeræ¨¡åä»¥è¾¾å°æ´å¥½çææãå ¸åæ¨¡åä»£è¡¨æDeepViT[34]ãCaiT[35]åCrossVit[19]ã
2.2 Transformerå¨æ·±åº¦ä¼ªé æ£æµä»»å¡ä¸çåºç¨éçæ·±åº¦ä¼ªé çæææ¯çæ¥çç²¾ç»åï¼ç ç©¶äººåå¼å§å¼å ¥åºäºTransformeræ¶æçæ£æµææ¯ï¼ä»¥æåæ£æµå¨å¨è·¨æ°æ®éä¸çæ³åæ§è½ãæ ¹æ®Transformerè¡¨å¾å¦ä¹ çä»»å¡ç±»åå¯åä¸ºåºäºè§è§æ¨¡æå¦ä¹ çæ£æµææ¯ãåºäºè§è§åå¬è§è·¨æ¨¡æå ³èå¦ä¹ çæ£æµææ¯ä¸¤ç±»ãå ¶ä¸ï¼åºäºè§è§æ¨¡æå¦ä¹ å å«äºç©ºé´ä¸ä¸æå ³èå¦ä¹ åæ¶é´ä¸ä¸æå ³èå¦ä¹ ãè¡¨1å¯¹Transformeræ¨¡åå¨äººè¸æ·±åº¦ä¼ªé æ£æµä»»å¡ä¸çåºç¨ååºåç±»å¹¶ç®è¦è¯´æäºåä¸ªæ¨¡åçç¹ç¹åä¸»è¦ä½ç¨ã
1) åºäºç©ºé´ä¸ä¸æå ³èå¦ä¹ çæ£æµææ¯ã
CNNsæ¶ææ é¿äºéè¿ä½¿ç¨å±é¨æåéãå ±äº«æå¼æ¥å¦ä¹ å±é¨ç¹å¾ãä½ç±äºCNNsçæåéæéï¼å®é¾ä»¥æè·å ¨å±ä¿¡æ¯ãç¸åï¼Transformerçèªæ³¨æåæºå¶å°å ¨å±å ³ç³»åé¿è·ç¦»ç¹å¾ä¾èµå ³ç³»å»ºæ¨¡ä¸ºè§è§è¡¨ç¤ºãå¯¹äºäººè¸æ·±åº¦ä¼ªé æ£æµï¼åºäºç©ºé´ä¸ä¸æå ³èå¦ä¹ çæ£æµææ¯ä¸»è¦ä»ç©ºååé¢åææå±é¨åå ¨å±çä¸ä¸è´çº¿ç´¢ã
ç¸æ¯äºçå®å¾åå¨ç¸é»åºåçèªç¶è¿ç»æ§ï¼æ·±åº¦ä¼ªé äººè¸å¾åçäººè¸åºåä¸å ¶ä¸ä¸æåºåå ·æä¸åçå¾åæ¥æºï¼å¯¼è´å ¶åå¨ä¸ä¸è´çç°è±¡ãåºäºç©ºåçº¿ç´¢çæ£æµææ¯ä¾§éäºæè·å¾åç©ºé´çä¸ä¸è´ä¿¡æ¯(å¦é¢è²çº¹çãåªå£°æçº¹ãè§è§ä¼ªå½±ç) ï¼ä»¥å¦ä¹ æ´ä¸ºæ¬è´¨çç¯¡æ¹æ£æµç¹å¾ãç¶èï¼å½éå°åç§ç ´åæ§å½¢å¼çå¾åéåæ¶(å¦å¾ååç¼©ãè§é¢ç¼è§£ç è½¬æ¢ç) æè æ°æ®åä¸å¹é çæ¡ä»¶ä¸ï¼è¿ç§ä½çº§å«ççº¹çä¸ä¸è´ä¿¡æ¯å¾å®¹æåå°å¹²æ°ï¼ä»èå¯¼è´æ£æµæ¹æ³çæ§è½æ¥å§ä¸éãä¸ºæ¤ï¼Dong Xç[36]æåºåºäºViTçèº«ä»½ä¸è´æ§æ£æµæ¨¡å(Identity Consistency Transformerï¼ICT) ï¼å¦ä¹ äººè¸é«çº§è¯ä¹ä¿¡æ¯ï¼ç¹å«æ¯æ£æµå¯¹è±¡çèº«ä»½ä¿¡æ¯ï¼éè¿å¨è¾å ¥ç«¯åµå ¥åºåä¸æ·»å ä¸¤ä¸ªé¢å¤çå¯å¦ä¹ çåµå ¥æ è®°ï¼ä»èå©ç¨å é¨åå¤é¨é¢ååºåçèº«ä»½ä¸ä¸è´æ§æ¥æ£æµå¯ççäººè¸ãè¯¥æ¨¡åå¨è·å¾èº«ä»½æåç½ç»åä¸éè¦ä»»ä½é¢å¤çè®ç»ï¼ä¸å¯ä»¥å¨æ²¡æä»»ä½ç±äººè¸æä½æ¹æ³çæçåè§é¢æ åµä¸è¿è¡è®ç»ãä½æ¯ï¼æ¤ç§æ¹æ³éè¦å¤§éçèº«ä»½ä¿¡æ¯æ è®°è¿è¡è®ç»ï¼ä¸åªè½éå¯¹åå¨èº«ä»½ä¸ä¸è´çäººè¸äº¤æ¢è§é¢ï¼æ æ³æ£æµäººè¸éç°çä¼ªé è§é¢ï¼å å ¶èº«ä»½ååä¿æä¸è´ãä¸ºäºåå°æ°æ®æ è®°å·¥ä½ï¼è§£å³ç±äºæ°æ®åä¸å¹é å¯¼è´æ£æµæ§è½ä¸éçé®é¢ï¼Chen Hç[37]æåºç¨ä¸ä¸ªä¸¤é¶æ®µçèªçç£èå¼(Transformer-Based Self-Supervisedï¼TBSS) æ¥æé«æ·±åº¦ä¼ªé æ£æµçæ³åè½åãå¨ç¬¬ä¸é¶æ®µçèªçç£æ©è½å¾åå»ºæ¨¡(Masked Image Modelingï¼MIM) åé¢è®ç»ä¸ï¼å©ç¨æ²¡æä»»ä½å¾åç±»æ³¨éçåºåæ©è½åé¢æµçç¥æ¥è®ç»ä¸ä¸ªSwin Transformerç¼ç å¨ï¼å¹¶éè¿å¼ºå¤§çé¿æä¾èµå»ºæ¨¡è½åå¯¹åç´ ä¹é´çå ³ç³»å»ºæ¨¡ï¼æåç±»å ä¸è´æ§ç¹å¾ãå ¶ä¸ï¼å¾ååºåæ¯è§è§Transformerçåºæ¬å¤çåå ï¼å¨åºåçº§å«ä¸æä½å¯ä»¥å®ç°å¯è§ææ©è½ï¼ä»èéè¿éå»ºè¢«æ©è½ç ´åçå¾åæ¥å¦ä¹ æç¨çè¡¨ç¤ºï¼æ´å¥½å°ä¿åå¾åä¿¡æ¯ãç»è¿é¢è®ç»åçç¬¬äºé¶æ®µï¼ç¨æ è®°æ°æ®å¯¹é¢è®ç»åçç¼ç å¨è¿è¡å¾®è°ï¼ä»¥æé«å ¶é´å«æ§è½ãè½ç¶è¯¥æ¨¡åå¨æ£æµæ³åæ§è½ä¸æäºä¸å®çæåï¼ä½ç±äºéç¨äºå¤§è§æ¨¡çé¢è®ç»æ°æ®ï¼éè¦å¯¹ä¸ä¸ªåºå¤§çéª¨å¹²ç½ç»è¿è¡é¢è®ç»ï¼å¯¼è´äºè¾å¤§çè®¡ç®ææ¬ã
æ¤å¤ï¼ç ç©¶äººå[3-4,7]å¨ç ç©¶ä¸åç°ï¼æ·±åº¦ä¼ªé çæç½ç»ä¸çåå·ç§¯ä¸éæ ·æä½æ æ³éå»ºèªç¶å¾åé¢è°±åå¸ï¼å¨é¢åä¸åç°ç½æ ¼åç¹å¾ä»èå¯¼è´åæåè¸ä¸çå®äººè¸çé¢è°±åå¸åå¨å·®å¼ãå æ¤ï¼é¨åç ç©¶å·¥ä½éåèåç©ºååé¢åç¹å¾è¿è¡æ£æµçç ç©¶è·¯çº¿ãWang Jç[38]å¼å ¥äºä¸ä¸ªå¤æ¨¡æå¤å°ºåº¦æ£æµç½ç»(Multi-modal Multi-scale Transformerï¼M2TR) ï¼å°è¾å ¥å¾ååå²æä¸åå¤§å°çåºååï¼å¹¶ä½¿ç¨å·ç§¯Transformeréæå¤å°ºåº¦ä¿¡æ¯ï¼ç¨äºææå¾åååºåå¨ä¸åç©ºé´å±æ¬¡çå±é¨ä¸ä¸è´æ§ãèé¢çæ»¤æ³¢å¨ç¨äºææé¢åå çç»å¾®ä¼ªé çè¿¹ï¼ä½ä¸ºä¸ç§äºè¡¥çæ¨¡å¼ãå¨ç©ºé¢åäº¤åæ¨¡æèååä¸ï¼éç¨Transformerçæ¥è¯¢âé®âå¼èªæ³¨æåæºå¶èåæä¸ä¸ªç»ä¸çè¡¨ç¤ºãè¯¥æ¹æ³è½ç¶é¢å¯¹é«åç¼©çä¼ªé å¾åæ¶å ·æè¾å¼ºçä¼ªé æ£æµè½åï¼ä½é¢å¯¹æªç¥ä¼ªé æ¹æ³æ¶æ£æµè½åä»ä¼æ¥å§ä¸éãä¸ºäºå¦ä¹ ä¸åç©ºé´å±æ¬¡çç¹å¾ï¼Tan Zç[39]ä»å ¨å±è§åº¦åºåï¼æåºäºä¸ç§å ·æå±é¨ç¹å¾è¡¥å¿åèåæ£æµæ¡æ¶(Transformer-based Framework with Feature Compensation and Aggregationï¼Trans-FCA) ï¼é¤äºå©ç¨Transformeræè·å ¨å±çº¿ç´¢å¤ï¼è¿å©ç¨å·ç§¯æ¥æè·å±é¨ç»èä¼ªé ç¼ºé·ãå¨å±é¨ç¹å¾è¡¥å¿æ¨¡åï¼æåºçå ¨å±âå±é¨äº¤åæ³¨æåä»£Transformerèªæ³¨æåæ¨¡åï¼èåäºå ¨å±Transformerç¹å¾åå±é¨å·ç§¯ç¹å¾ãå¨èåæ¨¡åï¼æåºäºä¸ä¸ªé¢å¯¼èåæ¨¡åæ¥äº¤äºé¢åä¸çææç¹å¾ï¼æ¨å¨åå±èéä¸é¢çç¸å ³çç¹å¾ï¼éåï¼ä½¿ç¨å¤å¤´èç±»æå½±å°ææç¹å¾èåå°åä¸ªèç±»(ç¹å¾åé) ä¸è¿è¡æ·±åº¦ä¼ªé æ£æµãè¯¥æ¹æ³æ¯TransformeråCNNs ä¸¤ç§æ¶æéæçå ¸åä»£è¡¨ï¼æç¤ºäºå±é¨ä¼ªé æ¨¡å¼åå ¨å±å ³ç³»è¡¨ç¤ºæ¯æ·±åº¦ä¼ªé æ£æµå¨æ³åè½åçå ³é®ï¼ä¸ºåç»å·¥ä½æä¾äºå¾å¥½çç ç©¶æè·¯ãåæ¤å¯åï¼ä¸å½ç§å¦ææ¯å¤§å¦çç¼ªé¿æ¶ç[40]æåºä¸ç§ååæ¯çåå±é¢çè¾ å©äº¤äºç½ç»(Hierarchical Frequency-assisted Interactive Networksï¼HFI-Net) ï¼ä»¥æ´å¥½å°å©ç¨TransformeråCNNsæ¶æåèªä¼å¿ï¼åå«æè·å ¨å±ä¸ä¸æä¿¡æ¯åå±é¨ç»èãå ·ä½æ¥è¯´ï¼ææåºçååæ¯ç½ç»éç¨å¯åç¦»çå·ç§¯æ¨¡ååTransformeræ¨¡åæ¥éä¸æè·å±é¨ä¼ªå½±åå ¨å±ç¹å¾ï¼å©ç¨ä¸é«é¢æ¨¡å¼æ¥ç»åååæ¯ç½ç»çç¹å¾ï¼å å¼ºä¸¤ä¸ªåæ¯ä¹é´çäºè¡¥ç¹å¾äº¤äºãè¯¥æ¹æ³è¯æäºå±é¨ä¼ªé ä¼ªå½±åå ¨å±ä¸ä¸æä¿¡æ¯å ·æå¼ºçäºè¡¥å ³ç³»ï¼æ¹åäºæ·±åº¦ä¼ªé æ£æµå¨è·¨åç¼©ãè·¨åºæ£æµæ¶çææï¼ä½å¹¶æ²¡æä¼åTransformerä½ç³»ç»æçèªæ³¨æåæºå¶ï¼åªæ¯å°å¤ä¸ªTransformeræ¨¡ååCNNsè¿è¡ç®åçç»åãä¸ºäºå¢å¼ºè§è§Transformerèªæ³¨æåæºå¶æè·ç»ç²åº¦çç¹å¾ç»èï¼è¯¥ç ç©¶å¢éæåºé«é¢ç»ç²åº¦æ£æµç½ç»(Fine-Grained Transformerï¼F2Trans) [41]ï¼å¨Transformeræ¶æä¸å¼å ¥ä¸å¿å·®åç®åï¼ä¸é¨è®¾è®¡äºä¸ä¸ªåæµé«é¢å¾®ç²åº¦æ¨¡åç¨äºäººè¸ä¼ªé æ£æµä»»å¡ï¼å åå©ç¨äºå¨ç©ºååé¢åçç»ç²åº¦ä¼ªé çè¿¹ä¿¡æ¯ãè¯¥ç½ç»å å«ä¸¤ä¸ªæ ¸å¿ç»ä»¶ï¼ä¸å¿å·®åæ³¨æ(Central Difference Attentionï¼CDA) åé«é¢å°æ³¢éæ ·(High-frequency Wavelet Samplerï¼HWS) ãå ¶ä¸ï¼ä¸å¿å·®åæ³¨æå©ç¨å·ç§¯æ¥çæå±é¨çº¹çç¹å¾ä½ä¸ºèªæ³¨æåçæ¥è¯¢ï¼ç¶åç±ä¸å¿å¾®åç®åå¯¹æ¥è¯¢ç¹å¾çé»å± ä¹é´çå±é¨å ³ç³»è¿è¡å»ºæ¨¡ï¼çæèªæ³¨æåçé®å¼å¯¹ï¼ä»èå¢å¼ºäºTransformerèªæ³¨æåæºå¶çç»ç²åº¦è¡¨ç¤ºè½åï¼ä»¥æè·æ´å¤çä¿¡æ¯ç¹å¾ãé«é¢å°æ³¢éæ ·ç»ä»¶å¯¹ç¹å¾å¾çé«é¢ä¼ªé çº¿ç´¢è¿è¡å±æ¬¡æ¢ç´¢ï¼å¹¶å ³æ³¨å±é¨é¢åä¿¡æ¯ï¼ææéå¶äºä½é¢åéå¼èµ·çæ¨¡åå¹²æ°ãä½æ¯ï¼è¯¥æ¹æ³å¨éå°ä¸å¯è§çæ°å¨æ¶ï¼æ§è½ä¸éææ¾ã
2) åºäºæ¶é´ä¸ä¸æå ³èå¦ä¹ çæ£æµææ¯ã
ä¸è¿°åºäºç©ºé´ä¸ä¸æå ³èå¦ä¹ çæ£æµæ¹æ³å¤§å¤éå¯¹ä¼ªé äººè¸å¾åæè ä¼ªé è§é¢ä¸çåå¸§å¾åè¿è¡æ£æµ, èå¯¹äºä¼ªé è§é¢æ¥è¯´, è¿å¯ä»¥å©ç¨æ¶é´åçº¿ç´¢æé«ä¼ªé æ£æµç®æ³çæ§è½ãåºäºæ¶é´ä¸ä¸æå ³èå¦ä¹ çæ£æµææ¯ä¸»è¦ä»ä¸åæ¶é´å°ºåº¦æææ´ç²¾ç»åå ¨é¢çæ¶åä¸ä¸è´çº¿ç´¢ï¼ä»¥æ£æµæ·±åº¦ä¼ªé è§é¢ãä¸ºäºæåæ¶é´åä¿¡æ¯ï¼ä»¥å¾éç¨çé¿çæè®°å¿(Long Short-Term Memoryï¼LSTM) [42]æºå¶éè¿è®¾è®¡é¨æ§ç¶æï¼ä»èè®°ä½éè¦é¿æè®°ä½çä¸è¥¿ï¼å¿è®°ä¸éè¦çä¿¡æ¯æ¥æ§å¶ä¼ è¾ç¶æãèå¨Transformerçèªæ³¨æåæºå¶ä¸ï¼è§é¢å¸§åºåä¸çæ¯ä¸å¸§é½å¯ä»¥ä¸ææå ¶ä»å¸§è¿è¡å ³ç³»è®¡ç®ãå æ¤ï¼ä¸LSTMç¸æ¯ï¼å¯ä»¥æ´å¥½å°ææè¿è·ç¦»å¸§çå ³ç³»ï¼ä»èæä¾æ´ææçæ¶é´ä¸ä¸æå ³èã
ç±äºç°æçä¼ªé è§é¢å¤§å¤é½æ¯å¯¹çå®è§é¢ä¸æ¯ä¸å¸§å¾åè¿è¡ä¼ªé ï¼åå°ä¼ªé å¾åè¿è¡æ¼æ¥ï¼æåå¾å°ä¼ªé è§é¢ãå æ¤ï¼ä¸å¯é¿å å°ä¼å¯¼è´ææ¾çéªçåä¸è¿ç»é¢é¨åºåãä¸ºäºææå¸§é´çå¨æä¸ä¸è´æ§ï¼Zheng Yç[43]æåºä¸ä¸ªç«¯å°ç«¯æ¡æ¶æ¥å¦ä¹ æ´ä¸è¬çæ¶é´ä¸ç¸å ³æ§ãå®å æ¬ä¸¤ä¸ªä¸»è¦çé¶æ®µï¼ç¬¬ä¸é¶æ®µæ¯ä¸ä¸ªå ¨æ¶æå·ç§¯ç½ç»(Fully Temporal Convolution Networkï¼FTCN) ï¼ä¸ºäºé¼å±æ¶ç©ºå·ç§¯ç½ç»å¦ä¹ æ¶é´ä¸çä¸ç¸å¹²æ§ï¼éæ°è®¾è®¡äºå·ç§¯ç®åï¼å°ææç©ºé´(é«åº¦åå®½åº¦) ç»´çæ ¸å¤§å°è®¾ç½®ä¸º1ï¼å¹¶å¨ä¸ç»´å·ç§¯ç®åä¸ä¿ææ¶é´ç»´çåå§æ ¸å¤§å°ï¼æå©äºæ¨¡åæåæ¶é´ç¹å¾ï¼ç¬¬äºé¶æ®µæ¯ä¸ä¸ªæ¶é´Transformerç½ç»ï¼å¨ä¼ªé è§é¢ä¸é¢é¨çç±çº¹æç£å¯è½ä¼éæ¸åºç°ææ¶å¤±ï¼å©ç¨Transformeræ²¿çæ¶é´ç»´åº¦æè·è¿ç§é¿æä¾èµå ³ç³»ãç¸æ¯ä¹åéè¦ä¾èµäºé¢è®ç»çæ£æµææ¯ï¼è¯¥æ¹æ³å¯ä»¥å¨æ²¡æä»»ä½äººå·¥æ æ³¨çæ åµä¸ï¼å®ä½åå¯è§åé¢é¨ä¼ªé è§é¢ä¸çæ¶é´ä¸ä¸è´æ§ï¼æ´å ·çµæ´»æ§åéç¨æ§ãä½ç±äºè¿ç§æ¶é´ä¸ç¸å¹²æ§å®¹æåå°åªå£°ãåç¼©çå ç´ çå¹²æ°ï¼ä»ç¶åå¨å¯¹åå¤ççé²æ£æ§é®é¢ãä¸ºè¿ä¸æ¥å©ç¨å±é¨ä½æ°´å¹³çº¿ç´¢åæ¶é´ä¿¡æ¯ï¼Guan Jç[44]æåºäºåºäºå±é¨åæ¶é´æç¥çæ·±åº¦ä¼ªé æ£æµæ¡æ¶(Local & Temporal aware Transformer-based Deepfake Detectionï¼LTTD) ãè¯¥æ¡æ¶éç¨äºä¸ä¸ªå±é¨å°å ¨å±çå¦ä¹ åè®®ï¼ç¹å«å ³æ³¨å±é¨åºåå æä»·å¼çæ¶é´ä¿¡æ¯ãå ·ä½å°è¯´ï¼ä½è æåºäºä¸ç§å±é¨Transformeråºåï¼æ¨¡æäºæéç©ºé´åºååºåçæ¶é´ä¸è´æ§ï¼å ¶ä¸ä½æ°´å¹³ä¿¡æ¯éè¿å¦ä¹ çä¸ç»´æ»¤æ³¢å¨çæµ å±åå±å¢å¼ºï¼å¹¶ä»¥å ¨å±å¯¹æ¯çæ¹å¼å®ç°æç»çåç±»ãè¯¥æ¹æ³èèå°äºå±é¨åºç°çæ¶é´å·®å¼ä¿¡æ¯ï¼è¿ç§æ½å¨çæ¶é´æ¨¡å¼åå°ç©ºé´å¹²æ°çå½±åè¾å°ï¼ä½¿å¾ä½çº§å»ºæ¨¡æ´å é²æ£ãèèå°æ·±åº¦ä¼ªé çæåå¯¹ææ§è®ç»çä¸æè¿æ¥ï¼è¯¥æ¹æ³å°ä¼éå°å¨ä½æ°´å¹³åæ¶é´ä¸ååå¢å¼ºçæ·±åº¦ä¼ªé è§é¢ï¼é¢æµçå¯ä¿¡åº¦æå¾ éªè¯ãæ¤å¤ï¼èèå°å·²æåºäºTransformer çæ·±åº¦ä¼ªé æ£æµç¼ºä¹å¯è§£éæ§ï¼Zhao Cç[45]æåºäºä¸ç§å ·å¤å¯è§£éæ§çåç¦»æ¶ç©ºèªæ³¨æåç½ç»(Interpretable Spatial-Temporal Video Transformerï¼ISTVT) ãå®å æ¬ä¸ç§æ°åè§£çæ¶ç©ºèªæ³¨æååä¸ç§èªåæ³æºå¶æ¥æè·ç©ºé´ä¼ªå½±åæ¶é´ä¸ä¸è´ï¼å¹¶éè¿ç¸å ³æ§ä¼ æç®æ³æ¥å¯è§åç©ºé´åæ¶é´ç»´åº¦çåºååºåï¼æä¾äºå¨Transformer å çæ¶é´ä¸ç©ºé´ç»´åº¦çå¯è§£éæ§ãè¯¥æ¹æ³æå©äºç ç©¶äººåçè§£Transformeræ¨¡åå¦ä½å¨æ¶ç©ºç»´åº¦ä¸æ£æµå°æ·±åº¦ä¼ªé è§é¢ï¼ä»èæ¹è¿æ£æµæ¨¡åçè®¾è®¡ãä½æ¯ï¼ç±äºè¯¥æ¹æ³ä¾§éäºå¦ä¹ çæçå¸§é´ä¸ä¸è´ï¼å¨å ç §æ¡ä»¶åå¤´é¨å§¿å¿ä¸è´çæ°æ®éä¸è¡¨ç°ä¸å¦FTCNç®æ³ãä¸ºäºæææ´è¯¦ç»çæ¶ç©ºä¿¡æ¯ï¼Yu Yç[46]æåºäºä¸ç§å ·æå±é¨æ¶ç©ºè§å¾åå ¨å±æ¶ç©ºè§å¾çå¤æ¶ç©ºè§å¾ç½ç»(Multiple Spatiotemporal Views Transformerï¼MSVT) ãé¦å ï¼ä¸ºäºå»ºç«å±é¨æ¶ç©ºè§å¾ï¼ä¸åäºç°æçç¨çéæ ·åå¸§æ¥æå»ºè¾å ¥åºåï¼ä½è ä½¿ç¨å±é¨è¿ç»æ¶é´è§å¾æ¥æè·å¨æä¸ä¸è´æ§ãæ¤å¤ï¼å°æ¯ç»å æåçå¸§ç¹å¾è¾å ¥æ¶é´è½¬æ¢å¨ï¼çæç»çº§æ¶ç©ºç¹å¾ãç¶åï¼éè¿å å ¥å ¨å±æ¶ç©ºè§å¾åç¹å¾èåæ¨¡åï¼å»ºç«å ¨å±æ¶ç©ºè§å¾ãæåï¼å©ç¨Transformeréæè¿äºå¤å±æ¬¡çç¹å¾ï¼ä»¥æææ´å¾®å¦åå ¨é¢çç¹å¾ãè¯¥æ¹æ³è®ºè¯äºå±é¨è¿ç»å¸§çä¸ä¸è´æ§å¨ä¼ªé äººè¸è§é¢æ£æµä¸æèµ·çéè¦ä½ç¨ã
2.2.2 åºäºè§è§åå¬è§è·¨æ¨¡æå ³èå¦ä¹ çæ£æµææ¯é¤äºä»è§é¢çç©ºåãé¢åãæ¶åçæåä¿¡æ¯ï¼é¨åç ç©¶äººåä¹å°è¯ç»åé³é¢ä¿¡æ¯ï¼ä»è·¨æ¨¡æçè§è§æ¥è¿è¡äººè¸æ·±åº¦ä¼ªé æ£æµãç¸æ¯äºCNNsï¼Transformerå ·ææ´å¼ºçè·¨æ¨¡æèåè½åï¼ä¸é²æ£æ§æ´å¥½ãç±äºTransformerçèªæ³¨æåæºå¶å¯ä»¥å°ä¸åæ¨¡æçä¿¡æ¯åå¨ä¸èµ·åæä¸ç»´é¿åºåï¼æååºåç¹å¾ï¼è®¡ç®ä¸ååºåçç¸å ³æ§ï¼ä»èæ´å¥½å°ææè·¨æ¨¡ææ°æ®ä¹é´çå å¨èç³»ãå æ¤ï¼å®è½å¤å¾å¥½å°å¤çå¤ç§ç±»åçæ°æ®ï¼å¦å¾åãé³é¢åææ¬çï¼å¹¶ä¸å¯¹äºä¸äºåªå£°æå¼å¸¸æ°æ®ä¹æå¾å¥½çå¤çè½åã
ç±äºç°å®åºæ¯ä¸çæ·±åº¦ä¼ªé è§é¢éå¸¸ç±è§è§åå¬è§ä¸¤ç§æ¨¡æç»åèæï¼éå¯¹è·¨æ¨¡ææ·±åº¦ä¼ªé çæ£æµæ¹æ³åå¤æ¨¡ææ·±åº¦ä¼ªé åºåï¼æä¸ºäºè¿æçç ç©¶çç¹æ¹åãä¹åçæ·±åº¦ä¼ªé æ£æµå·¥ä½å¤§å¤åªå ³æ³¨è§è§æå¬è§åæ¨¡æçæ£æµä»»å¡ï¼è´åäºæè·æ¨¡æå çä¼ªé ä¿¡æ¯ãåºäºè§è§åå¬è§è·¨æ¨¡æå ³èå¦ä¹ æ£æµçå ³é®ææ³æ¯å©ç¨åä¸è§é¢ä¸æåçè§é¢åé³é¢æ¨¡å¼ä¹é´çå ³èä¿¡æ¯ãç¸æ¯äºçå®è§é¢ï¼ç°æä¼ªé ææ¯é¾ä»¥ä¿æä¼ªé è§é¢å¨è§è§åå¬è§çèªç¶ä¸è´æ§ã
æ©æåºäºè·¨æ¨¡æçæ£æµæ¹æ³ä¸»è¦å©ç¨è¯é³å å®¹ææä¸ä¸è´çå´é¨å¨æåæ©å±è¾ å©è®ç»æ°æ®ãç¶èï¼è¿ç±»æ¹æ³å ³æ³¨çæ¯é¨åé¢é¨ç¹å¾ï¼æ æ³æ£æµè§å¬ååä¼ªé è§é¢ãä¸ºäºå æè¿ç§ç¼ºç¹ï¼åè·¨æ¨¡æçç©ç¹å¾å¹é ææ³çå¯åï¼Cheng Hç[47]è®¾è®¡äºè¯é³âé¢åå¹é æ£æµç®æ³(Voice-Face matching Detectionï¼VFD) ãé´äºåè§é¢ä¸å£°é³åäººè¸èåçèº«ä»½å¾å¾ä¸å¹é ï¼ä¸å£°é³åäººè¸å¨ä¸å®ç¨åº¦ä¸å ·æåè´¨æ§çç¹ç¹ãä½è é¦å å¨ä¸ä¸ªéç¨çè§å¬æ°æ®éå¯¹æ¨¡åè¿è¡è®ç»ï¼éç¨ViTèªæ³¨æåæºå¶æåä¸èº«ä»½ç¸å ³çè¯é³åäººè¸å¤æ¨¡æç¹å¾ï¼ç¶åå¯¹ä¸æ¸¸çæ·±åº¦ä¼ªé æ°æ®è¿è¡å¾®è°ãè¯¥æ¨¡åæ¯ç¬¬ä¸ä¸ªéè¿é¢é¨åé³é¢çå å¨ç¸å ³æ§æ¥è¿è¡æ·±åº¦ä¼ªé æ£æµï¼ä¸æ³¨äºå£°é³åäººè¸çä¸è¬å¹é ç®æ ï¼å¹¶ä¸å¯ä»¥å¿«éè¿ç§»å°åç§æ·±åº¦ä¼ªé æ°æ®éï¼èä¸æ¯å ³æ³¨æå®çäººè¸åºåãå ¶æ¬¡ï¼éç¨é¢è®ç»å¾®è°èå¼åè½»äºå¯¹è¾ å©æ°æ®çéæ±ãä½æ¯ï¼è¯¥æ¹æ³éå°è¸é¨å ç §ä¸è¶³æä¾§è¸çè§é¢æ£æµè½åæéï¼ä¸å¯¹ç¹å®çé¢é¨å±æ§ç¼è¾è§é¢æ£æµå¤±æãä¸ºæé«å¯¹ä¾§è¸è§é¢çæ£æµæ§è½ï¼Ilyas Hç[48]æåºåºäºSwin Transfomerçç«¯å°ç«¯æ£æµæ¨¡å(Audio-Visual Deefakes Detectionï¼AVFakeNet)ï¼å¹¶æä¾äºä¸ä¸ªåæ¶æçºµé³é¢åè§è§æ¨¡å¼æ°æ®éFakeAVCelebãè¯¥æ¨¡åå©ç¨Swin Transfomeræè·å ¨å±çé¿æä¾èµæ§åå¯éçå±æ¬¡ç¹å¾ï¼è½å¤æ£ç¡®å°åç±»ä¾§æå§¿å¿çé¢åãå ¶ä¸ï¼å¯éå±å¯¹ç½ç»ä½ç³»ç»æä¸çè¾å ¥å¾ååSwin Transfomerè¿è¡äºç²¾ç»ç¼ç ï¼æåäºå ·æå ¨å±æç¥å±æ§çç¹å¾å¾ï¼å»ºç«äºä¸åå¾åç¹å¾ä¹é´çå ³ç³»ï¼è½å¤æ£æµåºå ·ææç«¯ä¾§è¸çåè§é¢ãæ¤å¤ï¼ææä¾çé³é¢âè§é¢å¤æ¨¡ææ·±åº¦ä¼ªé æ£æµæ°æ®éï¼ä¿è¿äºåºäºè§å¬è§è·¨æ¨¡ææ£æµæ¨¡åçåå±ãä¸æ¤åæ¶ï¼Yang Wç[49]åæ ·å»ºç«äºä¸ä¸ªå¤æ¨¡ææ·±åº¦ä¼ªé æ£æµåºåDefakeAVMiTï¼å¹¶æåºå©ç¨è§å¬ä¸ä¸è´æ§çèåå¦ä¹ æ¹æ³(Audio-Visual Joint Learning for Detecting Deepfakeï¼AVoiD-DF) è¿è¡å¤æ¨¡æä¼ªé æ£æµãå ·ä½æ¥è¯´ï¼AVoiD-DFé¦å å¨æ¶ç©ºç¼ç å¨ä¸åµå ¥æ¶é´åºååç©ºé´ä½ç½®ä¿¡æ¯ï¼ç¶åè®¾è®¡äºå ·æäº¤åæ³¨ææºå¶çèåè§£ç å¨å¦ä¹ å å¨å ³ç³»ï¼æåéç¨ä¸ä¸ªè·¨æ¨¡æåç±»å¨æ¥æ£æµå ·ææ¨¡æé´åæ¨¡æå ä¸ä¸è´çæä½ãä¸ºæ¢ç´¢åºäºä¸¤ç§æ¨¡æä¹é´æ´å¸¸è§çä¸ä¸è´å ³ç³»ï¼Feng Cç[50]æåºä¸ç§åºäºå¼å¸¸æ£æµçæ¹æ³(Audio-Visual Anomaly Detectionï¼AVAD)ï¼è®ç»ä¸ä¸ªèªåå½Transformeræ¨¡åæ¥çæè§å¬ç¹å¾åºåï¼ä½¿ç¨äºä¸¤ä¸ªTransformerçè§£ç å¨å¦ä¹ è§é¢å¸§åé³é¢ä¹é´çæ¶é´åæ¥ç¹å¾åå¸ãè¯¥æ¹æ³ä»¥èªçç£çæ¹å¼æåçå®è§é¢ä¸çèªç¶è§å¬è§å¯¹åºï¼ç¶åä»¥å¦ä¹ å°ççå®å¯¹åºä½ä¸ºç®æ ï¼æå¯¼åç»è§å¬è§ä¸ä¸è´çæåï¼ææè§è§åé³é¢ä¿¡å·ä¹é´çç»å¾®ä¸ä¸è´ï¼å¹¶ä¸åç¬ä½¿ç¨çå®çãæªæ è®°çæ°æ®è¿è¡è®ç»ãä½æ¯ï¼è¯¥æ¨¡åæ æ³æ£æµå´é¨è¿å¨åé³é¢ä¹é´ä¿æç¸å¯¹ä¸è´çä¼ªé è§é¢ï¼æ¯å¦åªæ¹åè¯´è¯è é¢é¨å¤è§èå´çè¿å¨ä¿æä¸åãç±äºä¸åæ¨¡æåå¨å·®è·ï¼å ¶åºæçè§å¬è§å ³ç³»é¾ä»¥æåï¼ä¸åè§å¬è§ååä¼ªé æä½å½±åï¼å¯¼è´ä¸è¿°èªçç£æ¹æ³çè¾ å©æ§è½æéï¼Yang Yç[51]æåºäºé¢æµæ§è§è§ä¸é³é¢å¯¹é½èªçç£çå¤æ¨¡ææ·±åº¦ä¼ªé æ£æµæ¹æ³(Predictive Visual-Audio Alignment Seaf-Supervision for Multimodal Deepfake Detectionï¼PVASS-MDD)ãå®ç±é¢æµæ§è§å¬è§å¯¹é½èªçç£è¾ å©é¶æ®µPVASSåå¤æ¨¡ææ£æµé¶æ®µMDDç»æãå¨çå®è§é¢çPVASSè¾ å©é¶æ®µï¼è®¾è®¡äºä¸ä¸ªåºäºSwin Transfomerçä¸æ¯è·¯ç½ç»ï¼å°ä¸¤ä¸ªå¢å¼ºçè§è§è§å¾ä¸ç¸åºçé³é¢çº¿ç´¢å ³èèµ·æ¥ï¼ä»èåºäºäº¤åè§å¾å¦ä¹ æ¢ç´¢å¸¸è§çè§å¬è§å¯¹åºãå ¶æ¬¡ï¼å¼å ¥äºä¸ç§æ°çè·¨æ¨¡æé¢æµå¯¹é½æ¨¡åæ¥æ¶é¤è§å¬è§é´éï¼ä»¥æä¾åºæçè§å¬è§å¯¹åºãå¨MDDé¶æ®µï¼æåºäºè¾ å©æå¤±ï¼å©ç¨å»ç»çPVASSç½ç»æ¥å¯¹é½çå®è§é¢çè§å¬è§ç¹å¾ï¼ä»¥æ´å¥½å°å¸®å©å¤æ¨¡ææ·±åº¦ä¼ªé æ£æµå¨æè·ç»å¾®çè§å¬è§ä¸ä¸è´æ§ï¼æé«æ³åæ§è½ã
è½ç¶ï¼åºäºè§è§åå¬è§è·¨æ¨¡æçæ£æµæ¹æ³å¾å°äºä¼å¤ç ç©¶è çéçï¼ä½è¿ç±»è·¨æ¨¡æçæ¹æ³éè¦ä¼ªé è§é¢ä¸å å«é³é¢ä¿¡æ¯ï¼èå½åçä¸»æµæ°æ®éå¾å¾åªå å«è§è§å å®¹ï¼åªæå°é¨åæ°æ®éå å«é³é¢å å®¹ï¼å æ¤è¿ç±»æ¹æ³çåå±ä¹åå°äºä¸å®å¶çº¦ã
3 æ¨¡åè¯æµç»æ 3.1 å¸¸ç¨å ¬å¼æ°æ®éä¸ºäºéä½æ·±åº¦ä¼ªé äººè¸å¾åä¸è§é¢æå¸¦æ¥çè´é¢å½±åï¼ç»ç¸åºçæ£æµææ¯å¥ å®æ°æ®å¯¹æåºç¡ï¼å·²æä¸äºå¦è ç»ç»äºä¸æ¹äººè¸æ·±åº¦ä¼ªé æ°æ®éï¼ç¨äºè®ç»ä»¥åè¯ä¼°æ£æµæ¨¡åçæ§è½ãæ ¹æ®æ°æ®éçè§è§è´¨éåè§æ¨¡ï¼ç°æå¸¸ç¨çæ·±åº¦ä¼ªé å ¬å¼æ°æ®éå¯åä¸ºä¸ä»£ï¼å¦è¡¨2æç¤ºãç¬¬ä¸ä»£æ°æ®éå æ¬FaceForensics++[2]ãDeepfakeDetection[52]ãDFDC-preview[53]ãCeleb-DF-v1[54]ãCeleb-DF-v2[55]ãWildDeepfake[56]ï¼ç¬¬äºä»£æ°æ®éå æ¬DFDC[57]ãDeepForensics-1.0[58]ãVox-Deepfake[59]ãFFIW-10K[60]ãForgeryNet[61]ï¼ç¬¬ä¸ä»£æ°æ®éå æ¬KoDF[62]ãFakeAVCeleb[48]ãLAVDF[63]ãDefakeAVMiT[49]ã
æ£æµæ¨¡åçæ§è½è¯ä»·ææ ä¸»è¦å æ¬åç¡®ç(Accuracyï¼ACC) åæ¥åè æä½ç¹å¾æ²çº¿(Receiver Operating Characteristic curveï¼ROC) ä¸çé¢ç§¯(Area Under Curveï¼AUC) ãæ·±åº¦ä¼ªé äººåè§é¢æ£æµé®é¢ä¹å¯ä»¥çææ¯ä¸ä¸ªäºåç±»é®é¢ï¼å³æ ·æ¬åå¨æ£è´ä¸¤ä¸ªæ ç¾ãç±äºåç¡®çACCå¾å¾ä¼åå°æ£è´æ ·æ¬æ°éåå¸çå½±åï¼å æ¤ï¼å¨è¿è¡è·¨æ°æ®éæµè¯æ¶ï¼ä¸»è¦éç¨AUCä½ä¸ºè¯ä»·ææ ãAUCè¡¨ç¤ºROCæ²çº¿ä¸çé¢ç§¯ï¼ä¸»è¦è¡¨ç¤ºé¢æµç»æä¸æ£æ ·æ¬æå¨è´æ ·æ¬åé¢çæ¦çï¼å¼è¶æ¥è¿äº1åç±»ææè¶å¥½ãAUCä¸ä¼åå°æ£è´æ ·æ¬æ°éåå¸çå½±åï¼è½å¤å®¢è§å°è¡¡éæ¨¡ååç±»ææçå¥½åï¼å°¤å ¶éç¨äºäºåç±»çé®é¢ã
ä¸ºäºè¯ä¼°åºäºè§è§æ¨¡æçäººè¸ä¼ªé æ£æµå¨å¨è·¨æ°æ®éä¸çæ³åè½åï¼æå»ºäºä¸ä¸ªè·¨æ°æ®éæµè¯åè®®ãå ·ä½å°è¯´ï¼åå«æ¶éæ´çäº8ä¸ªåºäºCNNsæ¨¡åå8ä¸ªåºäºTransformeræ¨¡åçä»£è¡¨æ§æ£æµç®æ³ï¼ç»ä¸å¨FaceForensics++è®ç»éä¸çææ4ç±»ä¼ªé æ°æ®ä¸è¿è¡è®ç»ï¼å¹¶å¨3ä¸ªæªç¥æ°æ®éä¸è¿è¡æµè¯ï¼å æ¬Celeb-DF-v2ãDFDCåDeepForensics-1.0ãå ·ä½ç»æå¦è¡¨3æç¤ºãä»å®éªç»æå¯ä»¥çåºï¼å¨æµè¯éCeleb-DF-v2ä¸ï¼åºäºTransformeræ¨¡åçLTTDç®æ³AUCè¾¾å°äºæé«AUCå¼89.3%ï¼å ¶æ¬¡æ¯MSVTç®æ³88.81%ï¼å¨æµè¯éDFDCä¸ï¼åºäºTransformeræ¨¡åçLTTDç®æ³AUCè¾¾å°äºæé«AUCå¼80.3%ï¼å ¶æ¬¡æ¯MSVTç®æ³76.79%ï¼å¨æµè¯éDeepForensics-1.0ä¸ï¼åºäºCNNsæ¨¡åçPCL+I2Gç®æ³AUCè¾¾å°äºæé«AUCå¼99.4%ï¼ä½æ¯è¯¥ç®æ³å¨å ¶ä»ä¸¤ä¸ªæµè¯éæ§è½è¾ä½ï¼ä¸å¤ä¸ªåºäºTransformeræ¨¡åçç®æ³AUCå¼ä¹é½è¶ è¿äº98%ãæ»ä½æ¥çï¼åºäºTransformeræ¨¡åçæ£æµç®æ³æ³åæ§è½æ®éé«äºåºäºCNNsæ¨¡åçç®æ³ãç®åæ¥çï¼åºäºTransformeræ¨¡åçLTTDç®æ³æ´ä½ä¸å ·ææä¼çæ£æµæ§è½ï¼è¿ä¸»è¦å¾çäºææåºçå±é¨Transformeræè·å±é¨åºåå æä»·å¼çæ¶é´å·®å¼ä¿¡æ¯ï¼åç©ºé´å¹²æ°è¾å°ã
ä¸ºäºè¯ä¼°åºäºè§è§åå¬è§è·¨æ¨¡æçäººè¸ä¼ªé æ£æµå¨çæ³åè½åï¼æ¶éæ´çäº3ä¸ªåºäºCNNsæ¨¡åå3ä¸ªåºäºTransformeræ¨¡åçä»£è¡¨æ§æ£æµç®æ³ï¼å©ç¨3ä¸ªå¤æ¨¡æå ¬å¼æ°æ®éDFDCãFakeAVCelebåDefakeAVMiTè¿è¡è·¨æ°æ®éæ¯è¾ãéåå ¶ä¸ä¸ä¸ªæ°æ®éè¿è¡è®ç»ï¼å ¶ä»2ä¸ªæ°æ®éæµè¯ãå ·ä½ç»æå¦è¡¨4æç¤ºãä»å®éªç»æå¯ä»¥çåºï¼å¨ä¸åè·¨æ°æ®éæµè¯æ¡ä»¶ä¸ï¼åºäºTransformeræ¨¡åçè·¨æ¨¡ææ£æµç®æ³çæ³åæ§è½é½ä¼äºåºäºCNNsæ¨¡åãå ¶ä¸ï¼åºäºTransformeræ¨¡åçPVASS-MDDç®æ³åå¾äºæä¼çæ£æµæ§è½ï¼è¿ä¸»è¦å¾çäºéç¨åºäºSwin Transfomerçèªçç£ç½ç»å¦ä¹ è§å¬è§å¯¹åºå ³ç³»ï¼ä»¥åå¼å ¥äºè·¨æ¨¡æé¢æµå¯¹é½æ¨¡åæ¥æ¶é¤è§å¬è§é´éï¼æ´å¥½å°æè·ç»å¾®çè§å¬è§ä¸ä¸è´æ§ã
æ¬æéç¹æ»ç»åæäºTransformeræ¨¡åå¨äººè¸æ·±åº¦ä¼ªé æ£æµå¨æ§è½æåä¸åæ¥çä½ç¨åææ¯ç¹ç¹ãä¸»è¦å æ¬åºäºè§è§æ¨¡æååºäºè§å¬è§è·¨æ¨¡æä¸¤ç±»ï¼å¨åºäºè§è§æ¨¡æçæ£æµææ¯ä¸ï¼Transformerçèªæ³¨æåæºå¶åæ¥å ¶å ¨å±å ³ç³»åé¿è·ç¦»ç¹å¾ä¾èµå ³ç³»å»ºæ¨¡è½åï¼æ´å¥½å°æè·å°ä¼ªé äººè¸å¾ååºåä¸å ¶ä¸ä¸æåºå«çç©ºé´ä¸ä¸è´ä¿¡æ¯ï¼ä»¥åè§é¢å¸§ä¹é´çæ¶é´è¿ç»æ§ï¼ä»¥æ¹åæ·±åº¦ä¼ªé æ£æµå¨è·¨åç¼©ãè·¨åºæ£æµæ¶çææï¼åºäºè§å¬è§è·¨æ¨¡æèåå¦ä¹ çæ£æµææ¯ä¸ï¼Transformeråæ¥å ¶æ´ä¼å¼çè·¨æ¨¡æèåè½åï¼è½æ´å¥½å°ææè·¨æ¨¡ææ°æ®ä¹é´çå å¨èç³»ï¼æææ·±åº¦ä¼ªé è§é¢å¨ä¸åæ¨¡æé´çä¸ä¸è´å ³ç³»ã
ç±äºå¦Stable Diffusionçè§è§çææ¨¡åçå¿«éåå±ï¼é«ä¿çåº¦çäººè¸å¾çå¯ä»¥èªå¨åå°ä¼ªé ï¼èä¸ä¸äºææ¯å¼å§è¿è¡è§å¬ååä¼ªé ï¼å¶é è¶æ¥è¶ä¸¥éçDeepFakeé®é¢ãTransformerç±äºå ¶å ·å¤å ¨å±äº¤äºè½ååå¤§æ¨¡åé¢è®ç»è½åï¼æå©äºäººè¸æ·±åº¦ä¼ªé æ£æµå¨è·åæ´éç¨çç¹å¾åæ°æ®èåè½åï¼æææåå ¶æ£æµå¨çæ³åè½åï¼æææä¸ºæªæ¥çä¸»æµæ¨¡åä¹ä¸ãä½ä¹é¢ä¸´ä¸äºææï¼å æ¬ï¼
(1) Transformeræ¨¡åéå¸¸éè¦å¤§è§æ¨¡çæ°æ®è¿è¡è®ç»ï¼ä»¥ä¾¿è·å¾å¼ºå¤§çæ³åè½åãå¨æ·±åº¦ä¼ªé æ£æµé¢åï¼è·å¾å¤§è§æ¨¡çå¸¦ææ ç¾çæ·±åº¦ä¼ªé åçå®æ°æ®éå¯è½ç¸å¯¹å°é¾ï¼å æ¤æ°æ®æ¶éåæ æ³¨æä¸ºä¸ä¸ªææã
(2) Transformeræ¨¡åéå¸¸éè¦å¤§éçè®¡ç®èµæºæ¥è¿è¡è®ç»åæ¨çï¼å°¤å ¶æ¯å¤§åçé¢è®ç»æ¨¡åãè¿å¯è½å¯¹ç¡¬ä»¶åè½æºèµæºäº§çååï¼ä½¿å¾é¨ç½²ææ¬é«æã
(3) æ·±åº¦ä¼ªé å¶ä½è å¯è½ä¼å°è¯å¯¹ææ·±åº¦ä¼ªé æ£æµï¼éè¿å¯¹ææ§æå·§æ¥çææ´å ·è¿·ææ§çæ·±åº¦ä¼ªé è§é¢ãè½ç¶Transformeræ¨¡åç¸å¯¹äºCNNsæ¨¡åæ´è½æµæå¯¹ææ§æ»å»ï¼ä½ä»ç¶éè¦éåé¢å¤çå¯¹ææ§è®ç»åé²å¾¡æºå¶æ¥åºå¯¹è¿ä¸ææã
(4) è½ç¶Transformeræ¨¡åå¨å¾å¤ä»»å¡ä¸è¡¨ç°åºè²ï¼ä½å¨æäºç¹å®ä»»å¡ææ°æ®éä¸ï¼å®ä»¬å¯è½æ æ³åå¾æä½³æ§è½ãè¿éè¦æ´å¤çç ç©¶åè°ä¼ï¼ä»¥éåºæ·±åº¦æ£æµçç¹å®éæ±ã
| [1] | |
| [2] | 
									 
										ROSSLER A, COZZOLINO D, VERDOLIVA L, et al. Faceforensics++: learning to detect manipulated facial images[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. Seoul, South Korea: IEEE, 2019: 1-11. 
										
																 | 
| [3] | 
									 
										QIAN Y, YIN G, SHENG L, et al. Thinking in frequency: face forgery detection by mining frequency-aware clues[C]//European Conference on Computer Vision. Online: Springer, 2020: 86-103. 
										
																 | 
| [4] | 
									 
										MASI I, KILLEKAR A, MASCARENHAS R M, et al. Two-branch recurrent network for isolating deepfakes in videos[C] //European Conference on Computer Vision. Online: Springer, 2020: 667-684. 
										
																 | 
| [5] | 
									 
										LI L, BAO J, ZHANG T, et al. Face x-ray for more general face forgery detection[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. Seattle, USA: IEEE, 2020: 5001-5010. 
										
																 | 
| [6] | 
									 
										ZHAO H, ZHOU W, CHEN D, et al. Multi-attentional deepfake detection[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. Online: IEEE, 2021: 2185-2194. 
										
																 | 
| [7] | 
									 
										LIU H, LI X, ZHOU W, et al. Spatial-phase shallow learning: rethinking face forgery detection in frequency domain[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. Online: IEEE, 2021: 772-781. 
										
																 | 
| [8] | 
									 
										ZHAO T, XU X, XU M, et al. Learning self-consistency for deepfake detection[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. Montreal, Canada: IEEE, 2021: 15023-15033. 
										
																 | 
| [9] | 
									 
										HALIASSOS A, VOUGIOUKAS K, PETRIDIS S, et al. Lips don't lie: a generalisable and robust approach to face forgery detection[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. Online: IEEE, 2021: 5039-5049. 
										
																 | 
| [10] | 
									 
										CHUGH K, GUPTA P, DHALL A, et al. Not made for each other-audio-visual dissonance-based deepfake detection and localization[C]//Proceedings of the 28th ACM International Conference on Multimedia. Seattle , USA: ACM, 2020: 439-447. 
										
																 | 
| [11] | 
									 
										MITTAL T, BHATTACHARYA U, CHANDRA R, et al. Emotions don't lie: an audio-visual deepfake detection method using affective cues[C]//Proceedings of the 28th ACM International Conference on Multimedia. Seattle , USA : ACM, 2020: 2823-2832. 
										
																 | 
| [12] | 
									 
										ZHOU Y, LIM S N. Joint audio-visual deepfake detection[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. Montreal, Canada: IEEE, 2021: 14800-14809. 
										
																 | 
| [13] | |
| [14] | 
																												PENG Z, GUO Z, HUANG W, et al. Conformer: local features coupling global representations for recognition and detection[J].
												IEEE Transactions on Pattern Analysis and Machine Intelligence, 2023, 45(8): 9454-9468.
												DOI: 10.1109/TPAMI.2023.3243048.													 | 
| [15] | |
| [16] | 
									 
										VASWANI A, SHAZEER N, PARMAR N, et al. Attention is all you need[C]//31st Conference on Neural Information Processing Systems. Long Beach, USA: MIT Press, 2017: 5998â6008. 
										
																 | 
| [17] | 
									 
										DOSOVITSKIY A, BEYER L, KOLESNIKOV A, et al. An image is worth 16Ã16 words: transformers for image recognition at scale[C]//Proceedings of the 9th International Conference on Learning Representations. Online: ACM, 2021: 1-6. 
										
																 | 
| [18] | 
									 
										LIU Z, LIN Y, CAO Y, et al. Swin transformer: hierarchical vision transformer using shifted windows[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. Montreal, Canada: IEEE, 2021: 10012-10022. 
										
																 | 
| [19] | 
									 
										CHEN, RICHARD C F, FAN Q, et. al. Crossvit: cross-attention multi-scale vision transformer for image classification[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. Montreal, Canada: IEEE, 2021: 357-366. 
										
																 | 
| [20] | |
| [21] | 
									 
										KORSHUNOVA I, SHI W, DAMBRE J, et al. Fast face-swap using convolutional neural networks[C]//Proceedings of the IEEE International Conference on Computer Vision. Venice, Italy: IEEE, 2017: 3677-3685. 
										
																 | 
| [22] | 
									 
										LI L, BAO J, YANG H, et al. Advancing high fidelity identity swapping for forgery detection[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. Seattle, USA: IEEE, 2020: 5074-5083. 
										
																 | 
| [23] | 
									 
										CHEN R, CHEN X, NI B, et al. Simswap: an efficient framework for high fidelity face swapping[C]//Proceedings of the 28th ACM International Conference on Multimedia. Seattle, USA: ACM, 2020: 2003-2011. 
										
																 | 
| [24] | 
									 
										THIES J, ZOLLHOFER M, STAMMINGER M, et al. Face2face: real-time face capture and reenactment of rgb videos[C]//Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. Las Vegas, USA: IEEE, 2016: 2387-2395. 
										
																 | 
| [25] | 
									 
										NIRKIN Y, KELLER Y, HASSNER T. FSGAN: subject agnostic face swapping and reenactment[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. Seoul, Korea (South) : IEEE, 2019: 7184-7193. 
										
																 | 
| [26] | 
									æ±å¯, æç, å¼ å½¤ç. è§è§Transformerå¨ä½çº§è§è§é¢åçç ç©¶ç»¼è¿°[J/OL]. è®¡ç®æºå·¥ç¨ä¸åºç¨.https://link.cnki.net/urlid/11.2127.TP.20230817.1249.004 
											 ZHU K, LI L, ZHANG T, et al. A survey of vision transformer in low-level computer vision[J/OL]. Computer Engineering and Applications.https://link.cnki.net/urlid/11.2127.TP.20230817.1249.004 | 
| [27] | 
									 
										TOUVRON H, CORD M, DOUZE M, et al. Training data-efficient image transformers & distillation through attention[C]//International Conference on Machine Learning. Online: PMLR, 2021: 10347-10357. 
										
																 | 
| [28] | 
									 
										WU H, XIAO B, CODELLA N, et al. CvT: Introducing convolutions to vision transformers[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. Montreal, Canada: IEEE, 2021: 22-31. 
										
																 | 
| [29] | 
									 
										D'ASCOLI S, TOUVRON H, LEAVITT M L, et al. Convit: Improving vision transformers with soft convolutional inductive biases[C]//Proceedings of the 38th International Conference on Machine Learning. Online: ACM, 2021: 2286-2296. 
										
																 | 
| [30] | 
																												CHU X, TIAN Z, WANG Y, et al. Twins: revisiting the design of spatial attention in vision transformers[J].
												Advances in Neural Information Processing Systems, 2021, 34: 9355-9366.
																									 | 
| [31] | 
									 
										CHEN R, PANDA R, FAN Q. RegionViT: regional-to-local attention for vision transformers[C]//International Conference on Learning Representations. Online: ACM , 2022. 
										
																 | 
| [32] | 
									 
										WANG W, XIE E, LI X, et al. Pyramid vision transformer: a versatile backbone for dense prediction without convolutions[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. Montreal, Canada: IEEE, 2021: 568-578. 
										
																 | 
| [33] | 
									 
										YUAN L, CHEN Y, WANG T, et al. Tokens-to-token ViT: Training vision transformers from scratch on imagenet[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. Montreal, Canada: IEEE, 2021: 558-567. 
										
																 | 
| [34] | |
| [35] | 
									 
										TOUVRON H, CORD M, SABLAYROLLES A, et al. Going deeper with image transformers[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. Montreal, Canada: IEEE, 2021: 32-42. 
										
																 | 
| [36] | 
									 
										DONG X, BAO J, CHEN D, et al. Protecting celebrities from deepfake with identity consistency transformer[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. New Orleans, USA: IEEE, 2022: 9468-9478. 
										
																 | 
| [37] | 
																												CHEN H, LIN Y, LI B, et al. Learning features of intra-consistency and inter-diversity: keys toward generalizable deepfake detection[J].
												IEEE Transactions on Circuits and Systems for Video Technology, 2023, 33(3): 1468-1480.
												DOI: 10.1109/TCSVT.2022.3209336.													 | 
| [38] | 
									 
										WANG J, WU Z, OUYANG W, et al. M2tr: multi-modal multi-scale transformers for deepfake detection[C]//Proceedings of the 2022 International Conference on Multimedia Retrieval. Newark, USA: ACM, 2022: 615-623. 
										
																 | 
| [39] | |
| [40] | 
																												MIAO C, TAN Z, CHU Q, et al. Hierarchical frequency-assisted interactive networks for face manipulation detection[J].
												IEEE Transactions on Information Forensics and Security, 2022, 17: 3008-3021.
												DOI: 10.1109/TIFS.2022.3198275.													 | 
| [41] | 
																												MIAO C, TAN Z, CHU Q, et al. F2Trans: high-frequency fine-grained transformer for face forgery detection[J].
												IEEE Transactions on Information Forensics and Security, 2023, 18: 1039-1051.
												DOI: 10.1109/TIFS.2022.3233774.													 | 
| [42] | |
| [43] | 
									 
										ZHENG Y, BAO J, CHEN D, et al. Exploring temporal coherence for more general video face forgery detection[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. Montreal, Canada: IEEE, 2021: 15044-15054. 
										
																 | 
| [44] | 
																												GUAN J, ZHOU H, HONG Z, et al. Delving into sequential patches for deepfake detection[J].
												Advances in Neural Information Processing Systems, 2022, 35: 4517-4530.
																									 | 
| [45] | 
																												ZHAO C, WANG C, HU G, et al. ISTVT: interpretable spatial-temporal video transformer for deepfake detection[J].
												IEEE Transactions on Information Forensics and Security, 2023, 18: 1335-1348.
												DOI: 10.1109/TIFS.2023.3239223.													 | 
| [46] | 
																												YU Y, NI R, ZHAO Y, et al. MSVT: multiple spatiotemporal views transformer for deepfake video detection[J].
												IEEE Transactions on Circuits and Systems for Video Technology, 2023, 33(9): 4462-4471.
												DOI: 10.1109/TCSVT.2023.3281448.													 | 
| [47] | |
| [48] | 
																												ILYAS H, JAVED A, MALIK K M. AVFakeNet: A unified end-to-end dense swin transformer deep learning model for audio-visual deepfakes detection[J].
												Applied Soft Computing, 2023, 136: 110124.
												DOI: 10.1016/j.asoc.2023.110124.													 | 
| [49] | 
																												YANG W, ZHOU X, CHEN Z, et al. AVoiD-DF: audio-visual joint learning for detecting deepfake[J].
												IEEE Transactions on Information Forensics and Security, 2023, 18: 2015-2029.
												DOI: 10.1109/TIFS.2023.3262148.													 | 
| [50] | 
									 
										FENG C, CHEN Z, OWENS A. Self-supervised video forensics by audio-visual anomaly detection[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. Vancouver, Canada: IEEE, 2023: 10491-10503. 
										
																 | 
| [51] | 
									 
										YU Y, LIU X, NI R, et al. PVASS-MDD: predictive visual-audio alignment self-supervision for multimodal deepfake detection[J]. IEEE Transactions on Circuits and Systems for Video Technology.https://ieeexplore.ieee.org/document/10233898 
										
																 | 
| [52] | |
| [53] | |
| [54] | 
									 
										LI Y, YANG X, SUN P, et al. Celeb-DF: a large-scale challenging dataset for deepfake forensics[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. Seattle, USA : IEEE, 2020: 3207-3216. 
										
																 | 
| [55] | |
| [56] | 
									 
										ZI B, CHANG M, CHEN J, et al. WildDeepfake: a challenging real-world dataset for deepfake detection[C]//Proceedings of the 28th ACM International Conference on Multimedia. Seattle, USA: ACM, 2020: 2382-2390. 
										
																 | 
| [57] | |
| [58] | 
									 
										JIANG L, LI R, WU W, et al. Deeperforensics-1.0: a large-scale dataset for real-world face forgery detection[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. Seattle, USA: IEEE, 2020: 2889-2898. 
										
																 | 
| [59] | |
| [60] | 
									 
										ZHOU T, WANG W, LIANG Z, et al. Face forensics in the wild[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. Online: IEEE, 2021: 5778-5788. 
										
																 | 
| [61] | 
									 
										HE Y, GAN B, CHEN S, et al. ForgeryNet: a versatile benchmark for comprehensive forgery analysis[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. Online: IEEE, 2021: 4360-4369. 
										
																 | 
| [62] | 
									 
										KWON P, YOU J, NAM G, et al. KoDF: a large-scale Korean deepfake detection dataset[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. Montreal, Canada: IEEE, 2021: 10744-10753. 
										
																 | 
| [63] | 
									 
										CAI Z, STEFANOV K, DHALL A, et al. Do you really mean that? content driven audio-visual deepfake dataset and multimodal method for temporal forgery localization[C]//2022 International Conference on Digital Image Computing: Techniques and Applications. Online: IEEE, 2022: 1-10. 
										
																 | 
| [64] | |
| [65] |

---
*检索时间: 2026-07-24 20:49:29*
*搜索来源: DuckDuckGo*
