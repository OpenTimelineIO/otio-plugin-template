# OpenTimelineIO Plugin Template

This repository serves as a template for writing new adapters, media linkers, 
hooks or schemadefs that expand OpenTimelineIO through its plugin system.
It contains some boiler plate files and folders to help you write plugins that 
should install correctly through pip should you choose to do so.

Once cloned, you're free to add, rename or remove files and folders as you 
see fit, but we encourage you to follow the suggested 
[naming convention](#Suggested-naming-convention) below. 
That way it's easy for others to spot an OTIO plugin and understand what it does.


## Licensing

This template repository is licensed under a choice of the 
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)
or the [MIT License](https://opensource.org/licenses/MIT). If you are cloning 
this repository, you are welcome to have your code under either of these licenses, 
or a license that is compatible.


## Suggested naming convention

We recommend naming your cloned repository and package name after the 
following convention:

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
* `otio-videofx-shemadef` (adds some video effects schema)
* `otio-mxf` (complex plugin to read, write and link MXF files)


## Suggested folder structure

```bash
├── LICENSE
├── otio_plugin_template
│   ├── __init__.py
│   ├── plugin_manifest.json
│   ├── adapters
│   │   ├── __init__.py
│   │   ├── my_adapter.py
│   ├── hooks
│   │   ├── __init__.py
│   │   ├── my_hook.py
│   ├── operations
│   │   ├── __init__.py
│   │   ├── my_media_linker.py
│   └── schemadefs
│       ├── __init__.py
│       ├── my_schemadef.py
├── README.md
├── setup.cfg
├── setup.py
├── tests
    └── test_my_plugin.py
```
You're free to rename or restructure files and folders above, but make sure the 
`plugin_manifest.json` filename is kept and that the contents inside it reflect
your choices so OpenTimelineIO's plugin system loads your plugin properly.


## Testing your plugin during development
```bash
# In the root folder of the repo
pip install -e .

# Test an adapter for instance
otioconvert -i some_timeline.otio -o some_timeline.ext
```


## Unit tests

It's always a good idea to write unit tests for you code.
Please provide tests that run against supported versions of python and 
OpenTimelineIO.


## Github Actions

A set of simple automation scripts are available in the `.github/workflows` folder.
* `ci.yaml` - runs unit tests
* `create_draft_release` - when a tag is pushed, it creates a draft for a release
* `deploy_package.yaml` - simple packing an publishing of a plugin package. 
  Make sure you have a valid token for your PyPi user added to your repos 
  [secrets](https://docs.github.com/es/actions/reference/encrypted-secrets).


## Upload to PyPi

Should you want to release your package to the world and let others reap the 
fruits of your labor, an example setup.py is provided which should guide you 
on the way towards publishing your plugin on PyPi.
There's also a sample github-action provided to help automate the process.

Manual steps for creating a simple package and upload to (test)PyPi:
```bash
python setup.py sdist bdist_wheel --universal
twine upload --repository testpypi dist/*
```
Please check out pythons [docs](https://packaging.python.org/tutorials/packaging-projects/#packaging-python-projects) 
for more detailed descriptions on packaging. 


## Let us know about your plugin
If you release your plugin to the public please let us know about it, so we can 
add it to our [list](https://github.com/PixarAnimationStudios/OpenTimelineIO/wiki/Tools-and-Projects-Using-OpenTimelineIO) 
of known plugins.


## Contributions

If you have any suggested changes to the template repository itself, 
please provide them via [pull request](../../pulls) or [create an issue](../../issues) as appropriate. 

All contributions back to the template repository must align with the contribution
[guidelines](https://opentimelineio.readthedocs.io/en/latest/tutorials/contributing.html) 
of the OpenTimelineIO project.
