# promote2classical 词典扩展规格

## 目标

扩充词汇库至 600+ 词，不使用任何 API，纯本地词典。保持一字一义为主、必要时两字的混用风格。

## 方案

### 目录结构

```
promote2classical/
├── dict/
│   ├── __init__.py       # 加载逻辑，统一导出
│   ├── builtin.py        # 保留内置默认词典（修复重复key）
│   └── dictionary.yml     # 新增用户可编辑词典（YAML格式）
├── docs/
│   └── superpowers/
│       └── specs/
│           └── 2026-04-07-promote2classical-dictionary-expansion-design.md
```

### 查词顺序

1. **YAML 用户词典** — 优先查用户词典
2. **builtin.py 内置词典** — 兜底默认词库

用户词典可**覆盖**内置词（如用户认为某个翻译不妥可自行修正），也可**新增**内置中未收录的词。

### YAML 格式

```yaml
# dictionary.yml
entries:
  - en: model
    classical: 模
    domain: ai
    note: 模型

  - en: attention
    classical: 注
    domain: ai
    note: 注意力机制

  - en: function
    classical: 函
    domain: programming
    note: 函数

  - en: loop
    classical: 环
    domain: programming
    note: 循环
```

- `en`（必填）：英文单词（小写，内部自动转）
- `classical`（必填）：文言文翻译
- `domain`（可选）：分类 — `ai` | `programming` | `common`
- `note`（可选）：备注说明

### 词汇分类（目标 600+ 词）

| 分类 | 数量目标 | 内容 |
|------|---------|------|
| `ai` | ~200 | model、prompt、context、embedding、attention、token、layer、weight、bias、gradient、loss、optimizer、transformer、neural、network、train、infer、fine-tune、rag、retrieval 等 |
| `programming` | ~200 | function、variable、class、object、method、loop、array、list、dict、string、async、thread、process、memory、pointer、interface、abstract、module、package、dependency、api、route、endpoint、query、mutation、schema、debug、refactor 等 |
| `common` | ~200 | think、know、want、need、feel、see、hear、say、tell、ask、give、take、come、go、look、find、learn、understand、remember、forget、love、hate、hope、fear、try、manage、control、measure、calculate、compare、choose、decide、explain、describe、show、hide、save、load 等 |

### 代码改动

#### `dict/__init__.py` — 新增

```python
"""词典加载模块"""

import os
from pathlib import Path
from typing import Optional

import yaml

from .builtin import EN2CLASSICAL_BUILTIN

# 用户词典路径
_DICT_PATH = Path(__file__).parent / "dictionary.yml"

# 合并后词典（lazy加载）
_MERGED: Optional[dict[str, str]] = None


def _load_merged() -> dict[str, str]:
    """加载并合并内置词典和用户词典"""
    merged = dict(EN2CLASSICAL_BUILTIN)

    if _DICT_PATH.exists():
        with open(_DICT_PATH, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if data and "entries" in data:
            for entry in data["entries"]:
                en = entry.get("en", "").strip().lower()
                classical = entry.get("classical", "").strip()
                if en and classical:
                    merged[en] = classical

    return merged


def get_merged_dict() -> dict[str, str]:
    """获取合并后的完整词典"""
    global _MERGED
    if _MERGED is None:
        _MERGED = _load_merged()
    return _MERGED


def translate(word: str) -> str:
    """查词函数"""
    return get_merged_dict().get(word.strip().lower(), word)


# 导出
EN2CLASSICAL_MERGED = property(lambda self: get_merged_dict())
```

#### `dict/builtin.py` — 修复

- 删除重复 key `"build"`（保留 `"build": "建"`，删除 `"build": "筑"`）

#### `core.py` — 更新导入

- 将 `from .dict.builtin import EN2CLASSICAL_BUILTIN` 改为从 `dict/__init__.py` 导入合并后的词典

#### `promote2classical/__init__.py` — 新增导出

- 从 `dict` 包导出 `translate` 函数和 `EN2CLASSICAL_MERGED` 常量

### 修复项

1. `builtin.py` 重复 key `"build"` — 删除 `"build": "筑"` 行
2. `pyproject.toml` 占位符 — 将 `YOUR_USERNAME` 替换为 `onluuqs`，`Your Name` 替换为真实名称（或 `onluuqs`）

### 测试

- 新增 YAML 加载测试（`test_yaml_dict.py`）
- 验证覆盖逻辑（用户词典覆盖 builtin.py）
- 验证分类完整性

## 实施步骤

1. 创建 `dictionary.yml` 文件，按分类填充词汇
2. 修复 `builtin.py` 重复 key
3. 新增 `dict/__init__.py` 加载逻辑
4. 更新 `core.py` 导入
5. 更新 `promote2classical/__init__.py` 导出
6. 修复 `pyproject.toml` 占位符
7. 新增/更新测试
8. 运行测试验证
