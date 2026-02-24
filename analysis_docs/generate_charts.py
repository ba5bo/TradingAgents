#!/usr/bin/env python3
"""
TradingAgents 图表生成脚本

此脚本包含所有需要转换为图片的Mermaid图表代码。
您可以将这些代码复制到Mermaid编辑器中生成对应的PNG图片。
"""

def get_mermaid_charts():
    """返回所有需要生成的Mermaid图表代码"""
    
    charts = {
        "system_architecture_overview": '''
graph TB
    subgraph "用户接口层"
        A[TradingAgentsGraph] --> B[propagate()]
    end
    
    subgraph "数据接入层"
        C[Yahoo Finance]
        D[Alpha Vantage]
        E[Data Interface Layer]
        C --> E
        D --> E
    end
    
    subgraph "工具服务层"
        E --> F[Stock Data Tools]
        E --> G[Indicator Tools]
        E --> H[Fundamental Tools]
        E --> I[News Tools]
    end
    
    subgraph "分析Agent层"
        F --> J[Market Analyst<br/>技术分析]
        G --> J
        I --> K[News Analyst<br/>宏观新闻]
        I --> L[Social Media Analyst<br/>舆情分析]
        H --> M[Fundamentals Analyst<br/>基本面分析]
    end
    
    subgraph "辩论Agent层"
        J --> N[Bull Researcher<br/>看涨观点]
        K --> N
        L --> N
        M --> N
        J --> O[Bear Researcher<br/>看跌观点]
        K --> O
        L --> O
        M --> O
    end
    
    subgraph "决策管理层"
        N --> P[Research Manager<br/>投资判决]
        O --> P
        P --> Q[Trader<br/>交易计划]
        Q --> R[Aggressive Analyst<br/>激进策略]
        Q --> S[Conservative Analyst<br/>保守策略]
        Q --> T[Neutral Analyst<br/>平衡策略]
        R --> U[Risk Manager<br/>最终决策]
        S --> U
        T --> U
    end
    
    subgraph "记忆系统"
        V[Bull Memory]
        W[Bear Memory]
        X[Trader Memory]
        Y[Invest Judge Memory]
        Z[Risk Manager Memory]
        V --> N
        W --> O
        X --> Q
        Y --> P
        Z --> U
    end
    
    B --> J
    B --> K
    B --> L
    B --> M
    U --> B
''',

        "detailed_workflow": '''
sequenceDiagram
    participant User
    participant Graph as Trading Graph
    box LightBlue Analysts
    participant Market as Market Analyst
    participant News as News Analyst
    participant Social as Social Media Analyst
    participant Fund as Fundamentals Analyst
    end
    box LightGreen Researchers
    participant Bull as Bull Researcher
    participant Bear as Bear Researcher
    end
    box LightYellow Managers
    participant RM as Research Manager
    participant Trader as Trader
    end
    box LightPink Risk Team
    participant Agg as Aggressive Analyst
    participant Con as Conservative Analyst
    participant Neu as Neutral Analyst
    participant Risk as Risk Manager
    end
    box LightGray Memories
    participant Mem as Memory System
    end

    User->>Graph: propagate("TICKER", "DATE")
    
    Note over Graph: 初始化状态
    
    par 并行分析阶段
        Graph->>Market: 技术面分析请求
        Graph->>News: 宏观新闻分析请求
        Graph->>Social: 舆情分析请求
        Graph->>Fund: 基本面分析请求
    end
    
    Market->>Graph: market_report
    News->>Graph: news_report
    Social->>Graph: sentiment_report
    Fund->>Graph: fundamentals_report
    
    Note over Graph: 分析完成，进入辩论阶段
    
    loop 投资辩论循环 (max_debate_rounds轮)
        Graph->>Bull: 启动看涨论证
        Bull->>Mem: 查询相似历史情况
        Bull->>Graph: bull_history + 当前论点
        
        Graph->>Bear: 启动看跌反驳
        Bear->>Mem: 查询相似历史情况
        Bear->>Graph: bear_history + 当前论点
    end
    
    Graph->>RM: 提交完整辩论记录
    RM->>Mem: 查询过往决策经验
    RM->>Graph: judge_decision + investment_plan
    
    Graph->>Trader: 投资计划执行
    Trader->>Mem: 查询交易历史经验
    Trader->>Graph: trader_investment_plan
    
    Note over Graph: 风险评估阶段
    
    loop 风险分析循环
        Graph->>Agg: 激进策略分析
        Agg->>Graph: aggressive_response
        
        Graph->>Con: 保守策略分析
        Con->>Graph: conservative_response
        
        Graph->>Neu: 平衡策略分析
        Neu->>Graph: neutral_response
    end
    
    Graph->>Risk: 风险综合评估
    Risk->>Mem: 查询风险管理经验
    Risk->>Graph: final_trade_decision
    
    Graph->>User: 返回最终决策
''',

        "data_flow_diagram": '''
graph LR
    subgraph "输入数据"
        INPUT[Ticker + Date]
    end
    
    subgraph "共享状态 (AgentState)"
        STATE[company_of_interest<br/>trade_date<br/>messages]
        REPORTS[market_report<br/>news_report<br/>sentiment_report<br/>fundamentals_report]
        DEBATE[investment_debate_state<br/>risk_debate_state]
        PLANS[investment_plan<br/>trader_investment_plan]
        DECISION[final_trade_decision]
    end
    
    subgraph "数据生产者"
        ANALYSTS[Analysts<br/>生成各类报告]
        RESEARCHERS[Researchers<br/>生成辩论历史]
        MANAGERS[Managers<br/>生成决策和计划]
    end
    
    subgraph "数据消费者"
        CONSUMERS[下游Agents<br/>消费上游数据]
    end
    
    INPUT --> STATE
    STATE --> ANALYSTS
    ANALYSTS --> REPORTS
    REPORTS --> RESEARCHERS
    RESEARCHERS --> DEBATE
    DEBATE --> MANAGERS
    REPORTS --> MANAGERS
    MANAGERS --> PLANS
    PLANS --> CONSUMERS
    MANAGERS --> DECISION
''',

        "memory_interaction": '''
graph TB
    subgraph "当前情境"
        CURR[Current Situation<br/>多报告合并文本]
    end
    
    subgraph "内存查询过程"
        QUERY[BM25相似度查询]
        MEMORIES[历史情境库]
        RESULTS[Top-N匹配结果]
    end
    
    subgraph "内存数据库"
        DB1[Situation 1<br/>Recommendation 1]
        DB2[Situation 2<br/>Recommendation 2]
        DB3[Situation 3<br/>Recommendation 3]
        DBN[Situation N<br/>Recommendation N]
    end
    
    subgraph "Agent应用"
        AGENT[Bull/Bear/Trader等Agent]
        PROMPT[增强提示词]
        RESPONSE[含历史经验的决策]
    end
    
    CURR --> QUERY
    QUERY --> MEMORIES
    MEMORIES --> DB1
    MEMORIES --> DB2
    MEMORIES --> DB3
    MEMORIES --> DBN
    QUERY --> RESULTS
    RESULTS --> PROMPT
    CURR --> PROMPT
    PROMPT --> AGENT
    AGENT --> RESPONSE
''',

        "conditional_logic": '''
graph TB
    subgraph "条件判断节点"
        CONDITION[Should Continue?]
    end
    
    subgraph "可能的后续动作"
        TOOLS[调用工具节点]
        CLEAR[清除消息节点]
        NEXT[下一个Agent]
        DEBATE_NEXT[继续辩论]
        DEBATE_END[结束辩论]
    end
    
    subgraph "判断依据"
        ROUND_COUNT[当前轮次计数]
        TOOL_CALLS[工具调用需求]
        DEBATE_STATUS[辩论状态]
        CONFIDENCE[置信度水平]
    end
    
    ROUND_COUNT --> CONDITION
    TOOL_CALLS --> CONDITION
    DEBATE_STATUS --> CONDITION
    CONFIDENCE --> CONDITION
    
    CONDITION --> TOOLS
    CONDITION --> CLEAR
    CONDITION --> NEXT
    CONDITION --> DEBATE_NEXT
    CONDITION --> DEBATE_END
''',

        "agent_data_dependencies": '''
graph TD
    %% 分析师层相互独立
    MA[Market Analyst] --> |技术分析报告| BR
    MA --> |技术分析报告| BE
    NA[News Analyst] --> |新闻分析报告| BR
    NA --> |新闻分析报告| BE
    SA[Social Media Analyst] --> |舆情分析报告| BR
    SA --> |舆情分析报告| BE
    FA[Fundamentals Analyst] --> |基本面分析报告| BR
    FA --> |基本面分析报告| BE
    
    %% 研究员层相互辩论
    BR[Bull Researcher] --> |看涨论点| BE
    BE[Bear Researcher] --> |看跌论点| BR
    
    %% 管理层收集信息
    BR --> |辩论历史| RM[Research Manager]
    BE --> |辩论历史| RM
    
    %% 交易层流程
    RM --> |投资计划| TR[Trader]
    TR --> |交易策略| AA[Aggressive Analyst]
    TR --> |交易策略| CA[Conservative Analyst]
    TR --> |交易策略| NA[Neutral Analyst]
    
    %% 风险管理层汇总
    AA --> |风险分析| RK[Risk Manager]
    CA --> |风险分析| RK
    NA --> |风险分析| RK
    
    %% 最终输出
    RK --> |最终决策| OUTPUT[Final Trade Decision]
''',

        "agent_communication_flow": '''
flowchart TD
    subgraph "分析师层 (并行执行)"
        MA[Market Analyst]
        NA[News Analyst]
        SA[Social Media Analyst]
        FA[Fundamentals Analyst]
    end
    
    subgraph "研究员层 (相互辩论)"
        BR[Bull Researcher]
        BE[Bear Researcher]
    end
    
    subgraph "管理层"
        RM[Research Manager]
        TR[Trader]
    end
    
    subgraph "风险分析层"
        AA[Aggressive Analyst]
        CA[Conservative Analyst]
        NA2[Neutral Analyst]
        RK[Risk Manager]
    end
    
    MA --> BR
    NA --> BR
    SA --> BR
    FA --> BR
    MA --> BE
    NA --> BE
    SA --> BE
    FA --> BE
    
    BR <--> BE
    
    BR --> RM
    BE --> RM
    
    RM --> TR
    
    TR --> AA
    TR --> CA
    TR --> NA2
    
    AA --> RK
    CA --> RK
    NA2 --> RK
    
    RK --> OUTPUT[Final Decision]
'''
    }
    
    return charts

