# 社区 Skills

这个目录存放从其他地方下载的 skills，按来源组织。

## 目录结构

```
community-skills/
├── deepagents/                    # 来自 deepagents 的 4 个 skills
├── claude-code-plugins-plus/      # 来自 claude-code-plugins-plus 的 1 个 skill
└── anthropics/                    # 来自 Anthropic 官方的 16 个 skills
```

---

## DeepAgents Skills

来自 https://github.com/LifeIsSoSolong/deepagents

位于 `community-skills/deepagents/` 目录

### 1. arxiv-search

搜索 arXiv 预印本论文库（物理、数学、计算机科学、定量生物学等领域）。

**功能:**
- 查找期刊发表前的预印本和最新研究论文
- 搜索计算生物学、生物信息学或系统生物学方面的论文
- 访问与生物学相关的数学或统计方法论文
- 查找应用于生物问题的机器学习论文

### 2. langgraph-docs

获取 LangGraph 文档以提供准确、最新的指导。

**功能:**
- 访问 LangGraph Python 文档索引
- 获取相关的使用指南、核心概念和教程
- 提供基于官方文档的准确实现建议

### 3. skill-creator

创建有效 skills 的完整指南。

**功能:**
- 理解 skill 结构和设计模式
- 学习如何创建、验证和迭代 skills
- 掌握最佳实践：渐进式披露、资源组织、上下文效率

**适用场景:** 当你需要创建新 skill、修改现有 skill 或学习 skill 开发时使用

### 4. web-research

提供结构化的网络研究方法。

**功能:**
- 研究需要多个信息来源的复杂主题
- 从网络收集并综合当前信息
- 进行跨多个主题的对比分析
- 生成具有清晰引用的研究报告

---

## Claude Code Plugins Plus Skills

来自 https://github.com/jeremylongshore/claude-code-plugins-plus

位于 `community-skills/claude-code-plugins-plus/` 目录

### 5. ml-model-trainer

自动化机器学习模型训练工作流。

**功能:**
- 数据分析和准备：分析数据集，识别目标变量，确定模型类型（分类、回归等）
- 模型选择和训练：选择合适的算法，配置训练参数，使用交叉验证训练模型
- 性能评估和持久化：生成性能指标，保存训练好的模型
- 支持分类和回归任务

**适用场景:**
- 训练机器学习模型
- 评估模型性能
- 自动化机器学习工作流

**包含资源:**
- Python 训练脚本（数据预处理、模型训练、评估、保存和加载）
- 示例数据集
- 评估报告模板
- 依赖项清单

---

## Anthropic 官方 Skills

来自 https://github.com/anthropics/skills

位于 `community-skills/anthropics/` 目录

### 文档处理类

#### 6. docx

全面的文档创建、编辑和分析。

**功能:**
- 创建和修改 Word 文档
- 支持跟踪更改和评论
- 格式保留和文本提取

**适用场景:** 处理专业文档（.docx 文件）

#### 7. pdf

全面的 PDF 处理工具包。

**功能:**
- 提取文本和表格
- 创建新 PDF
- 合并/拆分文档
- 处理表单

**适用场景:** 填写 PDF 表单或大规模处理、生成、分析 PDF 文档

#### 8. pptx

演示文稿创建、编辑和分析。

**功能:**
- 创建和修改 PowerPoint 演示文稿
- 处理布局、评论和演讲者备注

**适用场景:** 处理演示文稿（.pptx 文件）

#### 9. xlsx

全面的电子表格创建、编辑和分析。

**功能:**
- 支持公式、格式化、数据分析和可视化
- 处理 .xlsx, .xlsm, .csv, .tsv 等格式
- 保留公式的同时修改数据
- 重新计算公式

**适用场景:** 处理电子表格文件

### 设计与创意类

#### 10. algorithmic-art

使用 p5.js 创建算法艺术，支持种子随机性和交互式参数探索。

**适用场景:** 生成艺术、算法艺术、流场、粒子系统

#### 11. brand-guidelines

应用官方品牌颜色和字体到各种产出物。

**适用场景:** 需要品牌风格、视觉格式化或公司设计标准时使用

#### 12. canvas-design

使用设计哲学创建美观的视觉艺术（PNG/PDF）。

**特色:** 包含 90+ 开源字体

**适用场景:** 海报、艺术作品、设计或其他静态作品

#### 13. frontend-design

创建具有高设计质量的生产级前端界面。

**适用场景:** 构建 Web 组件、页面、仪表板、React 组件、HTML/CSS 布局

#### 14. theme-factory

为各种产出物应用主题样式。

**功能:**
- 10个预设主题（颜色/字体）
- 可即时生成新主题
- 适用于幻灯片、文档、报告、HTML 页面等

### 开发与工具类

#### 15. mcp-builder

创建高质量的 MCP (Model Context Protocol) 服务器。

**适用场景:** 构建 MCP 服务器集成外部 API 或服务（Python FastMCP 或 Node/TypeScript MCP SDK）

#### 16. skill-creator

创建有效 skills 的指南（Anthropic 官方版本）。

**适用场景:** 创建或更新 skill，扩展 Claude 的能力

#### 17. web-artifacts-builder

创建复杂的多组件 claude.ai HTML artifacts。

**技术栈:** React, Tailwind CSS, shadcn/ui

**适用场景:** 需要状态管理、路由或 shadcn/ui 组件的复杂 artifacts

#### 18. webapp-testing

使用 Playwright 测试本地 Web 应用。

**功能:**
- 验证前端功能
- 调试 UI 行为
- 捕获浏览器截图
- 查看浏览器日志

### 沟通与协作类

#### 19. doc-coauthoring

结构化的文档协作编写工作流。

**适用场景:** 编写文档、提案、技术规范、决策文档或类似的结构化内容

#### 20. internal-comms

帮助编写各种内部沟通文档。

**适用场景:** 状态报告、领导更新、公司通讯、FAQ、事件报告、项目更新等

#### 21. slack-gif-creator

创建优化用于 Slack 的动画 GIF。

**功能:**
- 提供约束和验证工具
- 动画概念指导

**适用场景:** 为 Slack 创建动画 GIF

---

## Skills 统计

**总计：21 个 skills**

| 来源 | 数量 | 目录 |
|------|------|------|
| DeepAgents | 4 | `deepagents/` |
| Claude Code Plugins Plus | 1 | `claude-code-plugins-plus/` |
| Anthropic 官方 | 16 | `anthropics/` |

### 分类统计

- **文档处理**: 4 个 (docx, pdf, pptx, xlsx)
- **设计与创意**: 5 个 (algorithmic-art, brand-guidelines, canvas-design, frontend-design, theme-factory)
- **开发与工具**: 4 个 (mcp-builder, skill-creator, web-artifacts-builder, webapp-testing)
- **沟通与协作**: 3 个 (doc-coauthoring, internal-comms, slack-gif-creator)
- **研究与学习**: 3 个 (arxiv-search, langgraph-docs, web-research)
- **机器学习**: 2 个 (ml-model-trainer, skill-creator)

---

**最后更新:** 2025-12-31
