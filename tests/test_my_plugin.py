import opentimelineio as otio


def test_adapter():
    raw = """{
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
    }"""
    timeline = otio.adapters.read_from_string(raw, 'my_adapter')
    assert isinstance(timeline, otio.schema.Timeline)


def test_hook():
    timeline = otio.schema.Timeline()
    track = otio.schema.Track('v1')
    clip = otio.schema.Clip(
        'my_clip',
        source_range=otio.opentime.TimeRange(
            otio.opentime.RationalTime(0, 30),
            otio.opentime.RationalTime(100, 30)
        )
    )
    track.append(clip)
    timeline.tracks.append(track)

    assert clip.metadata.get(
        'my_hook_function_was_here',
        None
    ) is None

    raw_timeline_str = otio.adapters.write_to_string(timeline)
    o = otio.adapters.read_from_string(raw_timeline_str)

    assert isinstance(o, otio.schema.Timeline)

    clip_changed = o.tracks[0][0]
    assert clip_changed.metadata.get(
        'my_hook_function_was_here',
        None
    ) is True


def test_media_linker():
    clip = otio.schema.Clip(
        'my_clip',
        source_range=otio.opentime.TimeRange(
            otio.opentime.RationalTime(0, 30),
            otio.opentime.RationalTime(100, 30)
        )
    )
    clip.media_reference = otio.schema.ExternalReference(
        target_url='/client/source/to/my_clip.ext',
        available_range=otio.opentime.TimeRange(
            otio.opentime.RationalTime(0, 30),
            otio.opentime.RationalTime(100, 30)
        )
    )
    linker_args = {
        "old_root": "/client/source/",
        "new_root": "/local/storage/"
    }
    linker = otio.media_linker.from_name('my_media_linker')
    linker.link_media_reference(clip, linker_args)

    assert clip.media_reference.target_url == '/local/storage/to/my_clip.ext'


def test_schemadef():
    my_schema = otio.schemadef.my_schemadef.MyThing()
    assert isinstance(my_schema, otio.core.SerializableObject)
    assert my_schema.arg1 is None
    assert my_schema.argN is None
