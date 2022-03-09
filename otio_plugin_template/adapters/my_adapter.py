"""
Super simple adapter example that takes a json formatted string and creates
a Timeline.

Ex:
raw_data = '''{
    "timeline": {
        "name": "my_timeline"
    },
    "track": {
        "name": "v1"
    },
    "clip": {
        "name": "my_clip",
        "in": 0,
        "out": 100,
        "rate": 30
    }
}'''
"""

import json
import opentimelineio as otio


def read_from_string(input_str):
    data = json.loads(input_str)

    timeline_name = data['timeline']['name']
    track_name = data['track']['name']
    clip_data = data['clip']

    timeline = otio.schema.Timeline(timeline_name)
    track = otio.schema.Track(track_name)
    clip = otio.schema.Clip(
        clip_data['name'],
        source_range=otio.opentime.TimeRange(
            otio.opentime.RationalTime(clip_data['in'], clip_data['rate']),
            otio.opentime.RationalTime(clip_data['out'], clip_data['rate'])
        )
    )

    timeline.tracks.append(track)
    track.append(clip)

    return timeline