def save_chart_codes():
    """保存图表代码到单独的文件"""
    import os
    charts = get_mermaid_charts()
    
    # 创建charts目录
    os.makedirs("charts", exist_ok=True)
    
    for chart_name, chart_code in charts.items():
        filename = f"charts/{chart_name}.mmd"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(chart_code.strip())
        print(f"已保存图表代码到: {filename}")

def print_usage():
    """打印使用说明"""
    print("""
TradingAgents 图表生成助手

使用方法:
1. 运行此脚本保存图表代码: python generate_charts.py
2. 将生成的 .mmd 文件内容复制到以下任一平台:
   - Mermaid Live Editor: https://mermaid.live/
   - VSCode Mermaid插件
   - mermaid-cli 工具
3. 导出为PNG格式图片
4. 将图片保存到相应目录

生成的文件:
- charts/system_architecture_overview.mmd
- charts/detailed_workflow.mmd  
- charts/data_flow_diagram.mmd
- charts/memory_interaction.mmd
- charts/conditional_logic.mmd
- charts/agent_data_dependencies.mmd
- charts/agent_communication_flow.mmd
""")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "save":
        save_chart_codes()
        print("\n所有图表代码已保存完成！")
    else:
        print_usage()
        print("\n要保存图表代码，请运行: python generate_charts.py save")