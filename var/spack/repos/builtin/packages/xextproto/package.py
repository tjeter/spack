# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import json
import os
from spack.package import *


class Xextproto(AutotoolsPackage, XorgPackage):
    """X Protocol Extensions."""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "cpe.json") as f:
        data = json.load(f)
    cpe = data
    homepage = "https://cgit.freedesktop.org/xorg/proto/xextproto"
    xorg_mirror_path = "proto/xextproto-7.3.0.tar.gz"

    version('7.3.0', sha256='1b1bcdf91221e78c6c33738667a57bd9aaa63d5953174ad8ed9929296741c9f5')

    

    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')

    parallel = False
