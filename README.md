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
git clone https://github.com/onluuqs/promote2classical.git
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
t = Translator()
words = ["promote", "enhance", "improve"]
results = t.batch_translate(words)
print(results)  # ['升', '强', '改良']
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
│  1. 词典查找 (YAML > builtin dict)           │
│     ↓ 命中                                  │
│     返回文言文                               │
│                                             │
│  2. 词典无结果                              │
│     ↓                                      │
│     返回原英文单词                            │
└─────────────────────────────────────────────┘
```

## 适用场景

- 大量AI提示词需要Token优化
- 需要中英双语对照开发

## 不适用场景

- 词典覆盖不足的专业术语（可扩展词典解决）

## License

MIT
