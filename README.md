# OpenTimelineIO Plugin Template

This repository serves as a template for writing new adapters, media linkers, 
hooks or schemadefs that plug into OpenTimelineIO.
It contains some boiler plate files and folders to help you write plugins that 
should install correctly. 

Once cloned, you're encouraged to add, rename or remove files and folders as you 
see fit, but please try and keep to the suggested naming convention below. 
That way it's easy to spot an OTIO plugin and understand what it does.


## Suggested naming convention

We recommend naming your cloned repository and package name after the 
following conventions:

* Repository and uploaded package name (using hyphens):
`otio-<dialect>[-<plugintype>]`
* Python package name (using underscores): `otio_<dialect>_<plugintype>`


| Key          | Required | Notes                                                             |
|:-------------|:--------:|:------------------------------------------------------------------|
| `dialect`    | True     | The filetype, language, application etc. you're adding support for|
| `plugintype` | False    | `adapter`, `medialinker`, `hook`, `scemadef` etc.<br>If your plugin contains several of the mentioned components you may omit the<br>plugintype given that the dialect key covers the intention of the plugin.

Examples:
* `otio-playlist-adapter` (read or write playlist files)
* `otio-git-hook` (a hook that commits otio file to git after writing)
* `otio-ffmpeg-medialinker` (link media references using FFmpeg)
* `otio-videofx-shemadef` (adds a video effects schema)
* `otio-mxf` (complex plugin to read, write and link MXF files)


## Suggested folder structure

```bash
├── LICENSE
├── otio_plugin_template
│   ├── adapters
│   │   └── my_adapter.py
│   ├── hooks
│   │   └── my_hook.py
│   ├── operations
│   │   └── my_media_linker.py
│   └── schemadefs
│       └── my_schemadef.py
├── plugin_manifest.json
├── README.md
├── setup.py
└── tests
    └── test_my_plugin.py
```

## Tests

It's always a good idea to write unit tests for you code.
Please provide tests that run against supported versions of python and 
OpenTimelineIO.


## Upload to PyPi

An example setup.py is provided which should guide you on the way towards
publishing your plugin on PyPi.
There's also a sample github-action provided to help automate the process.


## Github Actions

A set of simple automation scripts are available in the `.github/workflows` folder.
* `ci.yaml` - runs unit tests
* `build_package.yaml` - simple packing an publishing of a plugin package
* `create_draft_release` - when a tag is pushed, it creates a draft for a release
