# promote2classical

**英文单词转文言文库** — 用最少的Token表达最丰富的含义。

## 理念

文言文一字一义，言简意赅。将AI提示词中的英文单词转为文言文，可显著减少Token消耗。

| 英文 | Token数 | 文言文 | Token数 |
|------|---------|--------|---------|
| promote | 1 | 升 | 1 |
| enhance | 1 | 强 | 1 |
| model | 1 | 模 | 1 |
| context | 1 | 境 | 1 |

**理论上可节省30-50%的词汇Token。**

## 安装

```bash
pip install promote2classical
```

或直接从源码安装：

```bash
git clone https://github.com/YOUR_USERNAME/promote2classical.git
cd promote2classical
pip install -e .
```

## 快速开始

```python
from promote2classical import translate

# 单词翻译
result = translate("promote")
print(result)  # 升

# 批量翻译
from promote2classical import Translator
t = Translator(api_key="your-api-key")
words = ["promote", "enhance", "improve"]
results = t.batch_translate(words)
print(results)  # ['升', '强', '改良']
```

## 高级用法

### 使用自定义API密钥

```python
import os
from promote2classical import Translator

# 方式1: 环境变量
# export ANTHROPIC_API_KEY=sk-...

# 方式2: 直接传入
translator = Translator(api_key="sk-ant-api03-...")
result = translator.translate("accelerate")
print(result)  # 疾
```

### 自定义模型

```python
translator = Translator(model="claude-opus-4-6")  # 默认
# 或使用其他模型
translator = Translator(model="claude-sonnet-4-6")
```

### 禁用缓存

```python
translator = Translator(cache=False)
```

### 扩展词典

```python
from promote2classical.dict.builtin import EN2CLASSICAL_BUILTIN

# 添加自定义词条
EN2CLASSICAL_BUILTIN["hello"] = "善"
EN2CLASSICAL_BUILTIN["world"] = "寰"
```

## 内置词典（部分）

| 英文 | 文言文 | 英文 | 文言文 |
|------|--------|------|--------|
| promote | 升 | increase | 增 |
| good | 善 | bad | 恶 |
| big | 大 | small | 小 |
| model | 模 | prompt | 令 |
| token | 符 | context | 境 |

完整词典请查看 [`promote2classical/dict/builtin.py`](promote2classical/dict/builtin.py)

## 工作原理

```
┌─────────────────────────────────────────────┐
│           promote2classical                 │
├─────────────────────────────────────────────┤
│  1. 词典查找 (builtin dict)                  │
│     ↓ 命中                                  │
│     返回文言文                               │
│                                             │
│  2. 缓存查找                                 │
│     ↓ 命中                                  │
│     返回缓存结果                             │
│                                             │
│  3. AI翻译 (Claude API)                     │
│     ↓                                       │
│     返回翻译结果                             │
└─────────────────────────────────────────────┘
```

## AI翻译策略

对于词典中没有的词汇，库会调用Claude API进行翻译：

- 使用Opus 4.6模型（默认）
- 提示词精简，减少翻译本身消耗的Token
- 自动缓存翻译结果

## 适用场景

- 大量AI提示词需要Token优化
- API调用成本敏感
- 需要中英双语对照开发

## 不适用场景

- 需要精确语义的场景（文言文有多义性）
- 实时性要求极高的场景（AI翻译有延迟）
- 词典覆盖不足的专业术语

## License

MIT
