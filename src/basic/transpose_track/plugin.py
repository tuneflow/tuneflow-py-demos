from tuneflow_py import TuneflowPlugin, Song, ParamDescriptor, WidgetType, TrackType, ClipType, Note
from typing import Any


class TransposeTrack(TuneflowPlugin):
    @staticmethod
    def provider_id():
        return "andantei"

    @staticmethod
    def plugin_id():
        return "transpose-track"

    @staticmethod
    def params(song: Song) -> dict[str, ParamDescriptor]:
        return {
            "trackId": {
                "displayName": {
                    "zh": '轨道',
                    "en": 'Track',
                },
                "defaultValue": None,
                "widget": {
                    "type": WidgetType.TrackSelector.value,
                    "config": {
                        "alwaysShowTrackInfo": True,
                        "allowedTrackTypes": [TrackType.MIDI_TRACK],  # type: ignore
                    },
                },
            },
            "pitchOffset": {
                "displayName": {
                    "zh": '调整半音数',
                    "en": 'Shift Pitches By',
                },
                "defaultValue": 12,
                "widget": {
                    "type": WidgetType.Select.value,
                    "config": {
                        "options": [
                            {
                                "label": {
                                    "zh": '+12 (升八度)',
                                    "en": '+12 (One Octave Up)',
                                },
                                "value": 12,
                            },
                            {
                                "label": {
                                    "zh": '-12 (降八度)',
                                    "en": '-12 (One Octave Down)',
                                },
                                "value": -12,
                            },
                            {
                                "label": {
                                    "zh": '+1 (升半音)',
                                    "en": '+1 (One Semiton Up)',
                                },
                                "value": 1,
                            },
                            {
                                "label": {
                                    "zh": '-1 (降半音)',
                                    "en": '-1 (One Semitone Down)',
                                },
                                "value": -1,
                            },
                        ],
                    },
                },
                "adjustableWhenPluginIsApplied": True
            },
        }

    @staticmethod
    def run(song: Song, params: dict[str, Any]):
        track_id = params["trackId"]
        pitch_offset = params["pitchOffset"]
        track = song.get_track_by_id(track_id=track_id)
        if track is None:
            raise Exception('Track not ready')

        for clip in track.get_clips():
            if clip.get_type() == ClipType.MIDI_CLIP:  # type: ignore
                raw_notes = list(clip.get_raw_notes())
                for i in reversed(range(len(raw_notes))):
                    note = raw_notes[i]
                    new_pitch = note.get_pitch() + pitch_offset
                    if not Note.is_valid_pitch(new_pitch):
                        clip.delete_note_at(i)
                        continue
                    note.set_pitch(new_pitch)
            elif clip.get_type() == ClipType.AUDIO_CLIP:  # type: ignore
                # TODO: Support audio pitch shift.
                pass
