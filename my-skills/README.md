# 我的 Skills

这个目录存放我自己创建的 skills，按作者或用途组织。

## 目录结构

```
my-skills/
└── daguan/                    # daguan 的 skills
    └── alphaevolve-run/       # AlphaEvolve/OpenEvolve 运行
```

---

## daguan Skills

### alphaevolve-run

**版本:** 0.6.1

使用 AlphaEvolve/OpenEvolve 执行 MLE 代码进化或 Prompt 进化任务。

**功能:**
- **MLE 代码进化**: 优化机器学习模型代码
- **Prompt 进化**: 优化提示词
- **完整流程管理**: 环境检查 → 输入校验 → 文件共创 → 启动进化 → 结果检查
- **输入输出验证**: 自动校验输入文件和输出结果
- **Judge 生成和验证**: 自动生成评判器并验证其正确性

**适用场景:**
- 启动 AlphaEvolve 进化任务
- 运行 OpenEvolve 优化
- 执行 MLE 代码进化
- 执行 Prompt 进化
- 使用 AlphaEvolve/OpenEvolve 运行任务

**包含资源:**

**Assets (6个):**
- `agent_mle.py` - MLE 代码进化 Agent 模板
- `agent_prompt.py` - Prompt 进化 Agent 模板
- `config_mle.json` - MLE 配置模板
- `config_prompt.json` - Prompt 配置模板
- `judge_mle.py` - MLE Judge 模板
- `judge_prompt.py` - Prompt Judge 模板

**References (4个):**
- `agent_spec.md` - Agent 编写规范
- `config_guide.md` - 配置文件指南
- `judge_spec.md` - Judge 编写规范
- `task_goal_guide.md` - 任务目标设置指南

**Scripts (8个):**
- `check_inputs.py` - 输入文件校验
- `check_outputs.py` - 输出结果检查
- `fix_agent_paths.py` - 修复 Agent 路径
- `generate_judge.py` - 生成 Judge 文件
- `main.py` - 主运行脚本
- `validate_agent.py` - Agent 验证
- `validate_judge.py` - Judge 验证

**执行流程:**
1. 环境检查 - 确认环境变量设置
2. 输入校验 - 验证输入文件完整性
3. 文件共创 - 与用户交互创建配置文件
4. 启动进化 - 运行 AlphaEvolve/OpenEvolve
5. 结果检查 - 验证输出结果

**位置:** `my-skills/daguan/alphaevolve-run/`

---

## Skills 统计

**总计:** 1 个 skill

| 作者/分类 | 数量 | Skills |
|----------|------|--------|
| daguan | 1 | alphaevolve-run |

---

**最后更新:** 2025-12-31
