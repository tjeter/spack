# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import json
import os
from spack.package import *


class LibpthreadStubs(AutotoolsPackage):
    """The libpthread-stubs package provides weak aliases for pthread
    functions not provided in libc or otherwise available by default."""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/cpe.json") as f:
        data = json.load(f)
    cpe = data
    homepage = "https://xcb.freedesktop.org/"
    url      = "https://xcb.freedesktop.org/dist/libpthread-stubs-0.4.tar.gz"

    version('0.4', sha256='50d5686b79019ccea08bcbd7b02fe5a40634abcfd4146b6e75c6420cc170e9d9')
    version('0.3', sha256='3031f466cf0b06de6b3ccbf2019d15c4fcf75229b7d226a711bc1885b3a82cde')

    

