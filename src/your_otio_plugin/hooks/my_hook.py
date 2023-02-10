"""
Simple hook function that injects a key in an item's metadata
"""


def hook_function(in_timeline, argument_map=None):
    for item in in_timeline.tracks[0]:
        item.metadata['my_hook_function_was_here'] = True

    return in_timeline
