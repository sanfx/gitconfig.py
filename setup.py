#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Setup file for gitconfig package """

from distutils.core import setup
import os


def is_package(path):
    return (
        os.path.isdir(path) and
        os.path.isfile(os.path.join(path, '__init__.py'))
    )


def find_packages(path, base=""):
    """ Find all packages in path """
    packages = {}
    for item in os.listdir(path):
        dir = os.path.join(path, item)
        if is_package(dir):
            if base:
                module_name = "%(base)s.%(item)s" % vars()
            else:
                module_name = item
            packages[module_name] = dir
            packages.update(find_packages(dir, module_name))
    return packages

setup(name='gitconfig',
      version='0.0.1',
      description='gitconfig',
      long_description=open("README.rst").read(),
      author='cancerhermit',
      author_email='cancerhermit@gmail.com',
      url='http://github.com/cancerhermit/PyGitConfig/',
      packages = find_packages(".").keys(),
      install_requires=[
        "GitPython"
      ],
      platforms = ["ALL"],
      keywords="git config",
      classifiers=(
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Environment :: Console',

          'Natural Language :: English',

          'Programming Language :: Python',

          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities'
        ),
      license="GPL"
     )