# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Firestarter(CMakePackage):
    """FIRESTARTER maximizes the energy consumption of
    64-Bit x86 processors by generating heavy load on the
    execution units as well as transferring data between
    the cores and multiple levels of the memory hierarchy."""

    tags = ["benchmark"]
    homepage = "https://github.com/tjeter/FIRESTARTER/tree/caliper"
    git = "https://github.com/tjeter/FIRESTARTER.git"

    license("Apache-2.0")

    version("master", branch="caliper")

    variant("caliper", default=False, description="Enable Caliper monitoring")

    depends_on("caliper", when="+caliper")
    depends_on("adiak", when="+caliper")

    def cmake_args(self):
        cmake_options = []
        cmake_options.append(self.define_from_variant("FIRESTARTER_WITH_CALIPER", "caliper"))

        return cmake_options
