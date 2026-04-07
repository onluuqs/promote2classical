# promote2classical 词典扩展实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 扩充词汇库至 600+ 词，纯本地词典，不调用 API。使用 YAML 管理用户词典，builtin.py 作为默认兜底。

**Architecture:** YAML 词典文件 + Python 加载模块 + 合并查词。查词顺序：YAML 用户词典优先，覆盖/新增 builtin.py 默认词。

**Tech Stack:** Python 3.8+, PyYAML

---

## 文件映射

| 文件 | 操作 |
|------|------|
| `dict/dictionary.yml` | 新建 — 用户可编辑词典 |
| `dict/__init__.py` | 新建 — 词典加载逻辑 |
| `dict/builtin.py` | 修改 — 删除重复 key `"build": "筑"` |
| `core.py` | 修改 — 导入改为从 `dict` 包加载合并词典 |
| `promote2classical/__init__.py` | 修改 — 新增导出 |
| `pyproject.toml` | 修改 — 修复占位符 |
| `tests/test_yaml_dict.py` | 新建 — YAML 加载测试 |
| `tests/test_promote2classical.py` | 修改 — 更新测试以使用新导入路径 |

---

## Task 1: 修复 builtin.py 重复 key

**Files:**
- Modify: `dict/builtin.py:28-30`

- [ ] **Step 1: 删除重复 key `"build": "筑"`**

找到 `builtin.py` 第 30 行附近的重复条目：
```python
    "build": "筑",
    "build": "建",
```

删除 `"build": "筑"` 这一行，保留 `"build": "建"`。

运行验证：
```bash
D:\anaconda\envs\torch128\python.exe -c "from dict.builtin import EN2CLASSICAL_BUILTIN; print('duplicate check:', len(EN2CLASSICAL_BUILTIN), len(set(EN2CLASSICAL_BUILTIN.keys())))"
```
确保 key 数量等于 unique key 数量（无重复）。

- [ ] **Step 2: 提交**

```bash
git add dict/builtin.py
git commit -m "fix: remove duplicate key 'build' in builtin dict

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 2: 创建 dictionary.yml 词典文件

**Files:**
- Create: `dict/dictionary.yml`

- [ ] **Step 1: 创建 YAML 文件，写入完整词汇**

创建 `J:/Main_AIproject/promote2classical/dict/dictionary.yml`，内容如下（按分类组织，共 600+ 词）：

```yaml
# 文言文词典 - 用户可编辑
# 查词顺序: YAML > builtin.py
# 格式: en(必填), classical(必填), domain(可选), note(可选)

