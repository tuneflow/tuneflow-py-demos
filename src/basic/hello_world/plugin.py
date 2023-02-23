from tuneflow_py import TuneflowPlugin, Song, ReadAPIs, ParamDescriptor
from typing import Any


class HelloWorld(TuneflowPlugin):
    @staticmethod
    def provider_id():
        return "andantei"

    @staticmethod
    def plugin_id():
        return "hello-world"

    @staticmethod
    def provider_display_name():
        return {
            "zh": "Andantei 行板",
            "en": "Andantei"
        }

    @staticmethod
    def plugin_display_name():
        return {
            "zh": "Hello World 插件",
            "en": "Hello World Plugin"
        }

    @staticmethod
    def plugin_description():
        return {
            "zh": "这是一个Hello World插件",
            "en": "This is a hello world plugin."
        }

    @staticmethod
    def allow_reset():
        return False
    
    def params(self) -> dict[str, ParamDescriptor]:
        return {}

    def run(self, song: Song, params: dict[str, Any], read_apis: ReadAPIs):
        """
        Do nothing except printing "hello world".

        You should be able to load all metadata of this plugin and
        the song should remain unchanged after running this plugin.
        """
        print("Hello World!")
