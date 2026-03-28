---
name: agent-paper-digest
displayName: 【agent-paper-digest】Agent论文追踪：每天自动追踪arXiv上Agent、Multi-Agent、Skill相关的最新论文
description: 🚀 科研人必备！自动全网搜索Agent/Multi-Agent/Skill最新论文，智能分类（必读/选读/速览），生成精美日报，支持定时推送到飞书/元宝/企微。告别手动刷arXiv，让AI帮你追踪前沿！
version: 1.0.4
type: skill
category: research
tags:
  - arxiv
  - agent
  - multi-agent
  - skill
  - paper
  - research
  - automation
  - cron
  - openclaw
author: MOMOZI
contributors:
  - MOMOZI
license: MIT
homepage: https://github.com/YOUR_USERNAME/agent-paper-digest
repository: https://github.com/YOUR_USERNAME/agent-paper-digest.git
longDescription: |
  Agent论文追踪技能，帮助研究者和开发者快速了解Agent领域的最新进展。
  
  核心功能：
  1. 全网搜索Agent/Multi-Agent/Skill相关论文
  2. 智能筛选和三级分类（必读/选读/速览）
  3. 按主题自动分类（技能进化、多智能体、记忆、安全等）
  4. 生成精美Markdown日报
  5. 支持定时任务自动推送到多平台
  
  关键词覆盖：agent, multi-agent, agentic, skill, tool use, function calling, 
  agent memory, agent safety, chain-of-thought, reasoning等。
---

功能特性

- 🔍 全网搜索 - 基于 StepFun Search，多源聚合
- 🎯 智能筛选 - 基于关键词识别Agent相关论文
- 📊 三级分类 - 🔴必读/🟡选读/🟢速览
- 📝 精美日报 - 格式化输出，支持多平台推送
- ⏰ 定时任务 - 支持cron自动执行
- 🔌 多平台 - 支持飞书/元宝/企微/钉钉

论文分类

分类
关键词
说明
🔥 技能自进化
skill, evolve, self-improving
Agent自动学习新技能
🤝 多智能体系统
multi-agent, collaboration
多Agent协作与协调
🧠 记忆与认知
memory, retrieval, cognitive
Agent记忆系统
🔒 安全与对齐
safety, security, alignment
Agent安全研究
📊 评估与基准
benchmark, evaluation
Agent评测方法
🏥 垂直应用
medical, finance, coding
领域应用
🧩 推理与思维
reasoning, chain-of-thought
推理能力

使用方法

# 新版：使用全网搜索（推荐）
python3 ~/.stepclaw/skills/agent-paper-digest/digest_search.py

# 旧版：使用arXiv API（可能不稳定）
python3 ~/.stepclaw/skills/agent-paper-digest/digest_v2.py

# 推送日报
python3 ~/.stepclaw/skills/agent-paper-digest/push_daily.py

定时任务

# 每天晚上9点自动推送
openclaw cron add --name "Agent论文日报" \
  --schedule "0 21 * * *" \
  --command "python3 ~/.stepclaw/skills/agent-paper-digest/digest_search.py"
