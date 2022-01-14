# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPoetryCore(PythonPackage):
    """Poetry PEP 517 Build Backend."""

    homepage = "https://github.com/python-poetry/poetry-core"
    pypi     = "poetry-core/poetry-core-1.0.7.tar.gz"

    version('1.0.7', sha256='98c11c755a16ef6c5673c22ca94a3802a7df4746a0853a70b6fae8b9f5cac206')

    depends_on('python@2.7,3.5:3', type=('build', 'run'))
    depends_on('py-importlib-metadata@1.7:1', when='^python@2.7,3.5:3.7', type=('build', 'run'))
    depends_on('py-pathlib2@2.3.5:2', when='^python@2.7', type=('build', 'run'))
    depends_on('py-typing@3.7.4.1:3', when='^python@2.7', type=('build', 'run'))
    depends_on('py-enum34@1.1.10:1', when='^python@2.7', type=('build', 'run'))
    depends_on('py-functools32@3.2.3-2:3', when='^python@2.7', type=('build', 'run'))
