from tuneflow_py import TuneflowPlugin, Song, ReadAPIs, ParamDescriptor
from typing import Any


class ThrowExceptionExample(TuneflowPlugin):
    @staticmethod
    def provider_id():
        return "andantei"

    @staticmethod
    def plugin_id():
        return "throw-exception-example"

    @staticmethod
    def provider_display_name():
        return {
            "zh": "Andantei 行板",
            "en": "Andantei"
        }

    @staticmethod
    def plugin_display_name():
        return {
            "zh": "抛出异常示例",
            "en": "Throw Exception Example",
        }

    @staticmethod
    def plugin_description():
        return {
            "zh": "一个在插件执行过程中抛出异常的示例，在TuneFlow桌面版中执行本插件后插件状态条将变成红色以表示执行出错。",
            "en": "Throw an exception during execution. You should be able to see that the plugin in TuneFlow Desktop turns red after execution.",
        }

    @staticmethod
    def allow_reset():
        return False

    def params(self) -> dict[str, ParamDescriptor]:
        return {}

    def run(self, song: Song, params: dict[str, Any], read_apis: ReadAPIs):
        """
        Throw an exception during execution. You should be able to see that
        the plugin in TuneFlow Desktop turns red after execution.
        """
        a = 1/0
