#!/usr/bin/env python3
"""检查 Agent 输出是否包含必需字段。不做内容判断，只做格式守门。"""
import sys

REQUIRED = ["诊断假设", "路径类型", "判断依据", "未知项"]

def validate(text: str) -> list[str]:
    return [f for f in REQUIRED if f not in text]

if __name__ == "__main__":
    text = sys.stdin.read()
    missing = validate(text)
    if missing:
        print("不合格，缺字段：" + "、".join(missing))
        sys.exit(1)
    print("通过")
