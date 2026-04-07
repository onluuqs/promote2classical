"""
核心翻译模块：混合方案（词典优先 + AI翻译）
"""

import os
import anthropic
from typing import Optional

from .dict.builtin import EN2CLASSICAL_BUILTIN

# 默认使用 Opus 4.6
DEFAULT_MODEL = "claude-opus-4-6"


class Translator:
    """英文转文言文翻译器"""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = DEFAULT_MODEL,
        cache: bool = True,
    ):
        """
        初始化翻译器

        Args:
            api_key: Anthropic API密钥，默认从环境变量ANTHROPIC_API_KEY读取
            model: 使用的模型，默认claude-opus-4-6
            cache: 是否缓存AI翻译结果，默认True
        """
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.model = model
        self.cache = cache
        self._cache: dict[str, str] = {}

        if self.api_key:
            self.client = anthropic.Anthropic(api_key=self.api_key)
        else:
            self.client = None

    def translate(self, word: str) -> str:
        """
        将英文单词翻译为文言文

        Args:
            word: 英文单词

        Returns:
            文言文翻译
        """
        word = word.strip().lower()

        # 1. 词典优先
        if word in EN2CLASSICAL_BUILTIN:
            return EN2CLASSICAL_BUILTIN[word]

        # 2. 缓存命中
        if self.cache and word in self._cache:
            return self._cache[word]

        # 3. AI翻译
        if self.client:
            result = self._ai_translate(word)
            if self.cache:
                self._cache[word] = result
            return result

        # 4. 无API密钥且词典无结果
        return word

    def _ai_translate(self, word: str) -> str:
        """调用Claude AI进行翻译"""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=50,
            messages=[{
                "role": "user",
                "content": f"将以下英文单词翻译为单个汉字的文言文（古汉语），只需返回汉字，不要解释：{word}"
            }]
        )

        result = "".join(
            block.text for block in response.content
            if hasattr(block, "text") and block.text
        ).strip()

        return result if result else word

    def batch_translate(self, words: list[str]) -> list[str]:
        """批量翻译"""
        return [self.translate(w) for w in words]


# 全局默认实例
_default_translator: Optional[Translator] = None


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
