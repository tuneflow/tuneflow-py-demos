from tuneflow_py import TuneflowPlugin, Song, ReadAPIs, ParamDescriptor, TrackType
from typing import Any


class CreateTrackExample(TuneflowPlugin):
    @staticmethod
    def provider_id():
        return "andantei"

    @staticmethod
    def plugin_id():
        return "create-track-example"

    @staticmethod
    def provider_display_name():
        return {
            "zh": "Andantei 行板",
            "en": "Andantei"
        }

    @staticmethod
    def plugin_display_name():
        return {
            "zh": "创建轨道示例",
            "en": "Create Track Example",
        }

    @staticmethod
    def plugin_description():
        return {
            "zh": "演示如何创建新轨道",
            "en": "An example of how to create new tracks",
        }

    @staticmethod
    def allow_reset():
        return False

    def params(self) -> dict[str, ParamDescriptor]:
        return {}

    def run(self, song: Song, params: dict[str, Any], read_apis: ReadAPIs):
        print("=============================")
        print("In this example you will see a new, empty midi track being added to the song.")
        song.create_track(TrackType.MIDI_TRACK, index=0)
