"""
Simple linker pretending to add an ExternalReference
"""

import opentimelineio as otio


def link_media_reference(in_clip, media_linker_argument_map):
    meta = dict()
    meta.update(media_linker_argument_map)

    # You'll probably want to set it to something other than this
    in_clip.media_reference = otio.schema.ExternalReference(
        target_url='/some/path/to/my_clip.ext',
        metadata=meta,
        available_range=otio.opentime.TimeRange(
            otio.opentime.RationalTime(0, 30),
            otio.opentime.RationalTime(100, 30)
        )
    )
