#!/usr/bin/env python

from setuptools import setup

setup(name='byte_fifo',
      packages=["byte_fifo"],
      use_scm_version = {
            "write_to": "byte_fifo/_version.py",
          },
      setup_requires=["setuptools_scm"],
     )

