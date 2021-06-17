# Copyright Contributors to the OpenTimelineIO project
#
# SPDX-License-Identifier: MIT OR Apache-2.0
#

import io
import setuptools

with io.open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


"""
Make sure to replace all the dummy names, emails etc. with your details and
package names.
"""

setuptools.setup(
    name="your-plugin-name",
    author="YOUR NAME",
    author_email="your.email@domain.com",
    version="0.0.1",
    description="Short description of your plugin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Replace url with your repo
    url="https://github.com/USERNAME/your-repo-name",
    packages=setuptools.find_packages(),
    entry_points={
        # Replace otio_plugin_template with your package name
        "opentimelineio.plugins": "otio_plugin_template = otio_plugin_template"
    },
    package_data={
        # Replace otio_plugin_template with your package name
        "otio_plugin_template": [
            "plugin_manifest.json",
        ],
    },
    install_requires=[
        "OpenTimelineIO >= 0.12.0"
    ],
    extras_require={
        "dev": [
            "flake8",
            "pytest",
            "pytest-cov",
            "twine"
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Video",
        "Topic :: Multimedia :: Video :: Display",
        "Topic :: Multimedia :: Video :: Non-Linear Editor",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English"
    ]
)
