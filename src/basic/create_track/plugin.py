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
    def params(song: Song, read_apis: ReadAPIs) -> dict[str, ParamDescriptor]:
        return {}

    @staticmethod
    def run(song: Song, params: dict[str, Any], read_apis: ReadAPIs):
        print("=============================")
        print("In this example you will see a new, empty midi track being added to the song.")
        song.create_track(TrackType.MIDI_TRACK, index=0)