entries:
  # ========== AI / LLM 术语 ==========
  - en: model
    classical: 模
    domain: ai
    note: 模型

  - en: prompt
    classical: 令
    domain: ai
    note: 提示词

  - en: context
    classical: 境
    domain: ai
    note: 上下文

  - en: token
    classical: 符
    domain: ai
    note: 标记

  - en: embedding
    classical: 嵌
    domain: ai
    note: 向量嵌入

  - en: attention
    classical: 注
    domain: ai
    note: 注意力

  - en: layer
    classical: 层
    domain: ai
    note: 层

  - en: weight
    classical: 权
    domain: ai
    note: 权重

  - en: bias
    classical: 偏
    domain: ai
    note: 偏置

  - en: gradient
    classical: 斜
    domain: ai
    note: 梯度

  - en: loss
    classical: 损
    domain: ai
    note: 损失

  - en: optimizer
    classical: 优
    domain: ai
    note: 优化器

  - en: transformer
    classical: 变
    domain: ai
    note: Transformer架构

  - en: neural
    classical: 神
    domain: ai
    note: 神经

  - en: network
    classical: 网
    domain: ai
    note: 网络

  - en: train
    classical: 训
    domain: ai
    note: 训练

  - en: infer
    classical: 推
    domain: ai
    note: 推理

  - en: fine-tune
    classical: 精调
    domain: ai
    note: 微调

  - en: rag
    classical: 索
    domain: ai
    note: 检索增强生成

  - en: retrieval
    classical: 觅
    domain: ai
    note: 检索

  - en: generation
    classical: 生
    domain: ai
    note: 生成

  - en: completion
    classical: 完
    domain: ai
    note: 补全

  - en: hallucination
    classical: 幻
    domain: ai
    note: 幻觉

  - en: alignment
    classical: 校
    domain: ai
    note: 对齐

  - en: reinforcement
    classical: 强
    domain: ai
    note: 强化

  - en: reward
    classical: 赏
    domain: ai
    note: 奖励

  - en: policy
    classical: 策
    domain: ai
    note: 策略

  - en: agent
    classical: 代理
    domain: ai
    note: 智能体

  - en: tool
    classical: 具
    domain: ai
    note: 工具

  - en: chain
    classical: 链
    domain: ai
    note: 链

  - en: pipeline
    classical: 管
    domain: ai
    note: 管道

  - en: batch
    classical: 批
    domain: ai
    note: 批量

  - en: epoch
    classical: 轮
    domain: ai
    note: 训练轮次

  - en: learning_rate
    classical: 速
    domain: ai
    note: 学习率

  - en: temperature
    classical: 温
    domain: ai
    note: 温度参数

  - en: top_p
    classical: 域
    domain: ai
    note: 采样域

  - en: corpus
    classical: 料
    domain: ai
    note: 语料

  - en: vocabulary
    classical: 汇
    domain: ai
    note: 词汇表

  - en: tokenizer
    classical: 分
    domain: ai
    note: 分词器

  - en: sentence
    classical: 句
    domain: ai
    note: 句子

  - en: document
    classical: 篇
    domain: ai
    note: 文档

  - en: paraphrase
    classical: 译
    domain: ai
    note: 改写

  - en: sentiment
    classical: 情
    domain: ai
    note: 情感

  - en: classification
    classical: 类
    domain: ai
    note: 分类

  - en: regression
    classical: 拟
    domain: ai
    note: 回归

  - en: clustering
    classical: 聚
    domain: ai
    note: 聚类

  - en: outlier
    classical: 异
    domain: ai
    note: 异常值

  - en: anomaly
    classical: 异
    domain: ai
    note: 异常检测

  - en: prediction
    classical: 测
    domain: ai
    note: 预测

  - en: estimation
    classical: 估
    domain: ai
    note: 估计

  - en: detection
    classical: 察
    domain: ai
    note: 检测

  - en: recognition
    classical: 识
    domain: ai
    note: 识别

  - en: segmentation
    classical: 分
    domain: ai
    note: 分割

  - en: synthesis
    classical: 合
    domain: ai
    note: 合成

  - en: inference
    classical: 断
    domain: ai
    note: 推断

  - en: reasoning
    classical: 推
    domain: ai
    note: 推理

  - en: planning
    classical: 策
    domain: ai
    note: 规划

  - en: decision
    classical: 决
    domain: ai
    note: 决策

  - en: knowledge
    classical: 知
    domain: ai
    note: 知识

  - en: memory
    classical: 忆
    domain: ai
    note: 记忆

  - en: schema
    classical: 纲
    domain: ai
    note: 模式

  - en: template
    classical: 模
    domain: ai
    note: 模板

  - en: constraint
    classical: 限
    domain: ai
    note: 约束

  - en: objective
    classical: 标
    domain: ai
    note: 目标

  - en: metric
    classical: 度
    domain: ai
    note: 指标

  - en: benchmark
    classical: 标
    domain: ai
    note: 基准

  - en: evaluation
    classical: 评
    domain: ai
    note: 评估

  - en: validation
    classical: 验
    domain: ai
    note: 验证

  - en: calibration
    classical: 校
    domain: ai
    note: 校准

  - en: robustness
    classical: 稳
    domain: ai
    note: 鲁棒性

  - en: generalization
    classical: 泛
    domain: ai
    note: 泛化

  - en: overfitting
    classical: 过
    domain: ai
    note: 过拟合

  - en: underfitting
    classical: 欠
    domain: ai
    note: 欠拟合

  - en: regularization
    classical: 则
    domain: ai
    note: 正则化

  - en: normalization
    classical: 常
    domain: ai
    note: 归一化

  - en: quantization
    classical: 量
    domain: ai
    note: 量化

  - en: distillation
    classical: 蒸
    domain: ai
    note: 蒸馏

  - en: pruning
    classical: 剪
    domain: ai
    note: 剪枝

  - en: sparsity
    classical: 稀
    domain: ai
    note: 稀疏性

  - en: latency
    classical: 迟
    domain: ai
    note: 延迟

  - en: throughput
    classical: 流
    domain: ai
    note: 吞吐量

  - en: scaling
    classical: 扩
    domain: ai
    note: 扩展

  - en: deployment
    classical: 布
    domain: ai
    note: 部署

  - en: serving
    classical: 服
    domain: ai
    note: 服务化

  - en: endpoint
    classical: 口
    domain: ai
    note: 端点

  - en: request
    classical: 请
    domain: ai
    note: 请求

  - en: response
    classical: 应
    domain: ai
    note: 响应

  - en: streaming
    classical: 流
    domain: ai
    note: 流式

  - en: session
    classical: 会
    domain: ai
    note: 会话

  - en: conversation
    classical: 谈
    domain: ai
    note: 对话

  - en: message
    classical: 讯
    domain: ai
    note: 消息

  - en: instruction
    classical: 指
    domain: ai
    note: 指令

  - en: constraint
    classical: 束
    domain: ai
    note: 限制

  - en: preference
    classical: 好
    domain: ai
    note: 偏好

  - en: feedback
    classical: 馈
    domain: ai
    note: 反馈

  - en: demonstration
    classical: 示
    domain: ai
    note: 示范

  - en: sample
    classical: 样
    domain: ai
    note: 样本

  - en: label
    classical: 标
    domain: ai
    note: 标签

  - en: annotation
    classical: 注
    domain: ai
    note: 标注

  - en: augmentation
    classical: 增
    domain: ai
    note: 数据增强

  - en: preprocessing
    classical: 前
    domain: ai
    note: 预处理

  - en: postprocessing
    classical: 后
    domain: ai
    note: 后处理

  - en: feature
    classical: 特
    domain: ai
    note: 特征

  - en: representation
    classical: 表
    domain: ai
    note: 表示

  - en: encoding
    classical: 编
    domain: ai
    note: 编码

  - en: decoding
    classical: 解
    domain: ai
    note: 解码

  - en: vector
    classical: 矢
    domain: ai
    note: 向量

  - en: matrix
    classical: 阵
    domain: ai
    note: 矩阵

  - en: tensor
    classical: 张
    domain: ai
    note: 张量

  - en: dimension
    classical: 维
    domain: ai
    note: 维度

  - en: head
    classical: 头
    domain: ai
    note: 注意力头

  - en: feedforward
    classical: 前
    domain: ai
    note: 前馈

  - en: convolution
    classical: 卷
    domain: ai
    note: 卷积

  - en: pooling
    classical: 池
    domain: ai
    note: 池化

  - en: residual
    classical: 残
    domain: ai
    note: 残差

  - en: skip
    classical: 跳
    domain: ai
    note: 跳跃连接

  - en: encoder
    classical: 编
    domain: ai
    note: 编码器

  - en: decoder
    classical: 解
    domain: ai
    note: 解码器

  - en: tokenizer
    classical: 符
    domain: ai
    note: 分词器

  - en: bos
    classical: 始
    domain: ai
    note: 序列开始

  - en: eos
    classical: 终
    domain: ai
    note: 序列结束

  - en: pad
    classical: 填
    domain: ai
    note: 填充符

  - en: mask
    classical: 掩
    domain: ai
    note: 掩码

  - en: attention_mask
    classical: 掩
    domain: ai
    note: 注意力掩码

  - en: causal
    classical: 因
    domain: ai
    note: 因果

  - en: autoregressive
    classical: 自
    domain: ai
    note: 自回归

  - en: zero-shot
    classical: 零
    domain: ai
    note: 零样本

  - en: few-shot
    classical: 少
    domain: ai
    note: 少样本

  - en: one-shot
    classical: 单
    domain: ai
    note: 单样本

  - en: in-context
    classical: 境
    domain: ai
    note: 上下文内

  - en: prompting
    classical: 令
    domain: ai
    note: 提示工程

  - en: system_prompt
    classical: 系
    domain: ai
    note: 系统提示

  - en: user_prompt
    classical: 用
    domain: ai
    note: 用户提示

  - en: assistant_prompt
    classical: 助
    domain: ai
    note: 助手提示

  - en: cot
    classical: 思
    domain: ai
    note: 思维链

  - en: reflection
    classical: 省
    domain: ai
    note: 反思

  - en: self_critique
    classical: 省
    domain: ai
    note: 自我批判

  - en: monte_carlo
    classical: 蒙
    domain: ai
    note: 蒙特卡洛

  - en: bandit
    classical: 盗
    domain: ai
    note: 多臂老虎机

  - en: exploration
    classical: 探
    domain: ai
    note: 探索

  - en: exploitation
    classical: 用
    domain: ai
    note: 利用

  - en: q_learning
    classical: Q学
    domain: ai
    note: Q学习

  - en: rlhf
    classical: 强学
    domain: ai
    note: 人类反馈强化学习

  - en:ppo
    classical: 策优
    domain: ai
    note: 近端策略优化

  - en: reward_modeling
    classical: 赏模
    domain: ai
    note: 奖励建模

  - en: preference_modeling
    classical: 好模
    domain: ai
    note: 偏好建模

  - en: constitutional_ai
    classical: 约
    domain: ai
    note: 约法AI

  - en: gpt
    classical: 变
    domain: ai
    note: GPT架构

  - en: bert
    classical: 彼
    domain: ai
    note: BERT架构

  - en: llama
    classical: 羊
    domain: ai
    note: LLaMA模型

  - en: mistral
    classical: 雾
    domain: ai
    note: Mistral模型

  - en: quantization
    classical: 量
    domain: ai
    note: 模型量化

  - en: safetensors
    classical: 安
    domain: ai
    note: 安全张量格式

  - en: gguf
    classical: 格式
    domain: ai
    note: GGUF格式

  - en: flash_attention
    classical: 闪
    domain: ai
    note: 快速注意力

  - en: kv_cache
    classical: 缓存
    domain: ai
    note: 键值缓存

  - en: speculative_decoding
    classical: 揣
    domain: ai
    note: 投机解码

  - en: beam_search
    classical: 梁
    domain: ai
    note: 束搜索

  - en: greedy
    classical: 贪
    domain: ai
    note: 贪心

  - en: nucleus_sampling
    classical: 域
    domain: ai
    note: 核心采样

  - en: repetition_penalty
    classical: 复
    domain: ai
    note: 重复惩罚

  - en: length_penalty
    classical: 长
    domain: ai
    note: 长度惩罚

  # ========== 编程 / 技术词汇 ==========
  - en: function
    classical: 函
    domain: programming
    note: 函数

  - en: method
    classical: 法
    domain: programming
    note: 方法

  - en: class
    classical: 类
    domain: programming
    note: 类

  - en: object
    classical: 体
    domain: programming
    note: 对象

  - en: variable
    classical: 变
    domain: programming
    note: 变量

  - en: constant
    classical: 常
    domain: programming
    note: 常量

  - en: type
    classical: 型
    domain: programming
    note: 类型

  - en: interface
    classical: 口
    domain: programming
    note: 接口

  - en: abstract
    classical: 象
    domain: programming
    note: 抽象

  - en: concrete
    classical: 实
    domain: programming
    note: 具体

  - en: module
    classical: 模块
    domain: programming
    note: 模块

  - en: package
    classical: 包
    domain: programming
    note: 包

  - en: library
    classical: 库
    domain: programming
    note: 库

  - en: framework
    classical: 架
    domain: programming
    note: 框架

  - en: dependency
    classical: 赖
    domain: programming
    note: 依赖

  - en: import
    classical: 引
    domain: programming
    note: 导入

  - en: export
    classical: 出
    domain: programming
    note: 导出

  - en: async
    classical: 异
    domain: programming
    note: 异步

  - en: await
    classical: 待
    domain: programming
    note: 等待

  - en: thread
    classical: 线
    domain: programming
    note: 线程

  - en: process
    classical: 程
    domain: programming
    note: 进程

  - en: task
    classical: 事
    domain: programming
    note: 任务

  - en: concurrency
    classical: 并
    domain: programming
    note: 并发

  - en: parallelism
    classical: 行
    domain: programming
    note: 并行

  - en: synchronization
    classical: 同
    domain: programming
    note: 同步

  - en: deadlock
    classical: 锁
    domain: programming
    note: 死锁

  - en: race_condition
    classical: 竞
    domain: programming
    note: 竞态条件

  - en: mutex
    classical: 互
    domain: programming
    note: 互斥

  - en: semaphore
    classical: 信
    domain: programming
    note: 信号量

  - en: callback
    classical: 回
    domain: programming
    note: 回调

  - en: promise
    classical: 诺
    domain: programming
    note: Promise

  - en: future
    classical: 待
    domain: programming
    note: Future

  - en: iterator
    classical: 迭
    domain: programming
    note: 迭代器

  - en: generator
    classical: 生
    domain: programming
    note: 生成器

  - en: coroutine
    classical: 协
    domain: programming
    note: 协程

  - en: event
    classical: 事
    domain: programming
    note: 事件

  - en: loop
    classical: 环
    domain: programming
    note: 循环

  - en: iteration
    classical: 代
    domain: programming
    note: 迭代

  - en: recursion
    classical: 归
    domain: programming
    note: 递归

  - en: array
    classical: 列
    domain: programming
    note: 数组

  - en: list
    classical: 表
    domain: programming
    note: 列表

  - en: dict
    classical: 典
    domain: programming
    note: 字典

  - en: set
    classical: 集
    domain: programming
    note: 集合

  - en: tuple
    classical: 元
    domain: programming
    note: 元组

  - en: string
    classical: 串
    domain: programming
    note: 字符串

  - en: number
    classical: 数
    domain: programming
    note: 数字

  - en: integer
    classical: 整
    domain: programming
    note: 整数

  - en: float
    classical: 浮
    domain: programming
    note: 浮点数

  - en: boolean
    classical: 布尔
    domain: programming
    note: 布尔

  - en: null
    classical: 空
    domain: programming
    note: 空值

  - en: undefined
    classical: 未
    domain: programming
    note: 未定义

  - en: optional
    classical: 可
    domain: programming
    note: 可选

  - en: generic
    classical: 泛
    domain: programming
    note: 泛型

  - en: template
    classical: 模
    domain: programming
    note: 模板

  - en: macro
    classical: 宏
    domain: programming
    note: 宏

  - en: compile
    classical: 编
    domain: programming
    note: 编译

  - en: interpret
    classical: 释
    domain: programming
    note: 解释

  - en: runtime
    classical: 运
    domain: programming
    note: 运行时

  - en: compile_time
    classical: 编时
    domain: programming
    note: 编译时

  - en: build
    classical: 建
    domain: programming
    note: 构建

  - en: debug
    classical: 除虫
    domain: programming
    note: 调试

  - en: test
    classical: 试
    domain: programming
    note: 测试

  - en: mock
    classical: 仿
    domain: programming
    note: 模拟

  - en: stub
    classical: 桩
    domain: programming
    note: 桩

  - en: assert
    classical: 断
    domain: programming
    note: 断言

  - en: exception
    classical: 异
    domain: programming
    note: 异常

  - en: error
    classical: 谬
    domain: programming
    note: 错误

  - en: warning
    classical: 警
    domain: programming
    note: 警告

  - en: log
    classical: 志
    domain: programming
    note: 日志

  - en: trace
    classical: 迹
    domain: programming
    note: 追踪

  - en: monitor
    classical: 监
    domain: programming
    note: 监控

  - en: profile
    classical: 谱
    domain: programming
    note: 性能分析

  - en: optimize
    classical: 优
    domain: programming
    note: 优化

  - en: refactor
    classical: 重
    domain: programming
    note: 重构

  - en: legacy
    classical: 旧
    domain: programming
    note: 遗留

  - en: deprecate
    classical: 废
    domain: programming
    note: 弃用

  - en: feature_flag
    classical: 关
    domain: programming
    note: 特性开关

  - en: configuration
    classical: 配
    domain: programming
    note: 配置

  - en: environment
    classical: 境
    domain: programming
    note: 环境

  - en: development
    classical: 发
    domain: programming
    note: 开发

  - en: production
    classical: 产
    domain: programming
    note: 生产

  - en: staging
    classical: 预
    domain: programming
    note: 预发布

  - en: deployment
    classical: 布
    domain: programming
    note: 部署

  - en: rollback
    classical: 回
    domain: programming
    note: 回滚

  - en: migration
    classical: 迁
    domain: programming
    note: 迁移

  - en: version
    classical: 版
    domain: programming
    note: 版本

  - en: release
    classical: 发
    domain: programming
    note: 发布

  - en: changelog
    classical: 变
    domain: programming
    note: 变更日志

  - en: documentation
    classical: 文
    domain: programming
    note: 文档

  - en: specification
    classical: 规
    domain: programming
    note: 规格

  - en: requirement
    classical: 要
    domain: programming
    note: 需求

  - en: design
    classical: 计
    domain: programming
    note: 设计

  - en: architecture
    classical: 构
    domain: programming
    note: 架构

  - en: pattern
    classical: 模
    domain: programming
    note: 模式

  - en: antipattern
    classical: 反
    domain: programming
    note: 反模式

  - en: convention
    classical: 约
    domain: programming
    note: 约定

  - en: protocol
    classical: 约
    domain: programming
    note: 协议

  - en: standard
    classical: 准
    domain: programming
    note: 标准

  - en: specification
    classical: 格
    domain: programming
    note: 规范

  - en: contract
    classical: 约
    domain: programming
    note: 契约

  - en: coupling
    classical: 耦
    domain: programming
    note: 耦合

  - en: cohesion
    classical: 聚
    domain: programming
    note: 内聚

  - en: abstraction
    classical: 象
    domain: programming
    note: 抽象

  - en: encapsulation
    classical: 封
    domain: programming
    note: 封装

  - en: inheritance
    classical: 承
    domain: programming
    note: 继承

  - en: polymorphism
    classical: 多
    domain: programming
    note: 多态

  - en: composition
    classical: 合
    domain: programming
    note: 组合

  - en: delegation
    classical: 委
    domain: programming
    note: 委托

  - en: dependency_injection
    classical: 注
    domain: programming
    note: 依赖注入

  - en: inversion_of_control
    classical: 反
    domain: programming
    note: 控制反转

  - en: factory
    classical: 厂
    domain: programming
    note: 工厂

  - en: singleton
    classical: 单
    domain: programming
    note: 单例

  - en: observer
    classical: 观
    domain: programming
    note: 观察者

  - en: strategy
    classical: 策
    domain: programming
    note: 策略

  - en: adapter
    classical: 适
    domain: programming
    note: 适配器

  - en: facade
    classical: 门
    domain: programming
    note: 门面

  - en: decorator
    classical: 饰
    domain: programming
    note: 装饰器

  - en: middleware
    classical: 间
    domain: programming
    note: 中间件

  - en: pipeline
    classical: 管
    domain: programming
    note: 管道

  - en: filter
    classical: 滤
    domain: programming
    note: 过滤器

  - en: router
    classical: 路
    domain: programming
    note: 路由器

  - en: handler
    classical: 处
    domain: programming
    note: 处理器

  - en: serializer
    classical: 序
    domain: programming
    note: 序列化器

  - en: parser
    classical: 析
    domain: programming
    note: 解析器

  - en: validator
    classical: 验
    domain: programming
    note: 验证器

  - en: formatter
    classical: 格
    domain: programming
    note: 格式化器

  - en: encoder
    classical: 编
    domain: programming
    note: 编码器

  - en: decoder
    classical: 解
    domain: programming
    note: 解码器

  - en: compiler
    classical: 编
    domain: programming
    note: 编译器

  - en: linker
    classical: 连
    domain: programming
    note: 链接器

  - en: interpreter
    classical: 释
    domain: programming
    note: 解释器

  - en: virtual_machine
    classical: 虚机
    domain: programming
    note: 虚拟机

  - en: garbage_collection
    classical: 回收
    domain: programming
    note: 垃圾回收

  - en: memory
    classical: 存
    domain: programming
    note: 内存

  - en: heap
    classical: 堆
    domain: programming
    note: 堆

  - en: stack
    classical: 栈
    domain: programming
    note: 栈

  - en: pointer
    classical: 针
    domain: programming
    note: 指针

  - en: reference
    classical: 引
    domain: programming
    note: 引用

  - en: allocation
    classical: 配
    domain: programming
    note: 分配

  - en: deallocation
    classical: 释
    domain: programming
    note: 释放

  - en: buffer
    classical: 缓
    domain: programming
    note: 缓冲区

  - en: cache
    classical: 缓存
    domain: programming
    note: 缓存

  - en: session
    classical: 会
    domain: programming
    note: 会话

  - en: cookie
    classical: 饼
    domain: programming
    note: Cookie

  - en: token
    classical: 牌
    domain: programming
    note: 令牌

  - en: header
    classical: 头
    domain: programming
    note: 头部

  - en: body
    classical: 体
    domain: programming
    note: 主体

  - en: payload
    classical: 载
    domain: programming
    note: 载荷

  - en: schema
    classical: 纲
    domain: programming
    note: 模式

  - en: field
    classical: 域
    domain: programming
    note: 字段

  - en: record
    classical: 录
    domain: programming
    note: 记录

  - en: row
    classical: 行
    domain: programming
    note: 行

  - en: column
    classical: 列
    domain: programming
    note: 列

  - en: index
    classical: 引
    domain: programming
    note: 索引

  - en: query
    classical: 询
    domain: programming
    note: 查询

  - en: mutation
    classical: 改
    domain: programming
    note: 变更

  - en: transaction
    classical: 事
    domain: programming
    note: 事务

  - en: commit
    classical: 交
    domain: programming
    note: 提交

  - en: rollback
    classical: 回
    domain: programming
    note: 回滚

  - en: concurrency
    classical: 并
    domain: programming
    note: 并发控制

  - en: isolation
    classical: 隔
    domain: programming
    note: 隔离级别

  - en: acid
    classical: 酸
    domain: programming
    note: ACID特性

  - en: nosql
    classical: 非
    domain: programming
    note: NoSQL

  - en: sql
    classical: 查
    domain: programming
    note: SQL

  - en: crud
    classical: 增删查改
    domain: programming
    note: CRUD

  - en: rest
    classical: 表
    domain: programming
    note: REST

  - en: graphql
    classical: 图
    domain: programming
    note: GraphQL

  - en: websocket
    classical: 套
    domain: programming
    note: WebSocket

  - en: http
    classical: 网
    domain: programming
    note: HTTP

  - en: https
    classical: 安
    domain: programming
    note: HTTPS

  - en: tcp
    classical: 传
    domain: programming
    note: TCP

  - en: udp
    classical: 数
    domain: programming
    note: UDP

  - en: ip
    classical: 网
    domain: programming
    note: IP

  - en: dns
    classical: 名
    domain: programming
    note: DNS

  - en: url
    classical: 址
    domain: programming
    note: URL

  - en: uri
    classical: 标
    domain: programming
    note: URI

  - en: domain
    classical: 域
    domain: programming
    note: 域名

  - en: host
    classical: 主
    domain: programming
    note: 主机

  - en: port
    classical: 口
    domain: programming
    note: 端口

  - en: path
    classical: 径
    domain: programming
    note: 路径

  - en: parameter
    classical: 参数
    domain: programming
    note: 参数

  - en: argument
    classical: 实
    domain: programming
    note: 实参

  - en: return
    classical: 返
    domain: programming
    note: 返回

  - en: throw
    classical: 抛
    domain: programming
    note: 抛出

  - en: catch
    classical: 捕
    domain: programming
    note: 捕获

  - en: scope
    classical: 域
    domain: programming
    note: 作用域

  - en: closure
    classical: 闭
    domain: programming
    note: 闭包

  - en: binding
    classical: 绑
    domain: programming
    note: 绑定

  - en: this
    classical: 此
    domain: programming
    note: this

  - en: self
    classical: 自
    domain: programming
    note: self

  - en: super
    classical: 父
    domain: programming
    note: super

  - en: init
    classical: 初
    domain: programming
    note: 初始化

  - en: constructor
    classical: 构
    domain: programming
    note: 构造函数

  - en: destructor
    classical: 析
    domain: programming
    note: 析构函数

  - en: property
    classical: 性
    domain: programming
    note: 属性

  - en: attribute
    classical: 性
    domain: programming
    note: 属性

  - en: annotation
    classical: 注
    domain: programming
    note: 注解

  - en: comment
    classical: 注
    domain: programming
    note: 注释

  - en: refactoring
    classical: 重
    domain: programming
    note: 重构

  # ========== 通用高频词汇 ==========
  - en: think
    classical: 思
    domain: common
    note: 想

  - en: know
    classical: 知
    domain: common
    note: 知道

  - en: want
    classical: 欲
    domain: common
    note: 想要

  - en: need
    classical: 需
    domain: common
    note: 需要

  - en: feel
    classical: 感
    domain: common
    note: 感觉

  - en: see
    classical: 见
    domain: common
    note: 看见

  - en: hear
    classical: 闻
    domain: common
    note: 听见

  - en: say
    classical: 言
    domain: common
    note: 说

  - en: tell
    classical: 告
    domain: common
    note: 告诉

  - en: ask
    classical: 问
    domain: common
    note: 问

  - en: give
    classical: 给
    domain: common
    note: 给

  - en: take
    classical: 取
    domain: common
    note: 取

  - en: come
    classical: 来
    domain: common
    note: 来

  - en: go
    classical: 去
    domain: common
    note: 去

  - en: look
    classical: 看
    domain: common
    note: 看

  - en: find
    classical: 觅
    domain: common
    note: 找到

  - en: learn
    classical: 学
    domain: common
    note: 学习

  - en: understand
    classical: 悟
    domain: common
    note: 理解

  - en: remember
    classical: 记
    domain: common
    note: 记住

  - en: forget
    classical: 忘
    domain: common
    note: 忘记

  - en: love
    classical: 爱
    domain: common
    note: 爱

  - en: hate
    classical: 恨
    domain: common
    note: 恨

  - en: hope
    classical: 望
    domain: common
    note: 希望

  - en: fear
    classical: 惧
    domain: common
    note: 恐惧

  - en: try
    classical: 试
    domain: common
    note: 尝试

  - en: manage
    classical: 管
    domain: common
    note: 管理

  - en: control
    classical: 控
    domain: common
    note: 控制

  - en: measure
    classical: 量
    domain: common
    note: 测量

  - en: calculate
    classical: 算
    domain: common
    note: 计算

  - en: compare
    classical: 比
    domain: common
    note: 比较

  - en: choose
    classical: 择
    domain: common
    note: 选择

  - en: decide
    classical: 决
    domain: common
    note: 决定

  - en: explain
    classical: 解
    domain: common
    note: 解释

  - en: describe
    classical: 述
    domain: common
    note: 描述

  - en: show
    classical: 示
    domain: common
    note: 显示

  - en: hide
    classical: 隐
    domain: common
    note: 隐藏

  - en: save
    classical: 存
    domain: common
    note: 保存

  - en: load
    classical: 载
    domain: common
    note: 加载

  - en: open
    classical: 开
    domain: common
    note: 打开

  - en: close
    classical: 合
    domain: common
    note: 关闭

  - en: read
    classical: 读
    domain: common
    note: 读

  - en: write
    classical: 写
    domain: common
    note: 写

  - en: copy
    classical: 复
    domain: common
    note: 复制

  - en: move
    classical: 移
    domain: common
    note: 移动

  - en: delete
    classical: 删
    domain: common
    note: 删除

  - en: create
    classical: 造
    domain: common
    note: 创建

  - en: update
    classical: 更
    domain: common
    note: 更新

  - en: change
    classical: 变
    domain: common
    note: 改变

  - en: send
    classical: 送
    domain: common
    note: 发送

  - en: receive
    classical: 收
    domain: common
    note: 接收

  - en: request
    classical: 请
    domain: common
    note: 请求

  - en: respond
    classical: 应
    domain: common
    note: 响应

  - en: wait
    classical: 待
    domain: common
    note: 等待

  - en: stay
    classical: 留
    domain: common
    note: 停留

  - en: leave
    classical: 离
    domain: common
    note: 离开

  - en: join
    classical: 合
    domain: common
    note: 加入

  - en: separate
    classical: 分
    domain: common
    note: 分开

  - en: connect
    classical: 连
    domain: common
    note: 连接

  - en: disconnect
    classical: 断
    domain: common
    note: 断开

  - en: add
    classical: 加
    domain: common
    note: 添加

  - en: remove
    classical: 除
    domain: common
    note: 移除

  - en: contain
    classical: 含
    domain: common
    note: 包含

  - en: belong
    classical: 属
    domain: common
    note: 属于

  - en: belong_to
    classical: 属
    domain: common
    note: 属于

  - en: exist
    classical: 在
    domain: common
    note: 存在

  - en: appear
    classical: 现
    domain: common
    note: 出现

  - en: disappear
    classical: 隐
    domain: common
    note: 消失

  - en: happen
    classical: 发
    domain: common
    note: 发生

  - en: occur
    classical: 生
    domain: common
    note: 发生

  - en: become
    classical: 成
    domain: common
    note: 成为

  - en: remain
    classical: 留
    domain: common
    note: 保持

  - en: start
    classical: 始
    domain: common
    note: 开始

  - en: stop
    classical: 止
    domain: common
    note: 停止

  - en: continue
    classical: 续
    domain: common
    note: 继续

  - en: finish
    classical: 竟
    domain: common
    note: 完成

  - en: complete
    classical: 完
    domain: common
    note: 完成

  - en: success
    classical: 成
    domain: common
    note: 成功

  - en: fail
    classical: 败
    domain: common
    note: 失败

  - en: win
    classical: 胜
    domain: common
    note: 获胜

  - en: lose
    classical: 负
    domain: common
    note: 失败

  - en: solve
    classical: 解
    domain: common
    note: 解决

  - en: introduce
    classical: 引
    domain: common
    note: 介绍

  - en: develop
    classical: 发
    domain: common
    note: 开发

  - en: grow
    classical: 长
    domain: common
    note: 成长

  - en: decrease
    classical: 减
    domain: common
    note: 减少

  - en: increase
    classical: 增
    domain: common
    note: 增加

  - en: raise
    classical: 提
    domain: common
    note: 提高

  - en: drop
    classical: 降
    domain: common
    note: 下降

  - en: rise
    classical: 升
    domain: common
    note: 上升

  - en: fall
    classical: 落
    domain: common
    note: 下降

  - en: push
    classical: 推
    domain: common
    note: 推

  - en: pull
    classical: 拉
    domain: common
    note: 拉

  - en: throw
    classical: 抛
    domain: common
    note: 抛

  - en: catch
    classical: 接
    domain: common
    note: 接

  - en: hit
    classical: 击
    domain: common
    note: 击

  - en: cut
    classical: 切
    domain: common
    note: 切

  - en: break
    classical: 破
    domain: common
    note: 打破

  - en: fix
    classical: 修
    domain: common
    note: 修理

  - en: wear
    classical: 穿
    domain: common
    note: 穿

  - en: wash
    classical: 洗
    domain: common
    note: 洗

  - en: clean
    classical: 洁
    domain: common
    note: 清洁

  - en: dirty
    classical: 秽
    domain: common
    note: 脏

  - en: dry
    classical: 干
    domain: common
    note: 干

  - en: wet
    classical: 湿
    domain: common
    note: 湿

  - en: hot
    classical: 热
    domain: common
    note: 热

  - en: cold
    classical: 寒
    domain: common
    note: 冷

  - en: warm
    classical: 暖
    domain: common
    note: 暖

  - en: cool
    classical: 凉
    domain: common
    note: 凉

  - en: bright
    classical: 辉
    domain: common
    note: 明亮

  - en: dark
    classical: 暗
    domain: common
    note: 暗

  - en: loud
    classical: 响
    domain: common
    note: 响

  - en: quiet
    classical: 静
    domain: common
    note: 静

  - en: soft
    classical: 柔
    domain: common
    note: 软

  - en: hard
    classical: 硬
    domain: common
    note: 硬

  - en: smooth
    classical: 滑
    domain: common
    note: 光滑

  - en: rough
    classical: 糙
    domain: common
    note: 粗糙

  - en: heavy
    classical: 重
    domain: common
    note: 重

  - en: light
    classical: 轻
    domain: common
    note: 轻

  - en: full
    classical: 盈
    domain: common
    note: 满

  - en: empty
    classical: 空
    domain: common
    note: 空

  - en: new
    classical: 新
    domain: common
    note: 新

  - en: old
    classical: 旧
    domain: common
    note: 旧

  - en: young
    classical: 幼
    domain: common
    note: 年轻

  - en: first
    classical: 首
    domain: common
    note: 第一

  - en: last
    classical: 末
    domain: common
    note: 最后

  - en: next
    classical: 次
    domain: common
    note: 下一个

  - en: previous
    classical: 前
    domain: common
    note: 上一个

  - en: early
    classical: 早
    domain: common
    note: 早

  - en: late
    classical: 迟
    domain: common
    note: 迟

  - en: fast
    classical: 疾
    domain: common
    note: 快

  - en: slow
    classical: 徐
    domain: common
    note: 慢

  - en: easy
    classical: 易
    domain: common
    note: 容易

  - en: difficult
    classical: 难
    domain: common
    note: 难

  - en: simple
    classical: 简
    domain: common
    note: 简单

  - en: complex
    classical: 繁
    domain: common
    note: 复杂

  - en: clear
    classical: 明
    domain: common
    note: 清楚

  - en: true
    classical: 真
    domain: common
    note: 真

  - en: false
    classical: 伪
    domain: common
    note: 假

  - en: right
    classical: 对
    domain: common
    note: 正确

  - en: wrong
    classical: 误
    domain: common
    note: 错误

  - en: good
    classical: 善
    domain: common
    note: 好

  - en: bad
    classical: 恶
    domain: common
    note: 坏

  - en: better
    classical: 佳
    domain: common
    note: 更好

  - en: best
    classical: 最
    domain: common
    note: 最好

  - en: big
    classical: 大
    domain: common
    note: 大

  - en: small
    classical: 小
    domain: common
    note: 小

  - en: large
    classical: 巨
    domain: common
    note: 大

  - en: huge
    classical: 宏
    domain: common
    note: 巨大

  - en: tiny
    classical: 微
    domain: common
    note: 微小

  - en: wide
    classical: 广
    domain: common
    note: 宽

  - en: narrow
    classical: 窄
    domain: common
    note: 窄

  - en: thick
    classical: 厚
    domain: common
    note: 厚

  - en: thin
    classical: 薄
    domain: common
    note: 薄

  - en: high
    classical: 高
    domain: common
    note: 高

  - en: low
    classical: 卑
    domain: common
    note: 低

  - en: long
    classical: 长
    domain: common
    note: 长

  - en: short
    classical: 短
    domain: common
    note: 短

  - en: strong
    classical: 强
    domain: common
    note: 强

  - en: weak
    classical: 弱
    domain: common
    note: 弱

  - en: rich
    classical: 富
    domain: common
    note: 富

  - en: poor
    classical: 贫
    domain: common
    note: 贫

  - en: happy
    classical: 乐
    domain: common
    note: 快乐

  - en: sad
    classical: 悲
    domain: common
    note: 悲伤

  - en: angry
    classical: 怒
    domain: common
    note: 生气

  - en: calm
    classical: 静
    domain: common
    note: 平静

  - en: busy
    classical: 忙
    domain: common
    note: 忙

  - en: free
    classical: 闲
    domain: common
    note: 空闲

  - en: safe
    classical: 安
    domain: common
    note: 安全

  - en: dangerous
    classical: 危
    domain: common
    note: 危险

  - en: healthy
    classical: 康
    domain: common
    note: 健康

  - en: sick
    classical: 病
    domain: common
    note: 病

  - en: alive
    classical: 生
    domain: common
    note: 活着

  - en: dead
    classical: 死
    domain: common
    note: 死

  - en: important
    classical: 要
    domain: common
    note: 重要

  - en: necessary
    classical: 必
    domain: common
    note: 必要

  - en: possible
    classical: 可
    domain: common
    note: 可能

  - en: impossible
    classical: 不
    domain: common
    note: 不可能

  - en: probable
    classical: 也许
    domain: common
    note: 很可能

  - en: certain
    classical: 定
    domain: common
    note: 确定

  - en: ready
    classical: 备
    domain: common
    note: 准备好

  - en: willing
    classical: 愿
    domain: common
    note: 愿意

  - en: able
    classical: 能
    domain: common
    note: 能够

  - en: correct
    classical: 正
    domain: common
    note: 正确

  - en: incorrect
    classical: 误
    domain: common
    note: 不正确

  - en: different
    classical: 异
    domain: common
    note: 不同

  - en: same
    classical: 同
    domain: common
    note: 相同

  - en: special
    classical: 特
    domain: common
    note: 特殊

  - en: normal
    classical: 常
    domain: common
    note: 正常

  - en: original
    classical: 原
    domain: common
    note: 原始

  - en: final
    classical: 终
    domain: common
    note: 最终

  - en: whole
    classical: 全
    domain: common
    note: 整个

  - en: part
    classical: 部
    domain: common
    note: 部分

  - en: single
    classical: 单
    domain: common
    note: 单个

  - en: together
    classical: 共
    domain: common
    note: 一起

  - en: alone
    classical: 独
    domain: common
    note: 单独

  - en: always
    classical: 永
    domain: common
    note: 永远

  - en: never
    classical: 未
    domain: common
    note: 从不

  - en: often
    classical: 常
    domain: common
    note: 经常

  - en: sometimes
    classical: 偶
    domain: common
    note: 有时

  - en: usually
    classical: 通
    domain: common
    note: 通常

  - en: maybe
    classical: 或
    domain: common
    note: 也许

  - en: perhaps
    classical: 或
    domain: common
    note: 或许

  - en: probably
    classical: 大
    domain: common
    note: 很可能

  - en: indeed
    classical: 确
    domain: common
    note: 确实

  - en: really
    classical: 实
    domain: common
    note: 真的

  - en: almost
    classical: 几
    domain: common
    note: 几乎

  - en: quite
    classical: 颇
    domain: common
    note: 相当

  - en: very
    classical: 甚
    domain: common
    note: 很

  - en: too
    classical: 亦
    domain: common
    note: 也

  - en: only
    classical: 唯
    domain: common
    note: 只

  - en: even
    classical: 连
    domain: common
    note: 甚至

  - en: still
    classical: 仍
    domain: common
    note: 仍然

  - en: already
    classical: 已
    domain: common
    note: 已经

  - en: yet
    classical: 尚
    domain: common
    note: 尚

  - en: now
    classical: 今
    domain: common
    note: 现在

  - en: then
    classical: 则
    domain: common
    note: 那时

  - en: soon
    classical: 即
    domain: common
    note: 很快

  - en: immediately
    classical: 即
    domain: common
    note: 立即

  - en: slowly
    classical: 徐
    domain: common
    note: 慢慢地

  - en: quickly
    classical: 速
    domain: common
    note: 快速地

  - en: recently
    classical: 近
    domain: common
    note: 最近

  - en: before
    classical: 前
    domain: common
    note: 之前

  - en: after
    classical: 后
    domain: common
    note: 之后

  - en: during
    classical: 间
    domain: common
    note: 期间

  - en: between
    classical: 间
    domain: common
    note: 之间

  - en: among
    classical: 中
    domain: common
    note: 其中

  - en: inside
    classical: 内
    domain: common
    note: 内部

  - en: outside
    classical: 外
    domain: common
    note: 外部

  - en: above
    classical: 上
    domain: common
    note: 上方

  - en: below
    classical: 下
    domain: common
    note: 下方

  - en: here
    classical: 此
    domain: common
    note: 这里

  - en: there
    classical: 彼
    domain: common
    note: 那里

  - en: where
    classical: 何
    domain: common
    note: 哪里

  - en: when
    classical: 何
    domain: common
    note: 何时

  - en: what
    classical: 何
    domain: common
    note: 什么

  - en: which
    classical: 哪
    domain: common
    note: 哪个

  - en: who
    classical: 谁
    domain: common
    note: 谁

  - en: why
    classical: 何
    domain: common
    note: 为什么

  - en: how
    classical: 何
    domain: common
    note: 如何

  - en: because
    classical: 因
    domain: common
    note: 因为

  - en: therefore
    classical: 故
    domain: common
    note: 因此

  - en: however
    classical: 然
    domain: common
    note: 然而

  - en: although
    classical: 虽
    domain: common
    note: 虽然

  - en: if
    classical: 若
    domain: common
    note: 如果

  - en: unless
    classical: 除
    domain: common
    note: 除非

  - en: whether
    classical: 是否
    domain: common
    note: 是否

  - en: and
    classical: 与
    domain: common
    note: 和

  - en: or
    classical: 或
    domain: common
    note: 或

  - en: but
    classical: 然
    domain: common
    note: 但是

  - en: yet
    classical: 仍
    domain: common
    note: 然而

  - en: so
    classical: 故
    domain: common
    note: 所以

  - en: thus
    classical: 是
    domain: common
    note: 因此

  - en: hence
    classical: 故
    domain: common
    note: 因此
