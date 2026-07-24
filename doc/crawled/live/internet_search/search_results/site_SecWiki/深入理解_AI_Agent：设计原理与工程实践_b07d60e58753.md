# 深入理解 AI Agent：设计原理与工程实践

### 来源信息
- **URL**: https://github.com/bojieli/ai-agent-book
- **来源站点**: SecWiki
- **页面抓取**: 成功

### 页面正文
中文 ← 当前 · 正体中文 · English · Русский · Tiếng Việt · தமிழ் · 日本語
📥 下载 PDF / EPUB（推荐）— 推荐使用 PDF / EPUB 离线阅读，排版最佳；也可在线阅读（支持多语言切换、章节折叠、全文搜索，每次推送自动更新）。
Agent = LLM + 上下文 + 工具——本书围绕这个核心公式，用 10 章把 AI Agent 从原理讲到工程实战。全书正文、配图、92 个配套实验全部开源，欢迎亲手把实验跑一遍。
| 📚 10 章 正文，从基础到生产 | 📂 92 个 配套项目（70+ 可独立运行） | 🌐 7 种 语言：中 / 正体中文 / 英 / 俄 / 泰米尔 / 越 / 日 | 
|---|
📥 离线下载（推荐，全书正文，开源免费）。以下链接始终指向 main 分支的最新构建；固定版本见 Releases：
- 中文（原版）：PDF · EPUB
- 正体中文（社区翻译，by @tigercosmos）：PDF · EPUB
- 英文（社区翻译，by @nsdevaraj）：PDF · EPUB
- 俄语（社区翻译，by @ui99ru）：PDF · EPUB
- 泰米尔语（社区翻译，by @nsdevaraj）：PDF · EPUB
- 越南语（社区翻译，by @toanalien）：PDF · EPUB
- 日语（社区翻译，by @eltociear）：PDF · EPUB
🌐 也可在线阅读 — 支持多语言切换、章节折叠、全文搜索、配套实验直达，每次 main 分支推送后自动重新构建。
中文正文源码位于 book/；正体中文/英文/俄语/泰米尔/越南语/日语版本为社区贡献（可能滞后于中文原版），分别位于 book-zhtw/、book-en/、book-ru/、book-ta/、book-vi/、book-ja/。
可使用统一的构建脚本生成中文、正体中文、英文、俄语、泰米尔语、越南语和日语 EPUB 3 电子书。请参阅 EPUB 构建说明。
🔧 想自行编译 PDF？（需 pandoc / xelatex / ElegantBook）
- 
正文源码： book/introduction.md（引言）、book/chapter1.md~book/chapter10.md（第一至第十章）、book/afterword.md（后记）
- 
编译：安装 pandoc、xelatex、ElegantBook 文档类与相关字体后，运行 cd book && bash build_pdf.sh 图表由 book/gen_*_figs.py生成、存于book/images/，排版细节见book/preamble.tex与book/*.lua。
全书围绕核心公式 Agent = LLM + 上下文 + 工具 展开，十章层层递进：
| 章 | 主题 | 一句话核心 | 正文 | 代码 | 
|---|---|---|---|---|
| 1 | 🚀 Agent 基础知识 | Agent = LLM + 上下文 + 工具；Harness 工程才是竞争力 | 读 | 4 | 
| 2 | 🎯 上下文工程 | 上下文决定能力上限：KV Cache、提示工程、Agent Skills、上下文压缩 | 读 | 9 | 
| 3 | 📚 用户记忆和知识库 | 跨会话记住用户、接入外部知识：用户记忆、RAG、结构化索引、知识图谱 | 读 | 13 | 
| 4 | 🛠️ 工具 | 工具是 Agent 的双手：MCP 协议、感知/执行/协作三类工具、事件驱动异步 Agent、主动工具发现 | 读 | 7 | 
| 5 | 💻 Coding Agent 与代码生成 | 代码是「能创造新工具的工具」，生产级 Coding Agent 全景 | 读 | 12 | 
| 6 | 🎯 Agent 的评估 | 把表现变成可比较信号：评估环境、指标、统计显著性、评估驱动选型 | 读 | 11 | 
| 7 | 🧠 模型后训练 | 预训练/SFT/RL 三阶段：何时选 SFT、何时选 RL，工具调用内化、样本效率 | 读 | 16 | 
| 8 | 🔄 Agent 的持续进化 | 从运行轨迹获得学习信号，更新知识、指令、程序与参数 | 读 | 8 | 
| 9 | 🎙️ 多模态与实时交互 | 从文本扩展到语音、GUI、物理世界：语音三范式、Computer Use、机器人 | 读 | 7 | 
| 10 | 🤝 多 Agent 协作 | 群体智能高于个体：协作框架、上下文共享/隔离、涌现的「Agent 社会」 | 读 | 7 | 
💡 读 = 在 GitHub 网页直接读章节正文（markdown）；N = 该章配套项目数，点击查看代码。项目类型说明（✅ 可运行 / 📖 复现 / 🚧 设计）见各章 README。
📚 如何高效阅读本书？详见 学习建议（核心理念、学习路径、难度分级、实践建议）。
建议申请下面几个平台的 API Key 方便学习。模型选型可参考 这篇指南。
| 平台 | 链接 | 特色 | 访问节点 | 
|---|---|---|---|
| Kimi（月之暗面） | https://platform.moonshot.cn/ | Kimi 系列，Coding、Agent 能力强 | 中国大陆 | 
| 智谱 GLM | https://open.bigmodel.cn/ | GLM-5.2 等，Coding、Agent 能力强 | 中国大陆 | 
| Siliconflow | https://siliconflow.cn/ | 各种开源模型（DeepSeek、Qwen 等），中国大陆访问速度快 | 中国大陆 | 
| DeepSeek | https://platform.deepseek.com/ | DeepSeek 官方 API | 全球 + 中国大陆 | 
| Krill AI | www.krill-ai.com | 一站式访问全球及国内主流模型（OpenAI、Claude、Gemini、Grok、Kimi、GLM、DeepSeek、Qwen、Minimax） | 全球 + 中国大陆 | 
| OpenRouter | https://openrouter.ai/ | 一站式访问全球及国内主流模型（GPT、Claude、Gemini、Kimi、GLM、DeepSeek、Qwen 等） | 全球 | 
感谢 Krill AI 赞助本项目！Krill 提供 GPT / Claude / Gemini / 多款国产模型的官方稳定极速 API 中转服务，支持企业级定制、报销开票、7×16h 专属技术支持，更有独家适配的 WebSocket 连接方式，畅享极速首字速度。
Krill 为本书读者提供特别优惠：使用此链接注册并在充值时填写优惠码「ai-agent-book」，首次购买 Codex 套餐可享 77 折优惠！
第 6、7、9、10 章的评测基准、训练框架、机器人平台等 19 个外部仓库未内置（出于体积与版权），需要自行克隆到对应目录。
🔧 展开克隆命令（共 19 个外部仓库）
# 第 6 章 · 评测基准
git clone https://github.com/google-research/android_world.git  chapter6/android_world
git clone https://huggingface.co/datasets/gaia-benchmark/GAIA  chapter6/GAIA
git clone https://github.com/xlang-ai/OSWorld.git  chapter6/OSWorld
git clone https://github.com/SWE-bench/SWE-bench.git  chapter6/SWE-bench
git clone https://github.com/sierra-research/tau2-bench.git  chapter6/tau2-bench
git clone https://github.com/laude-institute/terminal-bench.git  chapter6/terminal-bench
# 第 7 章 · 训练框架（bojieli/* 为本书适配的分支）
git clone https://github.com/bojieli/minimind.git  chapter7/MiniMind-pretrain/minimind  # 实验 7-3 从零训 LLM
git clone https://github.com/bojieli/minimind-v.git  chapter7/MiniMind-pretrain/minimind-v  # 实验 7-4 从零训 VLM（投影层）
git clone https://github.com/bojieli/AdaptThink.git  chapter7/AdaptThink-original
git clone https://github.com/bojieli/AWorld.git  chapter7/AWorld
git clone https://github.com/bojieli/SFTvsRL.git  chapter7/SFTvsRL
git clone https://github.com/bojieli/verl.git  chapter7/verl
git clone https://github.com/thinking-machines-lab/tinker-cookbook.git chapter7/tinker-cookbook
git clone https://github.com/19PINE-AI/rlvp.git  chapter7/RLVP/rlvp  # 实验 7-14 RLVP 论文代码
git clone https://github.com/PRIME-RL/SimpleVLA-RL.git  chapter7/SimpleVLA-RL/SimpleVLA-RL  # 实验 7-13 视觉-语言-动作 RL
# 第 9 章 · 浏览器自动化与 Claude 示例
git clone https://github.com/browser-use/browser-use.git  chapter9/browser-use
git clone https://github.com/anthropics/claude-quickstarts.git  chapter9/claude-quickstarts
# 第 10 章 · 双 Agent 架构（已独立为 TalkAct 项目）+ 斯坦福 AI 小镇
git clone https://github.com/19PINE-AI/TalkAct.git  chapter10/use-computer-while-calling
git clone https://github.com/joonspk-research/generative_agents.git  chapter10/generative_agents  # 实验 10-7 斯坦福 AI 小镇各项目 README 如标注了特定 commit，请按说明
git checkout到对应版本以保证复现一致。第 10 章use-computer-while-calling已发展为独立维护的 19PINE-AI/TalkAct，本仓库不内置该目录，用上面的克隆命令获取。
下面这些实验无专属 clone 命令，但有特定的复现方式：
| 实验 | 类型 | 说明 | 
|---|---|---|
| 6-2 / 6-3 / 6-4 / 6-9 | 📝 读者练习 | 人肉基准、记忆评估、JSON Cards vs RAG、记忆选型——改造复用第 3 章 user-memory/user-memory-evaluation/contextual-retrieval | 
| 5-12 | 📝 读者练习 | 能创造 Agent 的 Agent——基于 chapter5/coding-agent自举扩展 | 
| 7-8 | 📝 读者练习 | Prompt 蒸馏——落地实现见 chapter8/prompt-distillation（跨章复用） | 
| 7-9 | 📝 读者练习 | CoT 蒸馏 [扩展]——配套实现见chapter7/cot-distillation（含 SFT 数据生成与规则验证器） | 
| 6-11 | 🤖 仿真评估 | OpenVLA + RoboTwin2——VLA 训练/环境依赖见 chapter7/SimpleVLA-RL的 README | 
| 9-8 / 9-9 | 🔧 真实硬件 | XLeRobot 遥操作与 LLM Agent 控制——需 SO-100 机械臂，Teleop · LLM Agent | 
| 9-10 | 🔧 真实硬件 | RGB 零样本 Sim2Real 抓取—— StoneT2000/lerobot-sim2real（仿真可纯 GPU，部署需 SO-100） | 
本书与配套代码全部开源，非常欢迎社区通过 Pull Request 参与共建：
| 类型 | 说明 | 
|---|---|
| 📝 书籍内容改进 | 勘误、补充、更清晰的表述，或新增前沿进展（正文见 book/chapter*.md） | 
| 🐛 代码改进与 Bug 修复 | 让配套项目更健壮、更易用、更贴近生产实践 | 
| 🧪 新的实践项目 | 为某个实验补充/替换更好的实现，或贡献全新的示例项目 | 
| 🎨 配图设计改进 | 让 book/images/中的图表更清晰美观（配图由book/gen_*_figs.py生成） | 
| 🌐 新语言翻译 | 欢迎翻译成更多语言，可参考正体中文（ book-zhtw/）、英文（book-en/）、俄语（book-ru/）、泰米尔语（book-ta/）、越南语（book-vi/）、日语（book-ja/）的组织方式 | 
提交前建议先把相关实验亲手跑一遍、确认可复现；也欢迎先提 issue 讨论想法。
本项目采用 Apache License 2.0 开源许可证，详见 LICENSE 文件。部分子项目可能包含各自的许可证信息，请以子项目中的说明为准。
由 scripts/gen_star_history.py 生成，GitHub Actions 每日自动更新 · 点击图片查看实时数据

---
*爬取时间: 2026-07-24 16:01:07*
*来源: 直接站点爬取*
