# OpenTimelineIO Plugin Template

Welcome to OpenTimelineIO's plugin template repository!  
This repository serves as a template for writing new adapters, media linkers, 
hooks or schemadefs that expand OpenTimelineIO through its plugin system.
It contains boilerplate files and folders to help you write plugins that 
register properly when installing through pip should you choose to do so.  

## Licensing

This template repository is licensed under a choice of the 
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)
or the [MIT License](https://opensource.org/licenses/MIT). If you are cloning 
this repository, you are welcome to have your code under either of these licenses, 
or a license that is compatible.


# Getting started

To get started, just push the green **"Use this template"** button at the top right 
of the repository listing. A dialog will appear where you enter the name and
location of your new repository.  
Please consider following the suggested 
[naming convention](#Suggested-naming-convention) below.  
Sticking to a naming convention makes it easy for others to spot an 
OTIO plugin and understand what it does when browsing PyPi or GitHub
should you choose to share your plugin.

Once your new plugin repository is created you should be all set to begin 
writing your plugin.  
Please take a look at the notes in the 
[default folder structure](#Default-folder-structure) section for a few tips.

Please also consult with the OpenTimelineIO [documentation](https://opentimelineio.readthedocs.io/en/latest/index.html)
for more information about OpenTimelineIO in general and  
[here](https://opentimelineio.readthedocs.io/en/latest/tutorials/write-an-adapter.html) for documentation about **adapters**  
[here](https://opentimelineio.readthedocs.io/en/latest/tutorials/write-a-media-linker.html) for documentation about **media linkers**  
[here](https://opentimelineio.readthedocs.io/en/latest/tutorials/write-a-hookscript.html) for documentation about **hooks**  
[here](https://opentimelineio.readthedocs.io/en/latest/tutorials/write-a-schemadef.html) for documentation about **shemadefs**  

Good luck and happy coding!


## Suggested naming convention

We recommend naming your cloned repository and package name after the 
following convention:

* Repository and uploaded package name (using hyphens):
`otio-<dialect>[-<plugintype>]`
* Python package name (using underscores): `otio_<dialect>_<plugintype>`


| Key          | Required | Notes                                                                                                                                                                                                          |
|:-------------|:--------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `dialect`    |   True   | The filetype, language, application etc. you're adding support for                                                                                                                                             |
| `plugintype` |  False   | `adapter`, `medialinker`, `hook`, `scemadef` etc.<br>If your plugin contains several of the mentioned components you may omit the<br>plugintype given that the dialect key covers the intention of the plugin. |

Examples:
* `otio-playlist-adapter` (read or write playlist files)
* `otio-git-hook` (a hook that commits otio file to git after writing)
* `otio-ffmpeg-medialinker` (link media references using FFmpeg)
* `otio-videofx-shemadef` (adds some video effects schema)
* `otio-mxf` (complex plugin to read, write and link MXF files)


## Default folder structure
Below is the default file and folder tree that comes with the plugin template.
  
```
 |── LICENSE
 ├── otio_plugin_template
 │   ├── __init__.py
 │   ├── plugin_manifest.json  # Required
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

### Reorganizing the folder structure to suite your plugin
You're free to rename, remove or restructure the files and folders to best suite 
your plugin. Simple adapters may not need a deep folder structure (see example below).  
Just make sure the `plugin_manifest.json` file is kept and that the contents 
inside it reflect your choices. This makes sure OpenTimelineIO's plugin system 
loads your plugin properly.

> **TIP!** Make sure to add a descriptive docstring at the top of your plugin files, so they 
register properly and inform users of what they do.

Example of a simple adapter plugin. Notice how we removed the "adapters" folder.
```
 |── LICENSE
 ├── otio_my_adapter
 │   ├── __init__.py
 │   ├── plugin_manifest.json  # Required
 │   ├── my_adapter.py
 ├── README.md
 ├── setup.cfg
 ├── setup.py
 ├── tests
     └── test_my_adapter.py
```

And the manifest file:
``` json
{
    "OTIO_SCHEMA" : "PluginManifest.1",
    "adapters" : [
        {
            "OTIO_SCHEMA" : "Adapter.1",
            "name" : "my_adapter",
            "execution_scope" : "in process",
            "filepath" : "my_adapter.py",
            "suffixes" : ["xyz"]
        }
    ]
}
```

## Testing your plugin during development
```
# In the root folder of the repo
pip install -e .

# Check if plugin installed correctly
otiopluginfo myadapter

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
```
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
