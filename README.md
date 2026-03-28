# Agent-Paper-Digest
# 📚 Agent Paper Digest

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-green.svg)](https://openclawmp.cc)

> 🚀 **科研人必备神器** —— 让 AI 帮你追踪 Agent 领域最新论文，告别手动刷 arXiv！

## ✨ 核心特性

| 特性 | 说明 |
|------|------|
| 🔍 **全网搜索** | 基于 StepFun Search，不依赖单一数据源 |
| 🎯 **智能筛选** | 自动识别 Agent/Multi-Agent/Skill 相关论文 |
| 📊 **三级分类** | 🔴必读 / 🟡选读 / 🟢速览，快速定位重点 |
| 📝 **精美日报** | 自动生成格式化简报，支持多平台推送 |
| ⏰ **定时任务** | 支持 Cron 定时，每日自动推送 |
| 🔌 **多平台** | 支持飞书/元宝/企微/钉钉等主流 IM |

## 🚀 快速开始

### 安装
##### 通过 OpenClaw 水产市场安装
```bash
# 通过 OpenClaw 水产市场安装
openclawmp install skill/@u-ce6f93e8b7cd47febf93/agent-paper-digest
```

##### 或手动克隆
```bash
git clone https://github.com/YOUR_USERNAME/agent-paper-digest.git
cd agent-paper-digest
```

依赖

- Python 3.8+
- step-search Skill（用于全网搜索）

# 安装依赖 Skill
openclawmp install skill/step-search

# 使用
## 1. 手动执行

###  生成今日论文简报
python3 digest_search.py

###  推送到指定渠道
python3 push_daily.py yuanbao group:YOUR_GROUP_ID

## 2. Agent 调用


## 3. 定时任务（推荐）

###  每天晚上 9 点自动推送
openclaw cron add --name "Agent论文日报" \
  --schedule "0 21 * * *" \
  --command "python3 ~/.stepclaw/skills/agent-paper-digest/digest_search.py"
