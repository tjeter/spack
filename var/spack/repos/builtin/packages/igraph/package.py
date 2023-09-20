# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import json
import os
from spack.package import *


class Igraph(AutotoolsPackage):
    """igraph is a library for creating and manipulating graphs."""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/cpe.json") as f:
        data = json.load(f)
    cpe = data
    homepage = "https://igraph.org/"
    url      = "https://github.com/igraph/igraph/releases/download/0.7.1/igraph-0.7.1.tar.gz"

    version('0.7.1', sha256='d978030e27369bf698f3816ab70aa9141e9baf81c56cc4f55efbe5489b46b0df')

    

    depends_on('libxml2')
