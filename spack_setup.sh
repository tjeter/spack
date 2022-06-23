#!/bin/bash
export MYSPACK=${HOME}/local/spack
mkdir -p ${MYSPACK}
git clone git@github.com:tjeter/spack.git ${MYSPACK}
export SPACK_USER_CONFIG_PATH=${MYSPACK}/user_config
export SPACK_SYSTEM_CONFIG_PATH=${MYSPACK}/sys_config
export SPACK_USER_CACHE_PATH=${MYSPACK}/user_cache
export TEMPDIR=${MYSPACK}/tmp
mkdir -p \
	${SPACK_USER_CONFIG_PATH}  \
	${SPACK_SYSTEM_CONFIG_PATH}\
	${SPACK_USER_CACHE_PATH}   \
	${TEMPDIR}

