"""测试模块"""

import pytest
from promote2classical import translate, Translator
from promote2classical.dict.builtin import EN2CLASSICAL_BUILTIN


class TestBuiltinDictionary:
    """测试内置词典"""

    def test_known_words(self):
        """测试已知词汇"""
        assert translate("promote") == "升"
        assert translate("increase") == "增"
        assert translate("good") == "善"
        assert translate("model") == "模"

    def test_case_insensitive(self):
        """测试大小写不敏感"""
        assert translate("PROMOTE") == "升"
        assert translate("Promote") == "升"
        assert translate("promote") == "升"

    def test_whitespace(self):
        """测试空白字符处理"""
        assert translate("  promote  ") == "升"
        assert translate("\tmodel\n") == "模"


class TestTranslatorClass:
    """测试Translator类"""

    def test_translate_known_word(self):
        """测试翻译已知词汇"""
        t = Translator()
        assert t.translate("enhance") == "强"

    def test_translate_unknown_word_no_api(self):
        """测试无API密钥时未知词汇返回原词"""
        t = Translator(api_key=None)
        result = t.translate("nonexistent_word_xyz")
        assert result == "nonexistent_word_xyz"

    def test_batch_translate(self):
        """测试批量翻译"""
        t = Translator()
        words = ["promote", "increase", "good"]
        results = t.batch_translate(words)
        assert results == ["升", "增", "善"]


class TestDictionaryCoverage:
    """测试词典覆盖"""

    def test_dictionary_not_empty(self):
        """测试词典非空"""
        assert len(EN2CLASSICAL_BUILTIN) > 50

    def test_all_values_are_chinese(self):
        """测试所有值都是中文"""
        for eng, classical in EN2CLASSICAL_BUILTIN.items():
            # 检查是否包含中文字符
            assert any('\u4e00' <= c <= '\u9fff' for c in classical), \
                f"'{eng}' -> '{classical}' 不包含中文"
