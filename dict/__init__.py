"""词典加载模块"""

from pathlib import Path
from typing import Optional

import yaml

from .builtin import EN2CLASSICAL_BUILTIN

# 用户词典路径
_DICT_PATH = Path(__file__).parent / "dictionary.yml"

# 合并后词典（lazy加载）
_MERGED: Optional[dict[str, str]] = None


def _load_merged() -> dict[str, str]:
    """加载并合并内置词典和用户词典"""
    merged = dict(EN2CLASSICAL_BUILTIN)

    if _DICT_PATH.exists():
        with open(_DICT_PATH, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if data and "entries" in data:
            for entry in data["entries"]:
                en = entry.get("en", "").strip().lower()
                classical = entry.get("classical", "").strip()
                if en and classical:
                    merged[en] = classical

    return merged


def get_merged_dict() -> dict[str, str]:
    """获取合并后的完整词典"""
    global _MERGED
    if _MERGED is None:
        _MERGED = _load_merged()
    return _MERGED


def translate(word: str) -> str:
    """查词函数"""
    return get_merged_dict().get(word.strip().lower(), word)


# 向后兼容：导出 builtin 词典
EN2CLASSICAL_BUILTIN = EN2CLASSICAL_BUILTIN
