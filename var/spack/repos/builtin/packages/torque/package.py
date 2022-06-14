# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Torque(Package):
    """TORQUE (Terascale Open-source Resource and QUEue Manager) is an open
    source project based on the original PBS resource manager developed by NASA,
    LLNL, and MRJ."""

    homepage = "https://github.com/abarbu/torque"
    has_code = False

    maintainers = ['sethrj']

    version('6.0.0')
    version('5.1.2')
    version('5.1.1.2')
    version('5.1.1')
    version('5.0.2')
    version('5.0.1.h2')
    version('5.0.1')
    version('5.0.0')
    version('4.5.0')
    version('4.2.9')
    version('4.2.8')
    version('4.2.7')
    version('4.2.6.1.h1')
    version('4.2.6.1')
    version('4.2.6')
    version('4.2.5')
    version('4.2.4')
    version('4.2.3')
    version('4.2.2')
    version('4.2.1')
    version('4.2.0')
    version('4.1.6')
    version('4.1.5')
    version('4.1.4')
    version('4.1.3')
    version('4.1.2')
    version('4.1.1')
    version('4.1.0')
    version('4.0.3')
    version('4.0.2')
    version('4.0.1')
    version('4.0.0')
    version('3.0.5')
    version('3.0.4')
    version('3.0.3')
    version('3.0.2')
    provides('pbs')

    cpe = {
            '4.0.0':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.0.0:*:*:*:*:*:*:*',
            '4.0.2':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.0.2:*:*:*:*:*:*:*',
            '3.0.6':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:3.0.6:*:*:*:*:*:*:*',
            '3.0.5':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:3.0.5:*:*:*:*:*:*:*',
            '3.0.4':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:3.0.4:*:*:*:*:*:*:*',
            '3.0.3':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:3.0.3:*:*:*:*:*:*:*',
            '3.0.2':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:3.0.2:*:*:*:*:*:*:*',
            '3.0.1':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:3.0.1:*:*:*:*:*:*:*',
            '3.0.0':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:3.0.0:*:*:*:*:*:*:*',
            '4.1.7':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.1.7:*:*:*:*:*:*:*',
            '4.1.6':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.1.6:*:*:*:*:*:*:*',
            '4.1.5.1':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.1.5.1:*:*:*:*:*:*:*',
            '4.1.3':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.1.3:*:*:*:*:*:*:*',
            '4.1.2':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.1.2:*:*:*:*:*:*:*',
            '4.1.1':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.1.1:*:*:*:*:*:*:*',
            '4.1.0':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.1.0:*:*:*:*:*:*:*',
            '4.2.5':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.2.5:*:*:*:*:*:*:*',
            '4.2.4.1':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.2.4.1:*:*:*:*:*:*:*',
            '4.2.3.1':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.2.3.1:*:*:*:*:*:*:*',
            '4.2.3':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.2.3:*:*:*:*:*:*:*',
            '4.2.2':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.2.2:*:*:*:*:*:*:*',
            '5.0.0-1_43d8f09a':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:5.0.0-1_43d8f09a:*:*:*:*:*:*:*',
            '4.2.9':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.2.9:*:*:*:*:*:*:*',
            '4.2.8':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.2.8:*:*:*:*:*:*:*',
            '4.2.7':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.2.7:*:*:*:*:*:*:*',
            '4.2.6.1':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.2.6.1:*:*:*:*:*:*:*',
            '4.2.6':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.2.6:*:*:*:*:*:*:*',
            '4.2.4':'cpe:2.3:a:adaptivecomputing:torque_resource_manager:4.2.4:*:*:*:*:*:*:*'
           }

    # TORQUE needs to be added as an external package to SPACK. For this, the
    # config file packages.yaml needs to be adjusted:
    #
    # packages:
    #   torque:
    #     buildable: False
    #     externals:
    #     - spec: torque@3.0.2
    #       prefix: /opt/torque (path to your TORQUE installation)

    def install(self, spec, prefix):
        raise InstallError(
            self.spec.format('{name} is not installable, you need to specify '
                             'it as an external package in packages.yaml'))
