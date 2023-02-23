from tuneflow_py import TuneflowPlugin, Song, ReadAPIs, ParamDescriptor
from typing import Any


class ReadAPIExample(TuneflowPlugin):
    @staticmethod
    def provider_id():
        return "andantei"

    @staticmethod
    def plugin_id():
        return "read-api-example"

    @staticmethod
    def provider_display_name():
        return {
            "zh": "Andantei 行板",
            "en": "Andantei"
        }

    @staticmethod
    def plugin_display_name():
        return {
            "zh": "ReadAPIs示例",
            "en": "ReadAPIs Example",
        }

    @staticmethod
    def plugin_description():
        return {
            "zh": "演示如何使用ReadAPIs",
            "en": "An example of how to use ReadAPIs",
        }

    @staticmethod
    def allow_reset():
        return False

    def params(self) -> dict[str, ParamDescriptor]:
        return {}

    def init(self, song: Song, read_apis: ReadAPIs):
        print(read_apis.translate_label({
            "zh": "插件初始化中",
            "en": "Plugin initializing"
        }))

    def run(self, song: Song, params: dict[str, Any], read_apis: ReadAPIs):
        print("=============================")
        print("Available audio plugins: ")
        print(read_apis.get_available_audio_plugins())
