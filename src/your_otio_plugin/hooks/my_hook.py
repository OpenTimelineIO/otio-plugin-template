"""
Simple hook function that injects a key in a clips metadata
"""


def hook_function(in_timeline, argument_map=None):
    for clip in in_timeline.each_clip():
        clip.metadata['my_hook_function_was_here'] = True

    return in_timeline
