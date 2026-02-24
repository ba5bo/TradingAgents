# TradingAgents 系统架构分析文档

本目录包含TradingAgents系统的完整架构分析文档，所有图表均使用内置Mermaid语法，确保在VSCode 1.75+版本中能够正确渲染和实时预览。

## 文档结构

### 1. [TRADING_AGENTS_ARCHITECTURE_ANALYSIS.md](TRADING_AGENTS_ARCHITECTURE_ANALYSIS.md)
- **系统概述**: TradingAgents的整体设计理念和目标
- **核心Agent类**: 详细分析每个Agent的职责、输入输出和依赖关系
- **数据引用关系图**: 展示数据在各组件间的流动关系
- **工作流程图**: 完整的系统执行流程
- **提示词体系**: 各类Agent的prompt设计和特征分析
- **内存系统架构**: BM25记忆系统的实现和使用方式
- **条件逻辑控制**: 工作流的控制机制和参数配置
- **系统优势**: 系统的主要特色和优势

### 2. [ARCHITECTURE_DIAGRAM.md](ARCHITECTURE_DIAGRAM.md)
- **整体架构概览**: 系统的分层架构图
- **详细工作流图**: 时序图展示完整的决策过程
- **Agent间数据流向图**: 数据状态的传递和共享
- **内存系统交互图**: 记忆系统的查询和应用机制
- **条件控制逻辑图**: 辩论轮次和流程控制逻辑

### 3. [AGENT_RELATIONSHIP_MATRIX.md](AGENT_RELATIONSHIP_MATRIX.md)
- **Agent基本信息表**: 所有12个Agent的详细属性
- **数据依赖关系图**: Agent间的数据流向可视化
- **Agent间通信关系图**: 通信模式和交互方式
- **工具使用统计表**: 各Agent使用的具体工具
- **提示词特征分析表**: 不同类型Agent的prompt特点
- **内存系统使用情况**: 各Agent的内存使用模式
- **工作流控制参数**: 系统配置和控制参数

## 使用说明

### VSCode 预览
1. 确保您的VSCode版本为1.75或更高
2. 直接打开任何`.md`文件
3. Mermaid图表将自动渲染显示
4. 修改Mermaid代码后可实时查看效果

### 图表编辑
- 所有图表都使用标准Mermaid语法
- 可以直接在Markdown文件中编辑图表代码
- 支持graph TD、sequenceDiagram、flowchart等多种图表类型

### 维护建议
- 当系统架构发生变化时，请同步更新相关文档
- 保持Mermaid代码的简洁性和可读性
- 在添加新Agent时，请更新Agent关系矩阵

## 技术栈

- **框架**: LangGraph
- **内存系统**: BM25 (Best Matching 25) 算法
- **数据源**: Yahoo Finance, Alpha Vantage
- **LLM支持**: OpenAI, Anthropic, Google等多提供商支持

这些文档旨在帮助开发者和研究人员快速理解TradingAgents系统的架构设计和工作原理。