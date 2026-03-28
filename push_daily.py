#!/usr/bin/env python3
"""
Agent Paper Digest - 日报推送脚本
生成论文简报并推送到指定渠道
"""

import subprocess
import sys
import os

# 默认配置
DEFAULT_CHANNEL = "yuanbao"
DEFAULT_TARGET = "group:652398102"  # 元宝群聊ID


def generate_briefing():
    """生成论文简报"""
    result = subprocess.run(
        ['python3', os.path.expanduser('~/.stepclaw/skills/agent-paper-digest/digest_search.py')],
        capture_output=True,
        text=True,
        timeout=120
    )
    
    if result.returncode == 0:
        # 从输出中提取简报部分（在 === 之后）
        output = result.stdout
        if '==================================================' in output:
            briefing = output.split('==================================================')[-1].strip()
            return briefing
    
    return None


def push_to_channel(briefing: str, channel: str = None, target: str = None):
    """推送到指定渠道"""
    channel = channel or DEFAULT_CHANNEL
    target = target or DEFAULT_TARGET
    
    # 使用 message 工具推送
    # 注意：这里需要在 Agent 环境中调用，直接执行无法使用 message 工具
    print(f"准备推送到 {channel}...")
    print(f"目标: {target}")
    print("
简报内容预览:")
    print("=" * 50)
    print(briefing[:500] + "..." if len(briefing) > 500 else briefing)
    
    return True


def main():
    """主函数"""
    print("🔍 生成论文简报...")
    briefing = generate_briefing()
    
    if briefing:
        print("✅ 简报生成成功")
        
        # 解析命令行参数
        channel = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CHANNEL
        target = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_TARGET
        
        # 推送
        push_to_channel(briefing, channel, target)
        
        # 保存到文件供后续推送
        output_file = os.path.expanduser('~/.stepclaw/workspace/daily_paper_briefing.txt')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(briefing)
        print(f"
💾 简报已保存: {output_file}")
        
        return briefing
    else:
        print("❌ 简报生成失败")
        return None


if __name__ == "__main__":
    main()
