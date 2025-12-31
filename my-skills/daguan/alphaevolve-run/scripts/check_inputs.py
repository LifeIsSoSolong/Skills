#!/usr/bin/env python3
"""
检查输入目录完整性并判断任务类型。

Usage:
    python check_inputs.py --input-dir /path/to/inputs
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple


# 文件要求定义
MLE_REQUIRED = ["agent.py", "train.csv", "test.csv"]
MLE_OPTIONAL = ["judge.py", "config.json", "task.goal"]

PROMPT_REQUIRED = [
    "agent.py",
    "train.jsonl",
    "test.jsonl",
    "generate_press_agent.py",
    "evaluate_press_agent.py",
]
PROMPT_OPTIONAL = ["judge.py", "config.json", "task.goal"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check input directory for AlphaEvolve")
    parser.add_argument("--input-dir", required=True, help="Path to input directory")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    return parser.parse_args()


def check_files(input_dir: Path, required: List[str], optional: List[str]) -> Dict[str, List[str]]:
    """检查文件存在性"""
    result = {
        "present": [],
        "missing_required": [],
        "missing_optional": [],
    }
    
    for f in required:
        if (input_dir / f).exists():
            result["present"].append(f)
        else:
            result["missing_required"].append(f)
    
    for f in optional:
        if (input_dir / f).exists():
            result["present"].append(f)
        else:
            result["missing_optional"].append(f)
    
    return result


def detect_task_type(input_dir: Path) -> Tuple[str, Dict]:
    """
    检测任务类型
    
    Returns:
        (task_type, details)
        task_type: "mle" | "prompt" | "unknown"
    """
    # 检查 MLE 特征文件
    has_csv = (input_dir / "train.csv").exists() and (input_dir / "test.csv").exists()
    
    # 检查 Prompt 特征文件
    has_jsonl = (input_dir / "train.jsonl").exists() and (input_dir / "test.jsonl").exists()
    has_press_agents = (
        (input_dir / "generate_press_agent.py").exists() and
        (input_dir / "evaluate_press_agent.py").exists()
    )
    
    if has_csv and not has_jsonl:
        return "mle", check_files(input_dir, MLE_REQUIRED, MLE_OPTIONAL)
    elif has_jsonl and has_press_agents:
        return "prompt", check_files(input_dir, PROMPT_REQUIRED, PROMPT_OPTIONAL)
    elif has_jsonl and not has_press_agents:
        # 有 jsonl 但缺少 press agent 文件
        return "prompt", check_files(input_dir, PROMPT_REQUIRED, PROMPT_OPTIONAL)
    elif has_csv and has_jsonl:
        # 同时有两种数据格式，需要用户确认
        return "unknown", {
            "reason": "Both CSV and JSONL data files found",
            "mle_check": check_files(input_dir, MLE_REQUIRED, MLE_OPTIONAL),
            "prompt_check": check_files(input_dir, PROMPT_REQUIRED, PROMPT_OPTIONAL),
        }
    else:
        return "unknown", {
            "reason": "Cannot determine task type from files",
            "files_found": [f.name for f in input_dir.iterdir() if f.is_file()],
        }


def validate_data_file(file_path: Path) -> Dict:
    """验证数据文件可读性"""
    result = {"valid": False, "rows": 0, "error": None}
    
    try:
        if file_path.suffix == ".csv":
            import csv
            with open(file_path, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                headers = next(reader, None)
                rows = sum(1 for _ in reader)
                result["valid"] = True
                result["rows"] = rows
                result["columns"] = headers
        elif file_path.suffix == ".jsonl":
            rows = 0
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        json.loads(line)  # 验证 JSON 格式
                        rows += 1
            result["valid"] = True
            result["rows"] = rows
    except Exception as e:
        result["error"] = str(e)
    
    return result


def main() -> int:
    args = parse_args()
    input_dir = Path(args.input_dir).resolve()
    
    if not input_dir.is_dir():
        print(f"[ERROR] Input directory does not exist: {input_dir}")
        return 1
    
    # 检测任务类型
    task_type, details = detect_task_type(input_dir)
    
    # 验证数据文件
    data_validation = {}
    if task_type == "mle":
        for f in ["train.csv", "test.csv"]:
            fp = input_dir / f
            if fp.exists():
                data_validation[f] = validate_data_file(fp)
    elif task_type == "prompt":
        for f in ["train.jsonl", "test.jsonl"]:
            fp = input_dir / f
            if fp.exists():
                data_validation[f] = validate_data_file(fp)
    
    # 输出结果
    result = {
        "input_dir": str(input_dir),
        "task_type": task_type,
        "file_check": details,
        "data_validation": data_validation,
    }
    
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"[INFO] Input directory: {input_dir}")
        print(f"[INFO] Detected task type: {task_type}")
        print()
        
        if task_type in ["mle", "prompt"]:
            if details["missing_required"]:
                print("[ERROR] Missing required files:")
                for f in details["missing_required"]:
                    print(f"  - {f}")
            else:
                print("[OK] All required files present")
            
            if details["missing_optional"]:
                print("[INFO] Missing optional files (can be co-created):")
                for f in details["missing_optional"]:
                    print(f"  - {f}")
            
            print()
            print("[INFO] Data file validation:")
            for f, v in data_validation.items():
                if v["valid"]:
                    print(f"  - {f}: OK ({v['rows']} rows)")
                else:
                    print(f"  - {f}: ERROR - {v['error']}")
        else:
            print(f"[WARN] {details.get('reason', 'Unknown reason')}")
            if "files_found" in details:
                print("[INFO] Files found:")
                for f in details["files_found"]:
                    print(f"  - {f}")
    
    # 返回状态码
    if task_type == "unknown":
        return 2
    if task_type in ["mle", "prompt"] and details.get("missing_required"):
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
