"""
核心翻译模块：词典方案
"""

from .dict import get_merged_dict


class Translator:
    """英文转文言文翻译器"""

    def __init__(self):
        """
        初始化翻译器
        """
        pass

    def translate(self, word: str) -> str:
        """
        将英文单词翻译为文言文

        Args:
            word: 英文单词

        Returns:
            文言文翻译
        """
        word = word.strip().lower()

        # 词典查找（YAML > builtin）
        merged = get_merged_dict()
        if word in merged:
            return merged[word]

        # 词典无结果时返回原词
        return word

    def batch_translate(self, words: list[str]) -> list[str]:
        """批量翻译"""
        return [self.translate(w) for w in words]


# 全局默认实例
_default_translator: Translator | None = None


def translate(word: str) -> str:
    """
    将英文单词翻译为文言文（全局函数）

    用法:
        from promote2classical import translate
        result = translate("promote")  # "升"
    """
    global _default_translator
    if _default_translator is None:
        _default_translator = Translator()
    return _default_translator.translate(word)