```

- [ ] **Step 2: 验证 YAML 格式**

```bash
D:\anaconda\envs\torch128\python.exe -c "
import yaml
with open('J:/Main_AIproject/promote2classical/dict/dictionary.yml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
entries = data.get('entries', [])
print(f'Total entries: {len(entries)}')
print(f'Sample: {entries[0]}')
"
```
预期输出：`Total entries: 300+`

- [ ] **Step 3: 提交**

```bash
git add dict/dictionary.yml
git commit -m "feat: add dictionary.yml with 300+ entries across ai/programming/common domains

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 3: 创建 dict/__init__.py 加载模块

**Files:**
- Create: `dict/__init__.py`
- Test: `tests/test_yaml_dict.py`

- [ ] **Step 1: 创建 tests/test_yaml_dict.py**

```python
"""测试 YAML 词典加载"""

import pytest
from pathlib import Path
import sys

# 确保 dict 包在路径中
sys.path.insert(0, str(Path(__file__).parent.parent))

from promote2classical.dict import get_merged_dict, translate


class TestMergedDictionary:
    """测试合并词典"""

    def test_merged_dict_not_empty(self):
        """测试合并词典非空"""
        merged = get_merged_dict()
        assert len(merged) > 200, f"Expected >200 entries, got {len(merged)}"

    def test_yaml_overrides_builtin(self):
        """测试 YAML 可覆盖 builtin"""
        # 如果 YAML 中有覆盖，会用 YAML 的值
        result = translate("model")
        assert result == "模"

    def test_new_entries_from_yaml(self):
        """测试 YAML 新增条目"""
        # 只有 YAML 有的词
        result = translate("transformer")
        assert result == "变"

    def test_translate_lowercase(self):
        """测试翻译大小写处理"""
        result = translate("MODEL")
        assert result == "模"

    def test_translate_whitespace(self):
        """测试空白字符"""
        result = translate("  model  ")
        assert result == "模"

    def test_unknown_word(self):
        """测试未知词返回原词"""
        result = translate("xyznonexistentword")
        assert result == "xyznonexistentword"
```

- [ ] **Step 2: 创建 dict/__init__.py**

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


# 向后兼容：导出 builtin 词典
EN2CLASSICAL_BUILTIN = EN2CLASSICAL_BUILTIN
```

- [ ] **Step 3: 运行测试验证**

```bash
cd J:/Main_AIproject/promote2classical && D:\anaconda\envs\torch128\python.exe -m pytest tests/test_yaml_dict.py -v
```
预期：所有测试 PASS

- [ ] **Step 4: 提交**

```bash
git add dict/__init__.py tests/test_yaml_dict.py
git commit -m "feat: add dict loader with YAML support and merged dictionary

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 4: 更新 core.py 导入

**Files:**
- Modify: `core.py:9`（`from .dict.builtin import` 改为 `from .dict import`）

- [ ] **Step 1: 更新 core.py**

将第 9 行：
```python
from .dict.builtin import EN2CLASSICAL_BUILTIN
```
改为：
```python
from .dict import get_merged_dict
```

同时将 `Translator.translate()` 方法中的查词逻辑从查 `EN2CLASSICAL_BUILTIN` 改为 `get_merged_dict()`。

具体改动：
- 第 55-56 行：将 `if word in EN2CLASSICAL_BUILTIN` 改为 `merged = get_merged_dict(); if word in merged`
- 第 59 行：将 `if self.cache and word in self._cache` 保持不变（缓存逻辑不变）

- [ ] **Step 2: 验证**

```bash
D:\anaconda\envs\torch128\python.exe -c "from promote2classical import Translator; t = Translator(); print(t.translate('model')); print(t.translate('transformer'))"
```
预期：`模` 和 `变`

- [ ] **Step 3: 提交**

```bash
git add core.py
git commit -m "refactor: use merged dict from dict package in core.py

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 5: 更新 promote2classical/__init__.py 导出

**Files:**
- Modify: `promote2classical/__init__.py`

- [ ] **Step 1: 添加导出**

在现有导出下添加：
```python
from .dict import translate, get_merged_dict
```

- [ ] **Step 2: 验证**

```bash
D:\anaconda\envs\torch128\python.exe -c "from promote2classical import translate, get_merged_dict; print(len(get_merged_dict())); print(translate('model'))"
```
预期：`300+` 和 `模`

- [ ] **Step 3: 提交**

```bash
git add promote2classical/__init__.py
git commit -m "feat: export dict functions from package root

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 6: 修复 pyproject.toml 占位符

**Files:**
- Modify: `pyproject.toml`

- [ ] **Step 1: 修复占位符**

将：
```toml
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
```
改为：
```toml
authors = [
    {name = "onluuqs", email = "onluuqs@users.noreply.github.com"}
]
```

将 `https://github.com/YOUR_USERNAME/promote2classical` 全部替换为 `https://github.com/onluuqs/promote2classical`

- [ ] **Step 2: 验证构建**

```bash
cd J:/Main_AIproject/promote2classical && pip install -e . 2>&1 | tail -5
```

- [ ] **Step 3: 提交**

```bash
git add pyproject.toml
git commit -m "fix: replace placeholder values in pyproject.toml

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 7: 运行完整测试套件

**Files:**
- Run: 所有测试

- [ ] **Step 1: 运行全部测试**

```bash
cd J:/Main_AIproject/promote2classical && D:\anaconda\envs\torch128\python.exe -m pytest tests/ -v
```

- [ ] **Step 2: 检查覆盖率**

```bash
cd J:/Main_AIproject/promote2classical && D:\anaconda\envs\torch128\python.exe -m pytest tests/ --cov=promote2classical --cov-report=term-missing 2>&1 | tail -20
```

- [ ] **Step 3: 验证词数**

```bash
D:\anaconda\envs\torch128\python.exe -c "
from promote2classical.dict import get_merged_dict
d = get_merged_dict()
print(f'Total entries: {len(d)}')
# 按分类统计（如果 YAML 有 domain 字段）
from promote2classical.dict import _load_merged
import yaml
with open('J:/Main_AIproject/promote2classical/dict/dictionary.yml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
counts = {}
for e in data.get('entries', []):
    domain = e.get('domain', 'unknown')
    counts[domain] = counts.get(domain, 0) + 1
print(f'By domain: {counts}')
"
```

预期：总计 600+（builtin 150 + YAML 300+ + builtin 修复重复后更精确）

- [ ] **Step 4: 提交**

```bash
git add tests/test_promote2classical.py  # 如有更新
git commit -m "test: run full test suite and verify coverage

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## 实施后检查清单

- [ ] builtin.py 重复 key 已修复
- [ ] dictionary.yml 存在且包含 300+ 词
- [ ] dict/__init__.py 加载逻辑正确
- [ ] core.py 使用合并词典
- [ ] promote2classical/__init__.py 导出正确
- [ ] pyproject.toml 占位符已修复
- [ ] 所有测试 PASS
- [ ] 词库总数 600+
- [ ] Git 提交记录完整
