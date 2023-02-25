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
    def params(song: Song, read_apis: ReadAPIs) -> dict[str, ParamDescriptor]:
        return {}

    @staticmethod
    def run(song: Song, params: dict[str, Any], read_apis: ReadAPIs):
        """
        Throw an exception during execution. You should be able to see that
        the plugin in TuneFlow Desktop turns red after execution.
        """
        a = 1/0
