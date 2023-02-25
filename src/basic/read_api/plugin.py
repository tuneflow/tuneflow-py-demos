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
    def params(song: Song, read_apis: ReadAPIs) -> dict[str, ParamDescriptor]:
        return {}

    @staticmethod
    def run(song: Song, params: dict[str, Any], read_apis: ReadAPIs):
        print("=============================")
        print("Available audio plugins: ")
        print(read_apis.get_available_audio_plugins())
