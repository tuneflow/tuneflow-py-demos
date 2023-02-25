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
    def params(song: Song, read_apis: ReadAPIs) -> dict[str, ParamDescriptor]:
        return {}

    @staticmethod
    def run(song: Song, params: dict[str, Any], read_apis: ReadAPIs):
        """
        Do nothing except printing "hello world".

        You should be able to load all metadata of this plugin and
        the song should remain unchanged after running this plugin.
        """
        print("Hello World!")
