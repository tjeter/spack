# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack.package import *


class Maven(Package):
    """Apache Maven is a software project management and comprehension tool."""

    homepage = "https://maven.apache.org/index.html"
    url = "https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/3.3.9/apache-maven-3.3.9-bin.tar.gz"

    version('3.8.5', sha512='89ab8ece99292476447ef6a6800d9842bbb60787b9b8a45c103aa61d2f205a971d8c3ddfb8b03e514455b4173602bd015e82958c0b3ddc1728a57126f773c743')
    version('3.8.4', sha256='2cdc9c519427bb20fdc25bef5a9063b790e4abd930e7b14b4e9f4863d6f9f13c')
    version('3.6.3', sha256='26ad91d751b3a9a53087aefa743f4e16a17741d3915b219cf74112bf87a438c5')
    version('3.6.2', sha256='3fbc92d1961482d6fbd57fbf3dd6d27a4de70778528ee3fb44aa7d27eb32dfdc')
    version('3.6.1', sha256='2528c35a99c30f8940cc599ba15d34359d58bec57af58c1075519b8cd33b69e7')
    version('3.6.0', sha256='6a1b346af36a1f1a491c1c1a141667c5de69b42e6611d3687df26868bc0f4637')
    version('3.5.0', sha256='beb91419245395bd69a4a6edad5ca3ec1a8b64e41457672dc687c173a495f034')
    version('3.3.9', sha256='6e3e9c949ab4695a204f74038717aa7b2689b1be94875899ac1b3fe42800ff82')
    version('3.0.4', sha256='d35a876034c08cb7e20ea2fbcf168bcad4dff5801abad82d48055517513faa2f')

    cpe = {
            '3.0.4':'cpe:2.3:a:apache:maven:3.0.4:*:*:*:*:*:*:*',
            '3.0.4':'cpe:2.3:a:jenkins:pipeline_maven_integration:3.0.4:*:*:*:*:jenkins:*:*',
            '3.5.0':'cpe:2.3:a:jenkins:pipeline_maven_integration:3.5.0:-:*:*:*:jenkins:*:*',
            '3.5.0':'cpe:2.3:a:jenkins:pipeline_maven_integration:3.5.0:beta1:*:*:*:jenkins:*:*',
            '3.6.0':'cpe:2.3:a:jenkins:pipeline_maven_integration:3.6.0:-:*:*:*:jenkins:*:*',
            '3.6.0':'cpe:2.3:a:jenkins:pipeline_maven_integration:3.6.0:beta1:*:*:*:jenkins:*:*',
            '3.6.0':'cpe:2.3:a:jenkins:pipeline_maven_integration:3.6.0:beta2:*:*:*:jenkins:*:*',
            '3.6.1':'cpe:2.3:a:jenkins:pipeline_maven_integration:3.6.1:*:*:*:*:jenkins:*:*',
            '3.6.2':'cpe:2.3:a:jenkins:pipeline_maven_integration:3.6.2:*:*:*:*:jenkins:*:*',
            '3.6.3':'cpe:2.3:a:jenkins:pipeline_maven_integration:3.6.3:*:*:*:*:jenkins:*:*',
            '3.6.3':'cpe:2.3:a:apache:maven:3.6.3:*:*:*:*:*:*:*',
            '3.6.2':'cpe:2.3:a:apache:maven:3.6.2:*:*:*:*:*:*:*',
            '3.6.1':'cpe:2.3:a:apache:maven:3.6.1:*:*:*:*:*:*:*',
            '3.6.0':'cpe:2.3:a:apache:maven:3.6.0:*:*:*:*:*:*:*',
            '3.3.9':'cpe:2.3:a:apache:maven:3.3.9:*:*:*:*:*:*:*',
            '3.5.0':'cpe:2.3:a:apache:maven:3.5.0:-:*:*:*:*:*:*',
            '3.5.0':'cpe:2.3:a:apache:maven:3.5.0:alpha1:*:*:*:*:*:*',
            '3.5.0':'cpe:2.3:a:apache:maven:3.5.0:beta1:*:*:*:*:*:*',
            '3.8.5':'cpe:2.3:a:apache:maven:3.8.5:*:*:*:*:*:*',
            '3.3.9':'cpe:2.3:a:apache:maven:3.3.9:*:*:*:*:*:*',
            '3.8.4':'cpe:2.3:a:apache:maven:3.8.4:*:*:*:*:*:*'
          }

    depends_on('java', type='run')

    executables = ['^mvn$']

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)('--version', output=str, error=str)
        match = re.search(r'Apache Maven (\S+)', output)
        return match.group(1) if match else None

    def install(self, spec, prefix):
        # install pre-built distribution
        install_tree('.', prefix)
