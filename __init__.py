"""
promote2classical - 英文单词转文言文库，节约Token

用法:
    from promote2classical import translate

    result = translate("promote")
    print(result)  # 升
"""

__version__ = "0.1.0"
__all__ = ["translate", "Translator", "get_merged_dict"]

from .core import Translator, translate
from .dict import get_merged_dict
