#!/usr/bin/env python3
"""
Agent Paper Digest v3 - 基于全网搜索的论文追踪技能
使用 StepFun Search 搜索最新Agent相关论文
"""

import subprocess
import re
from datetime import datetime
from typing import List, Dict

# Agent相关搜索关键词
SEARCH_QUERIES = [
    "Agent AI papers arXiv 2025 multi-agent LLM reasoning",
    "LLM agent framework arXiv 2025 tool use function calling",
    "Multi-agent collaboration arXiv 2025",
]

# 论文主题分类关键词
CATEGORIES = {
    'skill_evolution': ['skill', 'evolve', 'self-improving', 'autonomous', 'learning', 'scientist'],
    'multi_agent': ['multi-agent', 'collaboration', 'coordination', 'distributed', 'orchestrate'],
    'memory': ['memory', 'retrieval', 'knowledge', 'cognitive', 'context'],
    'safety': ['safety', 'security', 'alignment', 'robustness', 'trust'],
    'evaluation': ['benchmark', 'evaluation', 'assessment', 'metric', 'measuring'],
    'application': ['medical', 'healthcare', 'finance', 'coding', 'production'],
    'reasoning': ['reasoning', 'chain-of-thought', 'cot', 'inference', 'planning'],
    'general': []
}

# 分类标题映射
CAT_NAMES = {
    'skill_evolution': '🔥 技能自进化',
    'multi_agent': '🤝 多智能体系统',
    'memory': '🧠 记忆与认知',
    'safety': '🔒 安全与对齐',
    'evaluation': '📊 评估与基准',
    'application': '🏥 垂直应用',
    'reasoning': '🧩 推理与思维',
    'general': '📄 其他Agent研究'
}


def search_papers(query: str, n: int = 5) -> List[Dict]:
    """使用 StepFun Search 搜索论文"""
    papers = []
    
    try:
        # 调用 step-search skill
        result = subprocess.run(
            ['python3', '/Users/jyxc-dz-0100378/.stepclaw/skills/step-search/scripts/stepsearch.py', query, '--n', str(n)],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode == 0:
            papers = parse_search_output(result.stdout)
    except Exception as e:
        print(f"搜索出错: {e}")
    
    return papers


def parse_search_output(output: str) -> List[Dict]:
    """解析搜索输出"""
    papers = []
    lines = output.split('
')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # 匹配 [数字] 标题格式
        match = re.match(r'\[(\d+)\]\s*(.+)', line)
        if match:
            paper = {
                'index': match.group(1),
                'title': match.group(2).strip(),
                'url': '',
                'published': '',
                'summary': ''
            }
            
            # 读取后续行获取更多信息
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                
                # 遇到新的论文或结束符
                if next_line.startswith('[') and re.match(r'\[\d+\]', next_line):
                    break
                if next_line.startswith('🔍'):
                    break
                if next_line.startswith('==='):
                    i += 1
                    continue
                
                # 提取链接
                if next_line.startswith('🔗'):
                     url_match = re.search(r'https?://\S+', next_line)
                    if url_match:
                        paper['url'] = url_match.group(0)
                
                # 提取时间
                elif '🕐' in next_line:
                    time_match = re.search(r'(\d{4}-\d{2}-\d{2})', next_line)
                    if time_match:
                        paper['published'] = time_match.group(1)
                
                # 提取描述（非标签行）
                elif next_line and not next_line.startswith('#') and len(next_line) > 20:
                    if not paper['summary']:
                        paper['summary'] = next_line
                
                i += 1
            
            papers.append(paper)
            continue
        
        i += 1
    
    return papers


def categorize_paper(paper: Dict) -> str:
    """对论文进行分类"""
    text = (paper.get('title', '') + ' ' + paper.get('summary', '')).lower()
    
    scores = {}
    for category, keywords in CATEGORIES.items():
        if category == 'general':
            continue
        score = sum(1 for kw in keywords if kw in text)
        scores[category] = score
    
    if scores and max(scores.values()) > 0:
        return max(scores, key=scores.get)
    return 'general'


def generate_one_liner(paper: Dict) -> str:
    """生成一句话摘要"""
    summary = paper.get('summary', '')
    if summary and len(summary) > 10:
        # 取前80字符
        if len(summary) > 80:
            return summary[:80] + "..."
        return summary
    return "Agent相关研究"


def deduplicate_papers(papers: List[Dict]) -> List[Dict]:
    """去重论文"""
    seen_titles = set()
    unique_papers = []
    
    for paper in papers:
        title = paper.get('title', '').lower().strip()
        simple_title = re.sub(r'[^\w\s]', '', title)
        
        if simple_title and simple_title not in seen_titles:
            seen_titles.add(simple_title)
            unique_papers.append(paper)
    
    return unique_papers
