#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
章节内容结构检查脚本
检查所有章节文件是否符合内容结构标准
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple

# 章节类型判断规则
SYNTAX_KEYWORDS = ['声明', '类型', '运算符', '控制', '函数', '对象', '数组', '字符串', '集合', '错误', '类', '继承', 'Proxy', 'Reflect']
CONFIG_KEYWORDS = ['安装', '配置', 'tsconfig', 'IDE', '编译器']
TOOL_KEYWORDS = ['执行', '编译', '工具']
PRACTICAL_KEYWORDS = ['第一个', '实践', '案例']
REFERENCE_KEYWORDS = ['stringify', 'parse', '方法', 'API']
BEST_PRACTICES_KEYWORDS = ['最佳实践', '规范', '标准']
COMPARATIVE_KEYWORDS = ['对比', 'vs', '比较']
CONCEPTUAL_KEYWORDS = ['概述', '历史', '发展', '生态系统']

# 必需要素
REQUIRED_SECTIONS = {
    'syntax': ['概述', '特性', '语法', '基本用法', '代码示例', '使用场景', '注意事项', '最佳实践'],
    'config': ['概述', '特性', '配置步骤', '注意事项', '常见问题'],
    'tool': ['概述', '特性', '基本用法', '使用场景', '注意事项', '常见问题', '最佳实践'],
    'practical': ['概述', '实践步骤', '完整代码示例', '输出结果说明', '注意事项', '练习任务'],
    'reference': ['概述', '定义', '示例', '使用场景'],
    'best_practices': ['概述', '实践建议', '代码示例', '最佳实践', '注意事项'],
    'comparative': ['概述', '对比分析', '使用建议', '注意事项'],
    'conceptual': ['概述', '核心概念', '总结']
}

def detect_chapter_type(filename: str, content: str) -> str:
    """检测章节类型"""
    filename_lower = filename.lower()
    content_lower = content.lower()

    # 检查文件名和内容关键词
    if any(kw in filename_lower or kw in content_lower for kw in COMPARATIVE_KEYWORDS):
        return 'comparative'
    elif any(kw in filename_lower or kw in content_lower for kw in BEST_PRACTICES_KEYWORDS):
        return 'best_practices'
    elif any(kw in filename_lower or kw in content_lower for kw in REFERENCE_KEYWORDS):
        return 'reference'
    elif any(kw in filename_lower or kw in content_lower for kw in PRACTICAL_KEYWORDS):
        return 'practical'
    elif any(kw in filename_lower or kw in content_lower for kw in TOOL_KEYWORDS):
        return 'tool'
    elif any(kw in filename_lower or kw in content_lower for kw in CONFIG_KEYWORDS):
        return 'config'
    elif any(kw in filename_lower or kw in content_lower for kw in CONCEPTUAL_KEYWORDS):
        return 'conceptual'
    elif any(kw in filename_lower or kw in content_lower for kw in SYNTAX_KEYWORDS):
        return 'syntax'
    else:
        return 'syntax'  # 默认为语法性章节

def extract_sections(content: str) -> Set[str]:
    """提取章节中的所有二级标题"""
    pattern = r'^##\s+(.+)$'
    sections = set()
    for line in content.split('\n'):
        match = re.match(pattern, line)
        if match:
            section_name = match.group(1).strip()
            sections.add(section_name)
    return sections

def check_file(filepath: Path) -> Tuple[str, str, Set[str], List[str]]:
    """检查单个文件"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return 'error', str(e), set(), []

    filename = filepath.name
    chapter_type = detect_chapter_type(filename, content)
    sections = extract_sections(content)

    # 检查必需要素
    required = REQUIRED_SECTIONS.get(chapter_type, [])
    missing = [req for req in required if req not in sections]

    return chapter_type, filename, sections, missing

def check_directory(directory: Path) -> Dict:
    """检查目录下所有章节文件"""
    results = {
        'total': 0,
        'by_type': {},
        'missing_sections': {},
        'files': []
    }

    for md_file in directory.rglob('*.md'):
        if md_file.name == 'readme.md':
            continue

        results['total'] += 1
        chapter_type, filename, sections, missing = check_file(md_file)

        if chapter_type not in results['by_type']:
            results['by_type'][chapter_type] = 0
        results['by_type'][chapter_type] += 1

        if missing:
            if chapter_type not in results['missing_sections']:
                results['missing_sections'][chapter_type] = {}
            results['missing_sections'][chapter_type][filename] = missing

        results['files'].append({
            'path': str(md_file.relative_to(directory)),
            'type': chapter_type,
            'sections': list(sections),
            'missing': missing
        })

    return results

def generate_report(results: Dict, title: str) -> str:
    """生成审查报告"""
    report = f"# {title}\n\n"
    report += f"**审查日期**：2025-01-XX\n"
    report += f"**审查范围**：所有章节文件\n"
    report += f"**审查标准**：`.docs/ai-rules/12-content-structure-standards.md`\n\n"
    report += "---\n\n"

    report += f"## 审查统计\n\n"
    report += f"- **总文件数**：{results['total']}\n"
    report += f"- **章节类型分布**：\n"
    for chapter_type, count in results['by_type'].items():
        report += f"  - {chapter_type}：{count} 个\n"

    report += f"\n## 缺失必需要素统计\n\n"
    total_missing = 0
    for chapter_type, files in results['missing_sections'].items():
        report += f"### {chapter_type} 类型章节\n\n"
        report += f"- **缺失文件数**：{len(files)}\n"
        for filename, missing in files.items():
            total_missing += len(missing)
            report += f"  - `{filename}`：缺失 {', '.join(missing)}\n"
        report += "\n"

    report += f"\n## 详细文件清单\n\n"
    for file_info in results['files']:
        report += f"### {file_info['path']}\n\n"
        report += f"- **章节类型**：{file_info['type']}\n"
        if file_info['missing']:
            report += f"- **缺失要素**：{', '.join(file_info['missing'])}\n"
        else:
            report += f"- **状态**：✅ 符合标准\n"
        report += "\n"

    return report

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python check-all-sections.py <directory>")
        sys.exit(1)

    directory = Path(sys.argv[1])
    if not directory.exists():
        print(f"Error: Directory {directory} does not exist")
        sys.exit(1)

    results = check_directory(directory)
    report = generate_report(results, f"{directory.name} 章节内容结构审查报告")

    # 输出到项目根目录的 .docs/reviews
    project_root = Path(__file__).parent.parent.parent
    output_file = project_root / '.docs' / 'reviews' / f'{directory.name}-content-structure-review.md'
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"审查报告已生成：{output_file}")
