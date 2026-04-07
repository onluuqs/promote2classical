"""测试 YAML 词典加载"""

import pytest
from pathlib import Path
import sys

# 确保 dict 包在路径中
sys.path.insert(0, str(Path(__file__).parent.parent))

from promote2classical.dict import get_merged_dict, translate


class TestMergedDictionary:
    """测试合并词典"""

    def test_merged_dict_not_empty(self):
        """测试合并词典非空"""
        merged = get_merged_dict()
        assert len(merged) > 400, f"Expected >400 entries, got {len(merged)}"

    def test_yaml_overrides_builtin(self):
        """测试 YAML 可覆盖 builtin"""
        # YAML 中的词应该能查到
        result = translate("transformer")
        assert result == "变"

    def test_new_entries_from_yaml(self):
        """测试 YAML 新增条目"""
        result = translate("llama")
        assert result == "羊"

    def test_translate_lowercase(self):
        """测试翻译大小写处理"""
        result = translate("TRANSFORMER")
        assert result == "变"

    def test_translate_whitespace(self):
        """测试空白字符"""
        result = translate("  model  ")
        assert result == "模"

    def test_unknown_word(self):
        """测试未知词返回原词"""
        result = translate("xyznonexistentword")
        assert result == "xyznonexistentword"

    def test_builtin_still_works(self):
        """测试内置词典仍然可用"""
        result = translate("promote")
        assert result == "升"

    def test_ai_term(self):
        """测试 AI 术语翻译"""
        result = translate("attention")
        assert result == "注"

    def test_programming_term(self):
        """测试编程术语翻译"""
        result = translate("function")
        assert result == "函"

    def test_common_word(self):
        """测试通用词翻译"""
        result = translate("think")
        assert result == "思"
