"""
Simple linker script replacing the root of the storage path
"""

import re
import opentimelineio as otio


def link_media_reference(in_clip, media_linker_argument_map):
    old_root = media_linker_argument_map.get('old_root', '')
    new_root = media_linker_argument_map.get('new_root', '')

    # Store media reference as a variable for convenience
    mr = in_clip.media_reference

    # Check for media reference
    if not mr:
        # Since there's no media reference we move on
        return

    if isinstance(mr, otio.schema.ExternalReference):
        mr.target_url = re.sub(old_root, new_root, mr.target_url, count=1)

    elif isinstance(mr, otio.schema.ImageSequenceReference):
        mr.target_url_base = re.sub(
            old_root,
            new_root,
            mr.target_url_base,
            count=1
        )
