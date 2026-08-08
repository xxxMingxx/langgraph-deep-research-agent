# Deep Research Agent

基于 **LangGraph + LLM + RAG** 构建的深度研究智能体（Deep Research Agent）。

本项目实现了一个能够自主进行信息检索、知识增强、工具调用和研究总结的 AI Agent 系统。

核心技术：

- LangGraph：Agent 工作流编排与状态管理
- Multi-Agent：多智能体协作架构
- RAG（Retrieval Augmented Generation）：检索增强生成
- ChromaDB：向量数据库
- DeepSeek LLM：大语言模型推理


---

# 项目介绍 (Introduction)

传统 LLM 在复杂任务中存在：

- 知识更新不及时
- 容易产生幻觉（Hallucination）
- 缺少外部知识支撑
- 难以完成多步骤任务


因此，本项目构建 Deep Research Agent，使 LLM 能够：

1. 理解用户研究任务
2. 自主选择工具
3. 检索外部信息或本地知识库
4. 对搜索结果进行分析和反思
5. 自动生成结构化研究报告


---

# 系统架构 (Architecture)


```
                User Query

                    |

                    v

            Research Agent

                    |

        +-----------+-----------+

        |                       |

        v                       v


   Tavily Search          Chroma RAG

   Web Search             Knowledge Retrieval


        |                       |

        +-----------+-----------+

                    |

                    v

              Think Tool

              Reflection

                    |

                    v

          Research Compression

                    |

                    v

            Final Report

```


---

# 核心功能 (Features)


## 1. LangGraph Agent Workflow


本项目使用 LangGraph 构建 Agent 工作流。


LangGraph 核心组件：

- State
- Node
- Edge
- Conditional Routing


通过 Graph 结构管理 Agent 执行流程。


当前 Research Agent 流程：


```
START

  |

LLM Decision

  |

Tool Calling

  |

Observation

  |

Continue Research / Generate Report

  |

END

```


其中 State 用于保存：

- 用户研究主题
- Agent 消息历史
- 工具返回结果
- 研究过程信息
- 最终输出


---

# 2. Agent Tool Calling


Agent 可以根据任务自主选择工具。


目前支持：


## Tavily Search Tool


用于获取外部网络信息。

适合：

- 最新资讯
- 外部资料
- 网络搜索


---


## Chroma RAG Search Tool


用于查询本地知识库。


RAG Pipeline：


```
Documents

    |

Text Splitting

    |

Embedding

    |

Vector Database

    |

Similarity Search

    |

LLM Generation

```


Embedding Model：

```
BAAI/bge-small-zh-v1.5
```


Vector Database：

```
ChromaDB
```


---

## Think Tool


用于 Agent 自我反思。


Agent 会根据当前结果判断：

- 是否需要继续搜索
- 是否已经获得足够信息
- 下一步应该执行什么操作


---

# 3. RAG Knowledge Base


本项目实现完整 RAG 流程。


数据流程：


```
Markdown Documents

        |

RecursiveCharacterTextSplitter

        |

Embedding Model

        |

Chroma Vector Database

        |

Similarity Retrieval

        |

LLM Response

```


知识库支持 Metadata：


```json
{
  "source": "langgraph.md",
  "category": "knowledge_base"
}
```


例如：

```
knowledge_base/

├── langgraph.md

├── rag.md

└── agent.md

```


---

# 4. Multi-Agent Architecture


项目采用模块化 Agent 设计。


目录结构：


```
deep_research

├── agents

│
├── research_agent.py

├── draft_agent.py

├── evaluator_agent.py

├── red_team_agent.py

└── supervisor.py

```


不同 Agent 负责不同任务：


| Agent | Responsibility |
|---|---|
| Research Agent | 信息搜索与研究分析 |
| Draft Agent | 初始报告生成 |
| Evaluator Agent | 输出质量评估 |
| Red Team Agent | 结果批判与优化 |
| Supervisor | Agent 流程协调 |


---

# Example


输入：

```
什么是 LangGraph，它如何用于构建 AI Agent？
```


Agent 执行过程：

1. 分析研究任务

2. 调用 Chroma RAG：

```
LangGraph
RAG
AI Agent Architecture
```


3. 获取知识库信息

4. Think Tool 进行反思

5. 判断是否继续检索

6. 生成最终研究报告


---

# Technology Stack


## Agent Framework

- LangGraph
- LangChain


## LLM

- DeepSeek


## RAG

- ChromaDB
- HuggingFace Embedding
- BAAI/bge-small-zh-v1.5


## Search

- Tavily Search API


## Programming

- Python


---

# Project Structure


```
deep-research-agent

├── deep_research

│
├── agents

├── rag

├── tools

├── states

└── prompts


├── knowledge_base


├── test_agent.py

├── test_rag.py

├── requirements.txt

└── README.md

```


---

# Installation


Create environment:


```bash
python -m venv .venv
```


Install dependencies:


```bash
pip install -r requirements.txt
```


---

# Build Knowledge Base


运行：


```bash
python -m deep_research.rag.ingestion
```


生成 Chroma Vector Database。


---

# Run Agent


运行：


```bash
python test_agent.py
```


Agent 将自动完成：

- Tool Selection
- Knowledge Retrieval
- Reasoning
- Research Summarization


---

# Future Improvements


计划增加：

- PDF 文档解析
- 更多数据源接入
- Agent 自动评测
- 长期 Memory
- Web Interface


---

# Summary


本项目实现了一个完整的 LLM Agent 应用。


核心设计：

**LangGraph 负责流程编排（Workflow），  
RAG 负责知识增强（Knowledge），  
LLM 负责推理决策（Reasoning）。**


通过 Agent 自主工具调用和知识检索，实现了一个能够完成复杂研究任务的 Deep Research Agent。

![alt text](image.png)

## 👨‍💻 Author

**Logic**

Master of Artificial Intelligence

Monash University 

GitHub:
https://github.com/xxxMingxx
