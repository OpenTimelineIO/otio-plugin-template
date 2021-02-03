"""
Simple linker just adding a MissingReference and giving it a tweaked name
"""

import opentimelineio as otio


def link_media_reference(in_clip, media_linker_argument_map):
    meta = dict()
    meta.update(media_linker_argument_map)

    # you'll probably want to set it to something other than a missing reference
    in_clip.media_reference = otio.schema.MissingReference(
        name=in_clip.name + "_tweaked",
        metadata=meta
    )
