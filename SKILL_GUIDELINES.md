# Skills 添加指南

本文档说明如何向此仓库添加新的 skills，以及需要注意的规范要求。

## Claude Skills Frontmatter 规范

在添加或创建新的 skill 时，`SKILL.md` 文件的 YAML frontmatter 必须符合 Claude 的规范。

### 允许的字段

只有以下字段是允许的：

1. **name** (必需)
   - Skill 的唯一标识符
   - 使用 kebab-case 格式（小写字母，连字符分隔）
   - 示例：`training-machine-learning-models`

2. **description** (必需)
   - 描述 skill 的功能和使用场景
   - 包含触发条件（何时使用此 skill）
   - 可以使用多行文本（使用 `|` 符号）
   - 示例：
     ```yaml
     description: |
       Train machine learning models with automated workflows. Use when asked to
       "train model" or "evaluate model" or "automate ML training".
     ```

3. **license** (可选)
   - Skill 的许可证
   - 示例：`MIT`, `Apache-2.0`

4. **allowed-tools** (可选)
   - 允许使用的工具列表
   - 示例：`Read, Write, Edit, Grep, Glob, Bash(cmd:*)`

5. **compatibility** (可选)
   - 兼容性信息

6. **metadata** (可选)
   - 其他元数据，以键值对形式存储
   - 可以包含 `version`、`author` 等信息
   - 示例：
     ```yaml
     metadata:
       version: 1.0.0
       author: Your Name <email@example.com>
     ```

### ❌ 不允许的字段

以下字段**不能**作为顶级字段出现在 frontmatter 中：

- `version` - 应放在 `metadata` 中
- `author` - 应放在 `metadata` 中
- 其他任何未在上述列表中的字段

## Frontmatter 示例

### 最简示例
```yaml
---
name: my-skill
description: A simple skill that does something useful
---
```

### 完整示例
```yaml
---
name: training-machine-learning-models
description: |
  Train machine learning models with automated workflows. Analyzes datasets,
  selects model types (classification, regression), configures parameters,
  trains with cross-validation, and saves model artifacts. Use when asked to
  "train model" or "evaluate model" or "automate ML training".
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(cmd:*)
license: MIT
metadata:
  version: 1.0.0
  author: Your Name <email@example.com>
  source: https://github.com/example/repo
---
```

## 常见错误

### ❌ 错误：version 和 author 作为顶级字段
```yaml
---
name: my-skill
description: My skill description
version: 1.0.0
author: John Doe
---
```

**错误信息：** `unexpected key in SKILL.md frontmatter: properties must be in ('name', 'description', 'license', 'allowed-tools', 'compatibility', 'metadata')`

### ✅ 正确：将 version 和 author 放在 metadata 中
```yaml
---
name: my-skill
description: My skill description
metadata:
  version: 1.0.0
  author: John Doe
---
```

## 添加新 Skill 的步骤

1. **下载或创建 skill**
   - 从其他仓库下载或自己创建

2. **检查 frontmatter**
   - 确保只使用允许的字段
   - 将不允许的字段移到 `metadata` 中

3. **测试上传**
   - 在 Claude 中使用 "Upload skill" 功能测试
   - 确保没有 frontmatter 错误

4. **添加到仓库**
   - 复制到 `my-skills/` 或 `community-skills/` 目录
   - 更新对应的 README.md

5. **提交和推送**
   - 使用清晰的 commit message
   - 推送到远程仓库

## 参考资源

- Claude Skills 官方文档
- 本仓库现有的 skills 示例

---

**创建日期:** 2025-12-31
